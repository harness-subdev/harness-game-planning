"""Check document lint and freshness of declared manual reviews, never semantic truth.

python3 check_report_language.py REPORT --glossary GLOSSARY [--workflow WORKFLOW]
Use --lint-only while drafting. Final mode requires current workflow review records.
Exit 0: requested check passed; 1: violations/missing or stale review; 2: input/tool error.
"""

import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys

from check_research_coverage import (
    anchor_sections,
    file_sha256,
    project_path,
    read_json,
)

SKILL = Path(__file__).resolve().parents[1]
STE = SKILL / "references/ste-ko"


def check(report, glossary, workflow, lint_only=False, domain_dictionary=None):
    root = workflow.parent.resolve()
    domain_dictionary = (
        domain_dictionary or SKILL / "references/game-domain-dictionary-v3.md"
    )
    inputs = [
        report,
        glossary,
        domain_dictionary,
        SKILL / "scripts/check_research_coverage.py",
        SKILL / "references/report-language.md",
        STE / "SPEC.md",
        STE / "dictionary.md",
        STE / "scripts/lint.py",
        Path(__file__).resolve(),
    ]
    for path in inputs:
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing/empty input: {path}")

    spec = importlib.util.spec_from_file_location(
        "ste_ko_lint", STE / "scripts/lint.py"
    )
    lint = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lint)
    vocab = lint.load_dictionary(STE / "dictionary.md")
    if not vocab:
        raise ValueError("STE-KO dictionary loaded no entries")
    hits = lint.check(report, "문서", vocab)
    hashes = {
        os.path.relpath(path.resolve(), root): file_sha256(path) for path in inputs
    }
    result = {
        "status": "violations" if hits else "automatic_pass_manual_pending",
        "surface": "문서",
        "input_sha256": hashes,
        "hits": [
            {"line": line, "rule": rule, "message": message}
            for line, rule, message in hits
        ],
        "review_errors": [],
        "scope": "Automated subset only; semantic truth and manual review quality are not verified.",
    }
    if lint_only:
        return result, 1 if hits else 0

    data = read_json(workflow)
    report_key = os.path.relpath(report.resolve(), root)
    reviews = data.get("stages", {}).get("validation", {}).get("language_reviews", {})
    review = reviews.get(report_key, {})
    if not isinstance(review, dict):
        raise ValueError("language_reviews entry must be an object")
    errors = result["review_errors"]
    if review.get("input_sha256") != hashes:
        errors.append("Missing/stale language review input_sha256")

    record = review.get("record", "")
    record_text = ""
    if not isinstance(record, str) or "#" not in record:
        errors.append("Missing 05-validation.md#anchor record")
    else:
        relative, anchor = record.split("#", 1)
        if relative != "05-validation.md" or not anchor:
            errors.append("Expected 05-validation.md#anchor")
        else:
            path = project_path(root, relative)
            if not path.is_file() or file_sha256(path) != review.get("record_sha256"):
                errors.append("Missing/stale validation record")
            else:
                record_text = anchor_sections(path).get(anchor, "")
                if not record_text.strip():
                    errors.append("Missing/nonempty explicit record anchor")

    # ponytail: attestations bind manual work to bytes; a machine cannot prove meaning.
    # Review actual sentences and evidence in validation; add no alias-based semantic score.
    for name in ("terminology", "manual_style"):
        item = review.get(name, {})
        if not isinstance(item, dict):
            raise ValueError(f"{name}: expected review object")
        locations, basis = item.get("locations"), item.get("basis")
        if item.get("status") != "pass":
            errors.append(f"{name}: not reviewed/pass")
        if (
            not isinstance(locations, list)
            or not locations
            or any(not isinstance(v, str) or not v.strip() for v in locations)
            or not isinstance(basis, str)
            or not basis.strip()
        ):
            errors.append(f"{name}: missing locations/basis")
        elif any(value not in record_text for value in [*locations, basis]):
            errors.append(f"{name}: locations/basis absent from validation record")
    if not hits and not errors:
        result["status"] = "recorded_review_current"
    elif errors:
        result["status"] = "review_required"
    return result, 1 if hits or errors else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--glossary", type=Path, required=True)
    parser.add_argument("--workflow", type=Path)
    parser.add_argument(
        "--domain-dictionary",
        type=Path,
        help="Actual V3 input; default: bundled dictionary",
    )
    parser.add_argument("--lint-only", action="store_true")
    args = parser.parse_args()
    workflow = args.workflow or args.report.parent / "workflow.json"
    try:
        result, code = check(
            args.report, args.glossary, workflow, args.lint_only, args.domain_dictionary
        )
    except (OSError, ValueError, TypeError, AttributeError, ImportError) as error:
        result, code = {"status": "error", "error": str(error)}, 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
