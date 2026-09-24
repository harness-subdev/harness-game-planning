#!/usr/bin/env python3
"""Build a self-contained planning portal from a derived JSON projection."""

import argparse
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import urlsplit

ID = re.compile(r"[a-z][a-z0-9-]{0,63}\Z")
RESERVED = {"portal-top", "portal-search", "portal-status", "portal-empty"}
STATUSES = {
    "draft": "초안", "unverified": "미검증", "pending": "대기",
    "running": "작성 중", "in_progress": "작성 중", "done": "문서 검수 완료", "blocked": "진행 불가",
    "stale": "원본 변경 · 갱신 필요", "not_run": "미실행",
    "proposed": "제안", "confirmed": "확인된 기획", "deferred": "보류",
    "not_started": "구현 미착수", "prototype": "프로토타입", "implemented": "구현됨",
    "unknown": "상태 미확인", "superseded": "이전 결정 · 대체됨",
}
EVIDENCE = {
    "verified": "검증 근거 있음", "researched": "자료 근거 있음",
    "assumption": "가설", "unverified": "미검증", "not_run": "미실행",
    "illustrative": "설명용 예시", "calculated": "계산 근거", "observed": "실제 관찰 기록",
}


def obj(value, required, optional, path):
    if not isinstance(value, dict):
        raise ValueError(f"{path}: 객체가 필요합니다")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    if missing or extra:
        raise ValueError(f"{path}: 누락 {sorted(missing)}, 알 수 없는 필드 {sorted(extra)}")
    return value


def seq(value, path):
    if not isinstance(value, list):
        raise ValueError(f"{path}: 배열이 필요합니다")
    return value


def txt(value, path, nonempty=False):
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ValueError(f"{path}: {'비어 있지 않은 ' if nonempty else ''}문자열이 필요합니다")
    return value


def safe_link(value, ids):
    if any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in value) or "\\" in value:
        raise ValueError(f"허용하지 않는 링크: {value!r}")
    if value.startswith("#"):
        if value[1:] not in ids:
            raise ValueError(f"대상이 없는 내부 링크: {value!r}")
        return
    try:
        parsed = urlsplit(value)
        if (parsed.scheme not in {"http", "https"} or not parsed.hostname
                or parsed.username is not None or parsed.password is not None):
            raise ValueError("HTTP(S) 출처 링크가 필요합니다")
        parsed.port  # Reject malformed ports before creating the HTML.
    except ValueError as error:
        raise ValueError(f"허용하지 않는 링크: {value!r} ({error})") from error


def validate(data):
    obj(data, {"version", "project", "sections"}, {"documents", "skipped"}, "portal")
    if type(data["version"]) is not int or data["version"] != 1:
        raise ValueError("version은 정수 1이어야 합니다")
    project = obj(data["project"], {"title"}, {"summary", "status"}, "project")
    txt(project["title"], "project.title", True)
    for key in ("summary", "status"):
        if key in project:
            txt(project[key], f"project.{key}")
    for value in seq(data.get("documents", []), "documents"):
        txt(value, "documents[]", True)
    for entry in seq(data.get("skipped", []), "skipped"):
        obj(entry, {"feature", "reason"}, set(), "skipped[]")
        for key in ("feature", "reason"):
            txt(entry[key], f"skipped[].{key}", True)

    ids, links = set(), []

    def block(entry, path, section=False):
        optional = {"paragraphs", "status", "evidence", "sources", "tables"}
        obj(entry, {"id", "title"}, optional | ({"items"} if section else set()), path)
        identifier = txt(entry["id"], f"{path}.id", True)
        if not ID.fullmatch(identifier) or identifier in RESERVED or identifier in ids:
            raise ValueError(f"{path}.id: 유효하지 않거나 중복된 ID {identifier!r}")
        ids.add(identifier)
        txt(entry["title"], f"{path}.title", True)
        for key in ("status", "evidence"):
            if key in entry:
                txt(entry[key], f"{path}.{key}")
        for paragraph in seq(entry.get("paragraphs", []), f"{path}.paragraphs"):
            txt(paragraph, f"{path}.paragraphs[]")
        for source in seq(entry.get("sources", []), f"{path}.sources"):
            obj(source, {"label", "url"}, {"source_id"}, f"{path}.sources[]")
            for key, value in source.items():
                txt(value, f"{path}.sources[].{key}", True)
            links.append(source["url"])
        for table in seq(entry.get("tables", []), f"{path}.tables"):
            obj(table, {"columns", "rows"}, {"caption"}, f"{path}.tables[]")
            if "caption" in table:
                txt(table["caption"], f"{path}.tables[].caption")
            columns = seq(table["columns"], f"{path}.tables[].columns")
            if not columns:
                raise ValueError(f"{path}: 표에는 하나 이상의 열이 필요합니다")
            for column in columns:
                txt(column, f"{path}.tables[].columns[]", True)
            for row in seq(table["rows"], f"{path}.tables[].rows"):
                if len(seq(row, f"{path}.tables[].rows[]")) != len(columns):
                    raise ValueError(f"{path}: 표 행과 열의 개수가 다릅니다")
                for cell in row:
                    txt(cell, f"{path}.tables[].rows[][]")
        if section:
            for index, item in enumerate(seq(entry.get("items", []), f"{path}.items")):
                block(item, f"{path}.items[{index}]")

    for index, section in enumerate(seq(data["sections"], "sections")):
        block(section, f"sections[{index}]", True)
    for link in links:
        safe_link(link, ids)


