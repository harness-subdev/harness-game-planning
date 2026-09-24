#!/usr/bin/env python3
"""Run: python3 scripts/self_check.py. Uses only temporary generated inputs."""

import copy
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
from build_portal import render


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.tags, self.links, self.text = [], [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.tags.append(tag)
        if "id" in values:
            self.ids.append(values["id"])
        if tag == "a":
            self.links.append(values["href"])
        assert not any(key.startswith("on") for key in values), values
        assert not (tag in {"script", "img", "iframe"} and "src" in values), values

    def handle_data(self, data):
        self.text.append(data)


def rejects(data):
    try:
        render(data)
    except ValueError:
        return
    raise AssertionError(f"Invalid input accepted: {data}")


def main():
    literal = '<img src=x onerror="alert(1)"><script>alert(2)</script> & "quote"'
    base = {"version": 1, "project": {"title": literal, "status": "future-state"}, "sections": []}
    empty = Page(render(base))
    assert "등록된 기획 섹션이 없습니다" in ''.join(empty.text)
    assert "알 수 없는 상태 · future-state" in ''.join(empty.text)
    assert literal in ''.join(empty.text)
    assert "img" not in empty.tags and empty.tags.count("script") == 1
    populated = {**base, "sections": [{"id": "rules", "title": "규칙", "status": "running",
                 "items": [{"id": "one", "title": "규칙 1", "paragraphs": ["내용"], "evidence": "observed"}]}]}
    populated_text = ''.join(Page(render(populated)).text)
    assert "아직 작성된 내용이 없습니다" not in populated_text
    assert "작성 중" in populated_text and "실제 관찰 기록" in populated_text
    for evidence, label in (("not_run", "미실행"), ("illustrative", "설명용 예시"), ("calculated", "계산 근거")):
        populated["sections"][0]["items"][0]["evidence"] = evidence
        assert label in ''.join(Page(render(populated)).text)
    populated["sections"][0]["items"][0]["status"] = "superseded"
    assert "이전 결정 · 대체됨" in "".join(Page(render(populated)).text)
    for section_count, item_count in ((1, 0), (3, 2), (2, 17)):
        data = copy.deepcopy(base)
        for s in range(section_count):
            data["sections"].append({
                "id": f"section-{s}", "title": f"구조 {s}", "paragraphs": [literal],
                "items": [{"id": f"rule-{s}-{i}", "title": f"규칙 {i}", "paragraphs": [literal],
                           "evidence": "assumption",
                           "sources": [{"label": literal, "url": "https://example.com/?a=1&b=2", "source_id": "S-1"}],
                           "tables": [{"columns": ["변수", "값"], "rows": [[literal, ""]]}]}
                          for i in range(item_count)],
                "sources": [{"label": "자기 섹션", "url": f"#section-{s}"}],
                "tables": [{"columns": ["비어 있는 표"], "rows": []}],
            })
        page = Page(render(data))
        assert len(page.ids) == len(set(page.ids)) == 4 + section_count + section_count * item_count
        assert page.tags.count("details") == section_count * item_count
        assert page.tags.count("table") == section_count * (item_count + 1)
        assert all(link[1:] in page.ids for link in page.links if link.startswith("#"))
        assert "미검증" in ''.join(page.text) and "등록된 행이 없습니다" in ''.join(page.text)
        assert literal in ''.join(page.text) and "img" not in page.tags
    for bad_id in ('bad" onclick="x', "UPPER", "", "x" * 65, "portal-top", "-start"):
        bad = copy.deepcopy(data)
        bad["sections"][0]["id"] = bad_id
        rejects(bad)
    bad = copy.deepcopy(data)
    bad["sections"][1]["id"] = bad["sections"][0]["id"]
    rejects(bad)
    for url in ("javascript:alert(1)", "data:text/html,x", "file:///tmp/x", "//example.com", "#missing",
                "https://user:pass@example.com", "https://example.com\\evil", "https://example.com/\nx",
                "https://example.com:bad", "https:///path", "../secret", "https://exa mple.com"):
        bad = copy.deepcopy(data)
        bad["sections"][0]["sources"][0]["url"] = url
        rejects(bad)
    for replacement in ({"version": True}, {"sections": None}, {"raw_html": "<b>x</b>"}):
        rejects({**data, **replacement})
    bad = copy.deepcopy(data)
    bad["sections"][0]["tables"][0]["rows"] = [["extra", "cell"]]
    rejects(bad)
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        source, target = root / "portal.json", root / "index.html"
        source.write_text(json.dumps(data), encoding="utf-8")
        script = Path(__file__).with_name("build_portal.py")
        good = subprocess.run([sys.executable, str(script), str(source), str(target)], capture_output=True, text=True)
        assert good.returncode == 0, good.stderr
        previous = target.read_text(encoding="utf-8")
        assert previous == render(data)
        source.write_text('{"version":', encoding="utf-8")
        fail = subprocess.run([sys.executable, str(script), str(source), str(target)], capture_output=True, text=True)
        assert fail.returncode != 0 and target.read_text(encoding="utf-8") == previous
        assert not list(root.glob(".portal-*.tmp"))
    print("PASS: variable counts, empty/unknown states, IDs, safe links, escaped text, table shape, CLI and output preservation")


if __name__ == "__main__":
    main()
