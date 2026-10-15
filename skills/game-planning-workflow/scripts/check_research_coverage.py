"""Check census structure and review freshness, not the truth of source claims.

python3 check_research_coverage.py PROJECT [--gold GOLD_DIR]
0 complete; 1 limited/incomplete; 2 malformed input. Standard library only.
"""

import argparse
from bisect import bisect_left
from collections import defaultdict
from functools import cache
from hashlib import sha256
import json
import math
from pathlib import Path
import re

KINDS = {
    "system": "missing_systems",
    "entity": "missing_entities",
    "attribute": "missing_attributes",
    "relation": "missing_relations",
    "lifecycle": "missing_lifecycle_cases",
}
STATES = {
    "unsearched",
    "searching",
    "supported",
    "observed",
    "inferred",
    "unknown",
    "conflicting",
    "not_applicable",
}
APPLICABILITY = {"applicable", "not_applicable", "unknown"}


def file_sha256(path):
    return sha256(path.read_bytes()).hexdigest()


def obligation_sha256(coverage):
    # Derived reviews/assessment never participate, avoiding a hash cycle.
    def canonical(value):
        if isinstance(value, dict):
            return {
                k: canonical(v)
                for k, v in sorted(value.items())
                if k not in {"reviews", "assessment", "review_records"}
            }
        if isinstance(value, list):
            values = [canonical(v) for v in value]
            return sorted(values, key=lambda v: json.dumps(v, sort_keys=True))
        return value

    payload = {
        key: coverage.get(key)
        for key in ["scope", "requirements", "catalogs", "entities"]
    }
    return sha256(
        json.dumps(
            canonical(payload),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()


def obligation_ids(coverage):
    ids = [r["id"] for r in coverage["requirements"]]
    ids += ["catalog:" + c["id"] for c in coverage["catalogs"]]
    for entity in coverage["entities"]:
        ids.append(entity["id"])
        ids += [entity["id"] + ":" + a["key"] for a in entity["attributes"]]
    return sorted(ids)


def project_path(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError(f"Expected project-relative path: {relative!r}")
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path outside project: {relative}")
    return path


def read_json(path):
    def reject_constant(value):
        raise ValueError("Nonfinite JSON number: " + value)

    data = json.loads(path.read_text(), parse_constant=reject_constant)
    if not isinstance(data, dict):
        raise ValueError(f"{path.name}: expected JSON object")
    return data


def index_records(records, label):
    if not isinstance(records, list) or any(not isinstance(r, dict) for r in records):
        raise ValueError(f"{label}: expected object array")
    indexed = {}
    for record in records:
        ident = record.get("id")
        if not isinstance(ident, str) or not ident or ident in indexed:
            raise ValueError(f"{label}: missing/duplicate ID {ident!r}")
        indexed[ident] = record
    return indexed


def anchor_sections(path):
    """Index the first occurrence of each ID through the next explicit anchor."""
    text = path.read_text()
    boundaries = [match.start() for match in re.finditer(r"<a\s+id=", text)]
    sections = {}
    for match in re.finditer(r"\bid=(?:\"([^\"]*)\"|'([^']*)')", text):
        anchor = match.group(1) if match.group(1) is not None else match.group(2)
        if anchor not in sections:
            following = bisect_left(boundaries, match.end())
            end = boundaries[following] if following < len(boundaries) else len(text)
            sections[anchor] = text[match.end() : end]
    return sections


def conditions_match(actual, required):
    """Evidence may refine unknown conditions, while retaining known restrictions."""
    return (
        isinstance(actual, dict)
        and required.keys() <= actual.keys()
        and all(
            value is None or (isinstance(value, str) and bool(value.strip()))
            for value in actual.values()
        )
        and all(
            value is None or actual[key] == value for key, value in required.items()
        )
    )


def check_coverage(project_dir: Path, gold_dir: Path | None = None) -> dict:
    root = Path(project_dir)
    result = {
        key: []
        for key in [
            "structural_errors",
            "open_catalogs",
            "missing_systems",
            "missing_entities",
            "missing_attributes",
            "missing_relations",
            "missing_lifecycle_cases",
            "unresolved_attributes",
            "missing_report_entries",
            "stale_inputs",
            "review_errors",
        ]
    }
    result.update(schema_version=1, completeness="incomplete", counts_by_category={})
    try:
        _check(root, gold_dir, result)
    except (
        OSError,
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        IndexError,
    ) as error:
        result["structural_errors"].append(str(error))
    blockers = [
        key
        for key in result
        if key
        not in {
            "schema_version",
            "completeness",
            "counts_by_category",
            "unresolved_attributes",
        }
    ]
    if any(result[key] for key in blockers):
        result["completeness"] = "incomplete"
    elif result["unresolved_attributes"]:
        result["completeness"] = "limited"
    else:
        result["completeness"] = "complete"
    return result


def _check(root, gold_dir, result):
    # Per-check lifetime: a resumed check must read changed reports again.
    document_sections = cache(anchor_sections)
    coverage = read_json(root / "coverage.json")
    sources = read_json(root / "sources.json")
    if coverage.get("schema_version") != 1 or sources.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")
    scope = coverage["scope"]
    conditions = scope["conditions"]
    if (
        not isinstance(conditions, dict)
        or not {"edition", "version", "platform"} <= conditions.keys()
    ):
        raise ValueError(
            "scope.conditions needs edition/version/platform (unknown is null)"
        )
    if any(
        value is not None and (not isinstance(value, str) or not value.strip())
        for value in conditions.values()
    ):
        raise ValueError("Scope condition values must be nonblank strings or null")
    if any(value is None for value in conditions.values()):
        result["unresolved_attributes"].append("scope:conditions")
    authors = scope["author_ids"]
    if (
        not isinstance(authors, list)
        or not authors
        or not all(isinstance(a, str) and a.strip() for a in authors)
    ):
        raise ValueError("scope.author_ids must identify actual authors")
    reference_path = project_path(root, scope["reference_path"])
    reference = read_json(reference_path)
    catalogs = index_records(coverage["catalogs"], "catalogs")
    entities = index_records(coverage["entities"], "entities")
    requirements = index_records(coverage["requirements"], "requirements")
    findings = index_records(sources["findings"], "findings")
    source_index = index_records(sources["sources"], "sources")
    inputs = coverage["input_sha256"]
    required_inputs = {
        "00-brief.md",
        "sources.json",
        "01-research.md",
        scope["reference_path"],
    }
    for source in source_index.values():
        locator = source["locator"]
        if not isinstance(locator, str) or not locator:
            raise ValueError("source locator must be nonempty")
        if locator.startswith(("https://", "http://")):
            snapshot = source.get("snapshot_path")
            if not snapshot:
                result["stale_inputs"].append("source snapshot missing:" + source["id"])
            else:
                required_inputs.add(snapshot)
        else:
            required_inputs.add(locator.split("#")[0])
    for required in required_inputs:
        if required not in inputs:
            result["stale_inputs"].append("unhashed:" + required)
    for relative, digest in inputs.items():
        if relative in {"coverage.json", "workflow.json", "05-validation.md"}:
            raise ValueError("Derived records cannot be input hashes: " + relative)
        if file_sha256(project_path(root, relative)) != digest:
            result["stale_inputs"].append(relative)
    if scope.get("brief_sha256") != inputs.get("00-brief.md"):
        result["stale_inputs"].append("scope:brief_sha256")

    def check_refs(ids, label):
        if not isinstance(ids, list) or not ids:
            result["structural_errors"].append(label + ": evidence references required")
            return
        for ident in ids:
            if ident not in findings:
                result["structural_errors"].append(label + ": dangling R " + str(ident))

    for finding in findings.values():
        ids = finding.get("source_ids")
        if (
            not isinstance(ids, list)
            or not ids
            or any(s not in source_index for s in ids)
        ):
            result["structural_errors"].append(finding["id"] + ": dangling/missing S")
        if not finding.get("location") or not finding.get("observation"):
            result["structural_errors"].append(finding["id"] + ": empty finding")
    # Local independent reference is mandatory even when --gold is omitted.
    # An optional external oracle adds obligations, never replaces that reference.
    references = [reference]
    if gold_dir is not None:
        references.append(read_json(Path(gold_dir) / "gold.json"))
    expected_attrs = defaultdict(set)
    expected_contracts = defaultdict(dict)
    for baseline in references:
        ref_catalogs = index_records(baseline["catalogs"], "reference catalogs")
        ref_entities = index_records(baseline["entities"], "reference entities")
        ref_requirements = index_records(
            baseline["requirements"], "reference requirements"
        )
        for ident, required in ref_requirements.items():
            current = requirements.get(ident)
            if current is None or any(
                current.get(k) != required.get(k)
                for k in [
                    "type",
                    "entity_ids",
                    "catalog_ids",
                    "required_attributes",
                    "evidence_kind",
                ]
            ):
                result["structural_errors"].append(
                    "requirement removed/changed:" + ident
                )
        for ident, ref in ref_catalogs.items():
            kind = ref["kind"]
            if kind not in KINDS:
                raise ValueError("Invalid reference catalog kind: " + kind)
            if ref.get("status") not in {"closed", "open"}:
                raise ValueError("Invalid reference catalog status: " + ident)
            if ref["status"] == "open" or ref.get("applicability") == "unknown":
                result["open_catalogs"].append("reference:" + ident)
            current = catalogs.get(ident)
            if current is None:
                result[KINDS[kind]].append("catalog:" + ident)
                continue
            if current.get("kind") != kind:
                result["structural_errors"].append("catalog kind differs:" + ident)
            if current.get("applicability") != ref.get("applicability"):
                result["structural_errors"].append(
                    "catalog applicability differs:" + ident
                )
            if set(ref["expected_ids"]) - set(current["expected_ids"]):
                result[KINDS[kind]].append("reduced denominator:" + ident)
            for eid in ref["expected_ids"]:
                expected_attrs[eid].update(ref["required_attributes"])
                if eid not in entities:
                    result[KINDS[kind]].append(eid)
        for eid, ref in ref_entities.items():
            expected_attrs[eid].update(ref["required_attributes"])
            for key, contract in ref.get("attribute_contracts", {}).items():
                if key not in ref["required_attributes"] or not isinstance(
                    contract, dict
                ):
                    raise ValueError(
                        "Invalid independent attribute contract: " + eid + ":" + key
                    )
                merged = expected_contracts[(eid, key)]
                for flag, required in contract.items():
                    if flag not in {
                        "numeric_required",
                        "rule_case_required",
                    } or not isinstance(required, bool):
                        raise ValueError("Invalid evidence contract flag: " + flag)
                    merged[flag] = merged.get(flag, False) or required
            entity = entities.get(eid)
            if entity is None:
                result[KINDS[ref["kind"]]].append(eid)
            elif any(
                entity.get(k) != ref.get(k)
                for k in ["kind", "catalog_id", "parent_id", "related_entity_ids"]
            ):
                result["structural_errors"].append(
                    "reference entity relationships differ:" + eid
                )
    for req in requirements.values():
        if req["type"] not in KINDS or req["evidence_kind"] not in {
            "exact_fact",
            "behavior",
            "interpretation",
        }:
            raise ValueError("Invalid requirement kind: " + req["id"])
        if not req.get("origin"):
            result["structural_errors"].append(
                "requirement origin missing:" + req["id"]
            )
        if not req["catalog_ids"] and not req["entity_ids"]:
            result["structural_errors"].append("unmapped requirement:" + req["id"])
        for cid in req["catalog_ids"]:
            if cid not in catalogs:
                result[KINDS[req["type"]]].append("requirement catalog:" + cid)
            elif not req["entity_ids"]:
                for eid in catalogs[cid]["expected_ids"]:
                    expected_attrs[eid].update(req["required_attributes"])
        for eid in req["entity_ids"]:
            expected_attrs[eid].update(req["required_attributes"])
            if eid not in entities:
                result[KINDS[req["type"]]].append(eid)
    for cat in catalogs.values():
        kind = cat["kind"]
        if kind not in KINDS or cat["applicability"] not in APPLICABILITY:
            raise ValueError("Invalid catalog: " + cat["id"])
        if cat["status"] not in {"closed", "open"}:
            raise ValueError("Catalog status must be closed/open")
        if cat["status"] == "open" or cat["applicability"] == "unknown":
            result["open_catalogs"].append(cat["id"])
        check_refs(cat["basis_r_ids"], "catalog:" + cat["id"])
        if cat["applicability"] == "not_applicable" and cat["expected_ids"]:
            result["structural_errors"].append("NA catalog has entities:" + cat["id"])
        for eid in cat["expected_ids"]:
            expected_attrs[eid].update(cat["required_attributes"])
            if eid not in entities:
                result[KINDS[kind]].append(eid)
    counts = defaultdict(
        lambda: {
            "expected": 0,
            "present": 0,
            "required_attributes": 0,
            "supported_attributes": 0,
            "unknown": 0,
            "not_applicable": 0,
        }
    )
    for cat in catalogs.values():
        counts[cat["id"]]["expected"] = len(set(cat["expected_ids"]))
        counts[cat["id"]]["required_attributes"] = sum(
            len(expected_attrs[eid]) for eid in set(cat["expected_ids"])
        )
    for entity in entities.values():
        eid = entity["id"]
        cid = entity["catalog_id"]
        kind = entity["kind"]
        if kind not in KINDS or cid not in catalogs:
            raise ValueError("Invalid entity kind/catalog: " + eid)
        if eid not in catalogs[cid]["expected_ids"]:
            result["structural_errors"].append("uncatalogued entity:" + eid)
        counts[cid]["present"] += 1
        if entity.get("parent_id") and entity["parent_id"] not in entities:
            result["structural_errors"].append("dangling parent:" + eid)
        related = entity["related_entity_ids"]
        if not isinstance(related, list) or any(v not in entities for v in related):
            result["structural_errors"].append("dangling related entity:" + eid)
        if kind in {"relation", "lifecycle"} and not related:
            result["structural_errors"].append("related_entity_ids required:" + eid)
        if isinstance(entity.get("conditions"), dict) and any(
            value is None for value in entity["conditions"].values()
        ):
            result["unresolved_attributes"].append(eid + ":conditions")
        attrs = entity["attributes"]
        keys = [a["key"] for a in attrs]
        if len(keys) != len(set(keys)):
            raise ValueError("Duplicate attribute: " + eid)
        for key in expected_attrs[eid] - set(keys):
            result["missing_attributes"].append(eid + ":" + key)
        for attr in attrs:
            aid = eid + ":" + attr["key"]
            state = attr["status"]
            applicable = attr["applicability"]
            unresolved_before = len(result["unresolved_attributes"])
            errors_before = sum(
                len(result[key])
                for key in [
                    "structural_errors",
                    "missing_attributes",
                    "missing_report_entries",
                ]
            )
            contract = expected_contracts[(eid, attr["key"])]
            if state not in STATES or applicable not in APPLICABILITY:
                raise ValueError("Invalid attribute status: " + aid)
            if applicable == "unknown" or state in {"unsearched", "searching"}:
                result["missing_attributes"].append(aid)
                continue
            if applicable == "not_applicable" or state == "not_applicable":
                if applicable != "not_applicable" or state != "not_applicable":
                    result["structural_errors"].append(
                        "NA status/applicability mismatch:" + aid
                    )
                check_refs(attr["r_ids"], aid)
                counts[cid]["not_applicable"] += 1
            elif state in {"unknown", "conflicting"}:
                check_refs(attr["attempt_r_ids"], aid + ": attempted search")
                result["unresolved_attributes"].append(aid)
                counts[cid]["unknown"] += 1
            else:
                check_refs(attr["r_ids"], aid)
                evidence_kinds = {
                    r["evidence_kind"]
                    for r in requirements.values()
                    if eid in r["entity_ids"]
                    or (not r["entity_ids"] and cid in r["catalog_ids"])
                }
                if state == "inferred" and (
                    evidence_kinds != {"interpretation"}
                    or not attr.get("inference_note")
                ):
                    result["missing_attributes"].append(
                        aid + ": inferred exact/unsupported fact"
                    )
                for rid in attr["r_ids"]:
                    if rid not in findings:
                        continue
                    finding = findings[rid]
                    confidence = finding.get("confidence")
                    if confidence not in {"supported", "observed"} and not (
                        state == "inferred" and confidence == "hypothesis"
                    ):
                        result["missing_attributes"].append(aid + ": unsupported R")
                    if state == "observed" and confidence != "observed":
                        result["missing_attributes"].append(aid + ": not observed")
                    if attr.get("numeric_required") or contract.get("numeric_required"):
                        _numeric(
                            finding.get("numeric"), entity["conditions"], aid, result
                        )
                    if (
                        kind in {"relation", "lifecycle"}
                        or attr.get("rule_case_required")
                        or contract.get("rule_case_required")
                    ):
                        cases = finding.get("rule_cases")
                        if not isinstance(cases, list) or not cases:
                            result["missing_attributes"].append(
                                aid + ": rule_cases required"
                            )
                        else:
                            for case in cases:
                                if any(
                                    not case.get(k)
                                    for k in [
                                        "initial_state",
                                        "event",
                                        "expected_state",
                                        "basis_location",
                                    ]
                                ):
                                    result["structural_errors"].append(
                                        aid + ": empty rule case"
                                    )
                                if not conditions_match(
                                    case.get("conditions"), entity["conditions"]
                                ):
                                    result["structural_errors"].append(
                                        aid + ": rule conditions differ"
                                    )
            if not conditions_match(entity.get("conditions"), conditions):
                result["structural_errors"].append("entity outside scope:" + eid)
            entry = attr["report_anchor"]
            if not isinstance(entry, str) or "#" not in entry:
                result["missing_report_entries"].append(aid + ": anchor missing")
                continue
            relative, anchor = entry.split("#", 1)
            path = project_path(root, relative)
            if relative != "01-research.md":
                result["missing_report_entries"].append(aid + ": not canonical report")
            excerpt = attr.get("report_excerpt")
            if (
                relative not in inputs
                or not anchor
                or not path.is_file()
                or anchor not in document_sections(path)
                or not isinstance(excerpt, str)
                or not excerpt.strip()
            ):
                result["missing_report_entries"].append(aid)
            else:
                section = document_sections(path)[anchor]
                if excerpt not in section:
                    result["missing_report_entries"].append(
                        aid + ": excerpt absent from anchor section"
                    )
            if (
                attr["key"] in expected_attrs[eid]
                and applicable == "applicable"
                and state in {"supported", "observed", "inferred"}
                and len(result["unresolved_attributes"]) == unresolved_before
                and sum(
                    len(result[key])
                    for key in [
                        "structural_errors",
                        "missing_attributes",
                        "missing_report_entries",
                    ]
                )
                == errors_before
            ):
                counts[cid]["supported_attributes"] += 1
    result["counts_by_category"] = dict(counts)
    _reviews(root, coverage, result, document_sections)


def _numeric(numeric, conditions, aid, result):
    if (
        not isinstance(numeric, dict)
        or not {"value", "unit", "conditions", "basis_location"} <= numeric.keys()
    ):
        result["structural_errors"].append(aid + ": numeric fields required")
        return
    if (
        not isinstance(numeric["unit"], str)
        or not numeric["unit"].strip()
        or not numeric["basis_location"]
    ):
        result["structural_errors"].append(aid + ": numeric unit/location required")
    if not conditions_match(numeric["conditions"], conditions):
        result["structural_errors"].append(aid + ": numeric conditions differ")
    value = numeric["value"]
    interval = numeric.get("range")
    formula = numeric.get("formula")
    if value is not None and (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or (isinstance(value, float) and not math.isfinite(value))
    ):
        result["structural_errors"].append(aid + ": invalid numeric value")
    if interval is not None and (
        not isinstance(interval, list)
        or len(interval) != 2
        or any(
            isinstance(v, bool)
            or not isinstance(v, (int, float))
            or (isinstance(v, float) and not math.isfinite(v))
            for v in interval
        )
        or interval[0] > interval[1]
    ):
        result["structural_errors"].append(aid + ": invalid range")
    if formula is not None and (not isinstance(formula, str) or not formula.strip()):
        result["structural_errors"].append(aid + ": invalid formula")
    if value is None and interval is None and not formula:
        result["unresolved_attributes"].append(aid + ": numeric unknown")


def _reviews(root, coverage, result, document_sections):
    expected = obligation_ids(coverage)
    digest = obligation_sha256(coverage)
    reviews = coverage["reviews"]
    if not isinstance(reviews, list) or not reviews:
        result["review_errors"].append("independent review not run")
        return
    valid = False
    for review in reviews:
        errors = []
        ident = review.get("reviewer_id")
        if not ident or ident in coverage["scope"]["author_ids"]:
            errors.append("reviewer missing/self review")
        if (
            review.get("input_sha256") != coverage["input_sha256"]
            or review.get("obligation_sha256") != digest
        ):
            errors.append("stale input/obligation hashes")
        if sorted(review.get("obligation_ids", [])) != expected:
            errors.append("not full obligation set")
        judgments = review.get("judgments", [])
        if (
            not isinstance(judgments, list)
            or sorted(j.get("id", "") for j in judgments) != expected
        ):
            errors.append("not full judgments")
        else:
            for judgment in judgments:
                if judgment.get("verdict") not in {
                    "pass",
                    "unresolved",
                } or not judgment.get("basis"):
                    errors.append("failed/unsubstantiated judgment:" + judgment["id"])
                if judgment.get("verdict") == "unresolved":
                    result["unresolved_attributes"].append("review:" + judgment["id"])
        record = review.get("record", "")
        if "#" not in record:
            errors.append("review record missing")
        else:
            relative, anchor = record.split("#", 1)
            if not anchor.strip():
                errors.append("review record anchor empty")
            if relative != "05-validation.md":
                errors.append("review record must be 05-validation.md")
            path = project_path(root, relative)
            if (
                not path.is_file()
                or anchor not in document_sections(path)
                or file_sha256(path) != review.get("record_sha256")
            ):
                errors.append("missing/stale review record")
            else:
                record_text = document_sections(path)[anchor]
                if (
                    ident not in record_text
                    or digest not in record_text
                    or any(
                        j["id"] not in record_text
                        or j.get("basis", "") not in record_text
                        for j in judgments
                    )
                ):
                    errors.append("record lacks reviewer/hash/full evidence judgments")
                rows = [
                    line.strip().split(" | ", 2)
                    for line in record_text.splitlines()
                    if " | " in line
                ]
                rows = [row for row in rows if row[0] in expected]
                expected_rows = sorted(
                    [j["id"], j.get("verdict", ""), j.get("basis", "")]
                    for j in judgments
                )
                if sorted(rows) != expected_rows:
                    errors.append(
                        "record verdict/evidence rows differ from review judgments"
                    )
        if not errors:
            valid = True
        else:
            result["review_errors"].extend(str(ident) + ": " + e for e in errors)
    # Old reviews may be archived in validation, not left as current reviews.
    if not valid:
        result["review_errors"].append("no current independent whole-obligation review")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--gold", type=Path)
    args = parser.parse_args()
    result = check_coverage(args.project_dir, args.gold)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return (
        2
        if result["structural_errors"]
        else (0 if result["completeness"] == "complete" else 1)
    )


if __name__ == "__main__":
    raise SystemExit(main())