def esc(value):
    return html.escape(value, quote=True)


def badges(entry):
    status = entry.get("status", "").strip() or "unverified"
    label = STATUSES.get(status, f"알 수 없는 상태 · {status}")
    out = f'<span class="badge">{esc(label)}</span>'
    evidence = entry.get("evidence", "").strip()
    if evidence:
        out += f'<span class="badge evidence">근거: {esc(EVIDENCE.get(evidence, evidence))}</span>'
    return f'<span class="badges">{out}</span>'


def content(entry):
    parts = [f'<p class="paragraph">{esc(p)}</p>' for p in entry.get("paragraphs", [])]
    for table in entry.get("tables", []):
        columns = table["columns"]
        rows = ''.join('<tr>' + ''.join(f'<td>{esc(cell)}</td>' for cell in row) + '</tr>'
                       for row in table["rows"])
        if not rows:
            rows = f'<tr><td colspan="{len(columns)}" class="muted">등록된 행이 없습니다.</td></tr>'
        caption = esc(table.get("caption") or "기획 표")
        heads = ''.join(f'<th scope="col">{esc(column)}</th>' for column in columns)
        parts.append(f'<div class="table-wrap" role="region" aria-label="{caption}" tabindex="0">'
                     f'<table><caption>{caption}</caption><thead><tr>{heads}</tr></thead>'
                     f'<tbody>{rows}</tbody></table></div>')
    sources = []
    for source in entry.get("sources", []):
        source_id = f' <span class="source-id">[{esc(source["source_id"])}]</span>' if "source_id" in source else ''
        sources.append(f'<li><a href="{esc(source["url"])}" rel="noreferrer">{esc(source["label"])}</a>{source_id}</li>')
    if sources:
        parts.append('<div class="sources"><strong>근거·관련 링크</strong><ul>' + ''.join(sources) + '</ul></div>')
    return ''.join(parts) or ('' if entry.get("items") else '<p class="muted">아직 작성된 내용이 없습니다.</p>')


