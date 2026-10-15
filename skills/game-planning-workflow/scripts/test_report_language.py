"""Run: python3 -B scripts/test_report_language.py (stdlib only)."""

from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

SKILL = Path(__file__).resolve().parents[1]


def self_test():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        # Moving the whole skill catches hidden session/source path dependencies.
        skill = root / "installed"
        shutil.copytree(SKILL, skill, ignore=shutil.ignore_patterns("__pycache__"))
        script = skill / "scripts/check_report_language.py"
        report = root / "01-research.md"
        glossary = root / "00-glossary.md"
        workflow = root / "workflow.json"
        record = root / "05-validation.md"
        report.write_text("# 아이템\n플레이어가 코인을 얻는다.\n", encoding="utf-8")
        glossary.write_text(
            "코인: 상점에서 쓰는 자원. 획득과 해금은 구별한다.\n", encoding="utf-8"
        )

        def run(expected, *extra):
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(script),
                    str(report),
                    "--glossary",
                    str(glossary),
                    *extra,
                ],
                capture_output=True,
                text=True,
            )
            assert result.returncode == expected, result.stdout + result.stderr
            return json.loads(result.stdout)

        initial = run(0, "--lint-only")
        assert initial["status"] == "automatic_pass_manual_pending"
        run(2)  # Missing workflow cannot become a pass.
        workflow.write_text('{"stages":{"validation":{}}}', encoding="utf-8")
        run(1)
        report.write_text("결과가 보여집니다.\n", encoding="utf-8")
        assert any(hit["rule"] == "3.2" for hit in run(1, "--lint-only")["hits"])
        report.write_text("# 아이템\n플레이어가 코인을 얻는다.\n", encoding="utf-8")
        initial = run(0, "--lint-only")
        record.write_text(
            '# 검수\n\n<a id="language"></a>\n제목·본문: 코인의 정의와 작품 근거 대조.\n표현: 문서 표면 수동 대조.\n',
            encoding="utf-8",
        )
        review = {
            "input_sha256": initial["input_sha256"],
            "terminology": {
                "status": "pass",
                "locations": ["제목·본문"],
                "basis": "코인의 정의와 작품 근거 대조",
            },
            "manual_style": {
                "status": "pass",
                "locations": ["표현"],
                "basis": "문서 표면 수동 대조",
            },
            "record": "05-validation.md#language",
            "record_sha256": sha256(record.read_bytes()).hexdigest(),
        }
        data = {
            "stages": {"validation": {"language_reviews": {"01-research.md": review}}}
        }
        workflow.write_text(json.dumps(data), encoding="utf-8")
        assert run(0)["status"] == "recorded_review_current"
        for section in ("terminology", "manual_style"):
            review[section]["status"] = "not_run"
            workflow.write_text(json.dumps(data), encoding="utf-8")
            run(1)
            review[section]["status"] = "pass"
        workflow.write_text(json.dumps(data), encoding="utf-8")
        domain = skill / "references/game-domain-dictionary-v3.md"
        domain_bytes = domain.read_bytes()
        domain.write_bytes(domain_bytes + b"\nchanged\n")
        run(1)
        domain.unlink()
        run(2)
        domain.write_bytes(domain_bytes)
        custom = root / "custom-v3.md"
        custom.write_bytes(domain_bytes)
        custom_result = run(0, "--lint-only", "--domain-dictionary", str(custom))
        assert "custom-v3.md" in custom_result["input_sha256"]
        assert (
            "installed/references/game-domain-dictionary-v3.md"
            not in custom_result["input_sha256"]
        )
        custom.unlink()
        run(2, "--lint-only", "--domain-dictionary", str(custom))
        helper = skill / "scripts/check_research_coverage.py"
        helper_bytes = helper.read_bytes()
        helper.write_bytes(helper_bytes + b"\n# package changed\n")
        run(1)
        helper.write_bytes(helper_bytes)
        record.write_text(record.read_text() + "\n기록 변경\n", encoding="utf-8")
        run(1)
        record.write_text(
            '# 검수\n\n<a id="language"></a>\n제목·본문: 코인의 정의와 작품 근거 대조.\n표현: 문서 표면 수동 대조.\n',
            encoding="utf-8",
        )
        report.write_text("플레이어가 코인을 쓴다.\n", encoding="utf-8")
        run(1)
        report.write_text("# 아이템\n플레이어가 코인을 얻는다.\n", encoding="utf-8")
        glossary.write_text("코인 정의 변경\n", encoding="utf-8")
        run(1)
        glossary.unlink()
        run(2, "--lint-only")
        glossary.write_text("코인: 자원\n", encoding="utf-8")
        report.unlink()
        run(2, "--lint-only")
        report.write_text("코인을 얻는다.\n", encoding="utf-8")
        dictionary = skill / "references/ste-ko/dictionary.md"
        dictionary.write_text("", encoding="utf-8")
        run(2, "--lint-only")
        dictionary.write_text("no dictionary entries", encoding="utf-8")
        run(2, "--lint-only")
        dictionary.unlink()
        run(2, "--lint-only")
    print(
        "PASS: normal, violation, missing inputs, missing/stale review, relocated skill"
    )


if __name__ == "__main__":
    self_test()
