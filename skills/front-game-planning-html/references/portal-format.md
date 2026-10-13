# portal.json 입력 형식 · version 1

이 파일은 원본 Markdown에서 작성한 **파생 열람 데이터**다. 빌더는 문서를 해석하거나 수치·출처·실측을 만들어내지 않는다. 내용 변경은 원본 문서에서 시작한다. 모든 문자열은 일반 텍스트이며 HTML 및 Markdown 문법은 해석하지 않는다.

## 지원 범위와 렌더러 선택

version 1은 텍스트·표·상태·문서 목록으로 충분한 **신작 기획 허브**의 실행 형식이다. [문서 모드](../../game-planning-workflow/references/artifact-contract.md#문서-모드와-원작-레퍼런스-보고서)에 맞는 실제 렌더러 선택과 제작 인계는 [HTML 스킬의 렌더러 선택](../SKILL.md#렌더러-선택)을 따른다.

| 실제 동작 | 입력·출력의 한계 |
| --- | --- |
| 텍스트·표·출처 링크, 한 단계 상세 펼침, 검색 | HTML·Markdown을 해석하지 않는다. 이미지·Mermaid·영상 임베드 필드는 없으며 미지원 키는 거부한다. |
| `Section` 아래의 `items` | `Item` 안의 `items`는 거부한다. 문자열 제목에 번호를 적어도 원작 정형 목차의 절 계층·중첩 목차가 생성되지 않는다. |
| 프로젝트·섹션·항목의 상태 배지 | `status`를 생략하거나 빈 값으로 넣어도 미검증 배지를 표시한다. |
| `documents`·`skipped`의 비어 있지 않은 목록 | 원본 문서 경로·생략 기능과 이유를 독자 화면에 출력한다. 파일을 읽거나 링크하지 않는다. |
| 기획 상태 안내·제작 footer | 입력과 관계없이 문서/게임 검증의 구별 안내와 Markdown → JSON → HTML 제작 안내를 출력한다. |

따라서 version 1은 원작 레퍼런스 보고서의 실행 입력으로 사용하지 않는다. 상태 생략·임의 필드·본문 속 파일명으로 필수 표시를 구현한 것처럼 처리하지 않는다. 원작의 [정형 목차](../../game-planning-workflow/references/artifact-contract.md#원작-보고서의-정형-목차), [독자용 문체](../../game-planning-workflow/references/game-terminology.md#독자용-문체와-작업-기록의-경계), [실제 장면](../../game-planning-research/SKILL.md#실제-플레이-장면과-ui-취득)은 지원하는 프로젝트 렌더러로 투영한다. 아래 스키마와 예는 version 1이 실제 지원하는 신작 기획 허브만 설명한다.

## 구조

`?`는 생략 가능 필드다. 아래에 없는 필드는 오타나 누락 방지를 위해 거부한다.

```text
Portal = {
  version: 1,
  project: {title: string, summary?: string, status?: string},
  sections: Section[],
  documents?: string[],
  skipped?: {feature: string, reason: string}[]
}
Section = {
  id: ID, title: string, paragraphs?: string[],
  status?: string, evidence?: string,
  sources?: Source[], tables?: Table[], items?: Item[]
}
Item = {
  id: ID, title: string, paragraphs?: string[],
  status?: string, evidence?: string,
  sources?: Source[], tables?: Table[]
}
Source = {label: string, url: string, source_id?: string}
Table = {caption?: string, columns: string[], rows: string[][]}
```

- `title`, ID, 출처 `label`, `url`, `source_id`, `columns` 이름, `documents` 항목, `feature`, `reason`은 공백만인 문자열이 될 수 없다. 문단·요약·표 셀은 빈 문자열을 허용한다. `null`은 받지 않는다.
- ID는 `[a-z][a-z0-9-]{0,63}`이며 전체 섹션과 항목 사이에서 유일해야 한다. `portal-top`, `portal-search`, `portal-status`, `portal-empty`는 예약어다. 표시 순서나 제목이 바뀌어도 기존 ID를 보존한다.
- 섹션·항목·문단·출처·표 개수에는 게임별 상한을 두지 않는다. 빈 `sections`, `items`, `rows`도 허용하며 읽을 수 있는 빈 상태를 표시한다. 표의 `columns`는 하나 이상이고 각 행은 열 개수와 같아야 한다.
- `status` 생략·빈 값은 `unverified`로 표시한다. 공통 계약의 문서 상태 `pending`, `running`, `done`, `blocked`, `stale`, 기획 상태 `proposed`, `confirmed`, `deferred`, 결정 이력 `superseded`(이전 결정 · 대체됨), 구현 상태 `not_started`, `prototype`, `implemented`, `unknown`을 지원한다. 열람본 보조 상태 `draft`, `unverified`, `not_run` 및 `running`과 같은 뜻의 `in_progress`도 지원한다. 알 수 없는 값은 삭제하지 않고 `알 수 없는 상태 · 원문`으로 표시한다. `done`은 문서 검수 완료로만 표시한다. 대상에 해당하는 상태만 투영하며 구현 여부는 문서 작성 완료에서 추론하지 않는다.
- `evidence`는 선택적인 근거 분류다. 공통 계약의 `not_run`(미실행), `illustrative`(설명용 예시), `calculated`(계산 근거), `observed`(실제 관찰 기록)를 사용한다. `verified`(검증 근거 있음), `researched`(자료 근거 있음), `assumption`(가설), `unverified`(미검증)도 표시를 지원한다. 다른 값도 일반 텍스트로 표시한다. `verified`라는 문자열만으로 실측을 추론하지 않는다. 상태와 근거는 독립 필드이며 자료 조사 완료를 재미 검증으로 간주하지 않는다.
- `sources`는 해당 주장·표·항목과 관련된 출처만 담는다. `source_id`는 원본 `sources.json`의 식별자를 복사한 표시값이며 신규 ID를 임의 발급하지 않는다. 빌더는 출처의 사실성이나 원본 ID 존재 여부를 판정하지 않으므로 생성 단계에서 대조한다.
- 링크는 사용자 정보가 없는 `http://` 또는 `https://` URL, 혹은 해당 입력에 실제 존재하는 섹션·항목을 향한 `#ID`만 허용한다. 공백·제어문자·역슬래시, 상대 파일 경로, `javascript:`, `data:`, `file:`, `//host`는 거부한다. 외부 링크를 클릭하기 전까지 네트워크 요청은 없다.
- 로컬 출처는 해당 출처의 ID·파일 위치·접근일을 표시하는 항목을 만들고 그 항목의 `#ID`로 연결할 수 있다. 원본 파일 경로를 HTTP URL인 것처럼 바꾸지 않는다.
- `documents`는 투영한 원본 파일명/경로의 표시 목록이다. 링크나 파일 읽기에 쓰이지 않는다. 목록만으로 최신성이나 원본과의 일치를 증명하지 않으므로 별도로 입력 해시를 기록한다.
- `skipped`에는 선택 기능을 생략한 이유를 기록한다. 예: `{ "feature": "규칙 시뮬레이터", "reason": "현재 검토는 문서의 수치와 가설 비교만 필요하다." }`.

## 상태와 검증 문맥의 투영

신작의 `SYS/P/V-*`·수락 조건·검증 문맥을 원문대로 유지한다. `status`와 `evidence`는 섹션·항목당 하나씩이다. 함께 필요한 문서/결정/구현/근거 상태는 기존 `tables` 또는 `paragraphs`에 명시한다. V의 방법, 플레이 주체 human/agent(해당할 때), 조건·원자료 위치, 기준 충족 여부와 판정 가능한 주장 범위도 같은 방식으로 표시한다. 실제 에이전트 플레이의 `observed`를 인간의 재미 통과로 해석하지 않는다. `method`, `actor` 같은 새 최상위/항목 필드를 넣지 않는다.

빌더의 형식 검사는 이 문맥의 진실성이나 정본과의 일치 여부를 판단하지 않는다. 입력 해시 비교와 stale 기록·해소는 공통 계약에 따라 실행 에이전트가 수행하며 빌더의 자동 동기화 기능이 아니다.

## 신작 기획 허브 실행 예

아래는 보스·장비·전투를 가정하지 않은 퍼즐 탐험 신작의 초안이다. 원작 조사 사실이나 실제 플레이 테스트 결과의 예가 아니다. 이 JSON은 제공 빌더로 실행할 수 있으며, 원작 보고서용 캡처·그림 데이터는 이 스키마에 억지로 넣지 않는다.

```json
{
  "version": 1,
  "project": {
    "title": "퍼즐 탐험 게임",
    "summary": "플레이 규칙과 검증 계획을 공유하는 초안.",
    "status": "draft"
  },
  "documents": ["00-brief.md", "03-systems.md", "05-validation.md"],
  "sections": [
    {
      "id": "core-loop",
      "title": "핵심 루프",
      "status": "proposed",
      "paragraphs": ["관찰 → 선택 → 결과 확인 → 다음 탐색."],
      "evidence": "assumption",
      "items": [
        {
          "id": "retry-rule",
          "title": "재시작 규칙",
          "status": "proposed",
          "paragraphs": ["패널티는 플레이테스트에서 비교한다."],
          "tables": [
            {
              "caption": "제안과 확인할 조건",
              "columns": ["항목", "내용", "현재 상태"],
              "rows": [
                ["SYS-001", "플레이어가 현재 퍼즐을 다시 시작할 수 있다.", "proposed"],
                ["구현", "규칙을 구현한 게임은 아직 없다.", "not_started"],
                ["V-001", "재시작 후 퍼즐을 다시 풀 수 있는지 확인한다.", "not_run"]
              ]
            }
          ],
          "sources": [{"label": "검증 계획으로 이동", "url": "#validation"}]
        }
      ]
    },
    {
      "id": "validation",
      "title": "검증 계획",
      "status": "not_run",
      "paragraphs": ["실제 테스트는 아직 실행하지 않았다."]
    }
  ],
  "skipped": [{"feature": "게임 플레이어", "reason": "이번 요청은 기획 문서 열람본 제작이다."}]
}
```