CSS = """
:root{color-scheme:light;--ink:#202c2a;--muted:#52635e;--paper:#f7f6f0;--line:#d6ded6;--accent:#195c46}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:1rem}body{margin:0;color:var(--ink);background:var(--paper);font:16px/1.7 system-ui,-apple-system,sans-serif}a{color:var(--accent);text-underline-offset:.2em}a:hover{text-decoration-thickness:2px}:focus-visible{outline:3px solid #9a5c00;outline-offset:4px}[hidden]{display:none!important}.skip{position:absolute;left:1rem;top:-6rem;background:white;padding:.7rem;z-index:2}.skip:focus{top:1rem}.layout{display:grid;grid-template-columns:16rem minmax(0,1fr);max-width:92rem;margin:auto}.sidebar{padding:2rem 1.5rem;border-right:1px solid var(--line);position:sticky;top:0;height:100vh;overflow:auto}.brand{font-size:.8rem;letter-spacing:.13em;font-weight:750}.sidebar ol{padding-left:1.4rem}.sidebar li{padding:.3rem 0}.sidebar a{overflow-wrap:anywhere}main{min-width:0;padding:3rem clamp(1.2rem,4vw,4.5rem)}h1{font-size:clamp(2rem,4vw,3.6rem);line-height:1.2;letter-spacing:-.04em;margin:1rem 0}h2{font-size:1.6rem;line-height:1.4;margin:0 0 .8rem}h2 a{color:inherit;text-decoration:none}h2 a:hover{text-decoration:underline}.hero{padding-bottom:2rem}.hero-summary{font-size:1.15rem;max-width:65ch}.muted,.source-id{color:var(--muted)}.notice{border-left:3px solid #b78427;padding:.5rem 1rem;background:#f2ecdb;font-size:.9rem}.badges{display:flex;gap:.45rem;flex-wrap:wrap;margin:.7rem 0}.badge{font-size:.78rem;font-weight:650;border:1px solid #b6c6bc;border-radius:5px;padding:.15rem .55rem;background:#edf3ed}.evidence{background:#f4eedf;border-color:#d7c9a2}.search{border-block:1px solid var(--line);padding:1.2rem 0;margin-bottom:2rem}.search label{display:block;font-weight:700}.search input{width:100%;max-width:40rem;font:inherit;padding:.65rem .85rem;border:1px solid #899b91;border-radius:6px;background:white;color:var(--ink)}.search p{font-size:.85rem;margin:.4rem 0 0}.doc-section{border-bottom:1px solid var(--line);padding:0 0 2rem;margin-bottom:2rem;scroll-margin-top:1.5rem}.paragraph{white-space:pre-wrap;overflow-wrap:anywhere}.item{background:#fffef9;border:1px solid var(--line);border-radius:8px;margin:1rem 0;scroll-margin-top:1.5rem}.item summary{cursor:pointer;padding:1rem;font-weight:700;overflow-wrap:anywhere}.item[open] summary{border-bottom:1px solid var(--line)}.item-content{padding:0 1.1rem 1.1rem}.permalink{font-size:.8rem}.table-wrap{max-width:100%;overflow:auto;margin:1.3rem 0;border:1px solid var(--line);border-radius:5px}table{border-collapse:collapse;width:100%;font-size:.9rem}caption{text-align:left;font-weight:700;padding:.65rem;background:#edf1e9}th,td{vertical-align:top;text-align:left;padding:.7rem;border-bottom:1px solid var(--line);min-width:8rem;white-space:pre-wrap;overflow-wrap:anywhere}th{background:#f2f5ef}tr:last-child td{border-bottom:0}.sources{font-size:.85rem;padding:.7rem 0}.sources ul{margin:.3rem 0;padding-left:1.3rem}.sources a{overflow-wrap:anywhere}.metadata{font-size:.85rem;margin-top:2rem}.metadata li{overflow-wrap:anywhere}footer{font-size:.8rem;color:var(--muted);margin-top:2rem}
@media(max-width:780px){.layout{display:block}.sidebar{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);padding:1.2rem}.sidebar ol{columns:2;column-gap:2rem;margin-bottom:0}main{padding:1.5rem 1.2rem}h1{font-size:2.1rem}.hero{padding-bottom:1rem}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{.sidebar,.search,.skip,.permalink{display:none}.layout{display:block}main{padding:0}.item{break-inside:avoid}body{background:white}}
"""

JS = """
const search=document.getElementById('portal-search');
const status=document.getElementById('portal-status');
const empty=document.getElementById('portal-empty');
const sections=[...document.querySelectorAll('.doc-section')];
function filter(){
  const q=search.value.trim().toLocaleLowerCase();
  let count=0;
  for(const section of sections){
    const own=section.querySelector('[data-section-text]').textContent.toLocaleLowerCase().includes(q);
    let match=own;
    for(const item of section.querySelectorAll('.item')){
      item.hidden=!(own||item.textContent.toLocaleLowerCase().includes(q));
      if(!item.hidden){match=true;if(q)item.open=true;}
    }
    section.hidden=!match;
    if(match)count++;
  }
  status.textContent=`전체 ${sections.length}개 중 ${count}개 섹션 표시`;
  empty.hidden=count!==0||sections.length===0;
}
search.addEventListener('input',filter);
function reveal(hash=location.hash){
  let id;
  try{id=decodeURIComponent(hash.slice(1));}catch{return;}
  const target=document.getElementById(id);
  if(!target)return;
  if(target.closest('.doc-section')){search.value='';filter();}
  if(target.matches('details'))target.open=true;
  requestAnimationFrame(()=>target.scrollIntoView());
}
window.addEventListener('hashchange',()=>reveal());
document.addEventListener('click',event=>{
  const link=event.target.closest('a[href^="#"]');
  if(link)reveal(link.getAttribute('href'));
});
filter();
reveal();
"""


def render(data):
    validate(data)
    project = data["project"]
    nav = ''.join(f'<li><a href="#{section["id"]}">{esc(section["title"])}</a></li>'
                  for section in data["sections"])
    sections = []
    for section in data["sections"]:
        items = []
        for item in section.get("items", []):
            items.append(f'<details class="item" id="{item["id"]}"><summary>{esc(item["title"])}</summary>'
                         f'<div class="item-content">{badges(item)}<a class="permalink" href="#{item["id"]}">항목 링크</a>'
                         f'{content(item)}</div></details>')
        if "items" in section and not items:
            items.append('<p class="muted">등록된 상세 항목이 없습니다.</p>')
        sections.append(f'<section class="doc-section" id="{section["id"]}"><div data-section-text>'
                        f'<h2><a href="#{section["id"]}">{esc(section["title"])}</a></h2>'
                        f'{badges(section)}{content(section)}</div>{"".join(items)}</section>')
    if not sections:
        sections.append('<p class="muted">등록된 기획 섹션이 없습니다. 원본 문서에서 내용을 작성한 뒤 다시 생성하세요.</p>')
    documents = ''.join(f'<li>{esc(doc)}</li>' for doc in data.get("documents", []))
    metadata = f'<div class="metadata"><strong>투영한 원본 문서</strong><ul>{documents}</ul></div>' if documents else ''
    skipped = ''.join(f'<li><strong>{esc(s["feature"])}</strong>: {esc(s["reason"])}</li>' for s in data.get("skipped", []))
    if skipped:
        metadata += f'<div class="metadata"><strong>생략한 선택 기능과 이유</strong><ul>{skipped}</ul></div>'
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(project["title"])} · 기획 열람본</title><style>{CSS}</style></head>
<body><a class="skip" href="#portal-top">본문으로 이동</a><div class="layout">
<aside class="sidebar"><a class="brand" href="#portal-top">GAME PLANNING</a><nav aria-label="기획 섹션 목차"><ol>{nav}</ol></nav></aside>
<main id="portal-top"><header class="hero"><div class="brand">기획 문서 열람본</div><h1>{esc(project["title"])}</h1>
{badges(project)}<p class="hero-summary paragraph">{esc(project.get("summary", ""))}</p>
<p class="notice">문서 준비 상태와 게임 검증은 별개입니다. 문서 검수 완료는 재미·밸런스·사업성의 실측 검증을 의미하지 않습니다.</p></header>
<div class="search"><label for="portal-search">기획 내용 검색</label><input id="portal-search" type="search" placeholder="규칙, 가설, 항목 이름 검색" aria-describedby="portal-status"><p id="portal-status" role="status" aria-live="polite"></p><noscript>브라우저 찾기 기능으로 검색할 수 있습니다. 모든 내용은 아래에서 읽을 수 있습니다.</noscript></div>
<p id="portal-empty" class="muted" hidden>검색 결과가 없습니다. 다른 단어로 검색해 주세요.</p>{''.join(sections)}{metadata}
<footer>원본 Markdown → portal.json → HTML · 기획 내용은 원본 문서에서 수정한 뒤 재생성합니다.</footer></main></div><script>{JS}</script></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_html", type=Path)
    args = parser.parse_args()
    temporary = None
    try:
        if args.input_json.resolve() == args.output_html.resolve():
            raise ValueError("입력 JSON과 출력 HTML 경로는 달라야 합니다")
        result = render(json.loads(args.input_json.read_text(encoding="utf-8")))
        args.output_html.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=args.output_html.parent,
                                         prefix=".portal-", suffix=".tmp", delete=False) as output:
            temporary = Path(output.name)
            output.write(result)
        os.replace(temporary, args.output_html)
        print(f"HTML 생성 완료: {args.output_html.resolve()}")
    except (OSError, ValueError) as error:
        print(f"오류: {error}", file=sys.stderr)
        return 1
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
