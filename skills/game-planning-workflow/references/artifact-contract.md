# 공통 산출물 계약

각 프로젝트의 기존 기획 경로를 우선 사용한다. 없으면 `<project>/game-planning/`를 만든다. 기존 파일을 먼저 읽고 병합하며 다른 프로젝트의 자료를 섞지 않는다. 작은 프로젝트에서는 각 문서가 짧아도 된다. 없는 시스템이나 임의의 콘텐츠 수를 채우지 않는다.

## 원본과 파생물

| 파일 | 소유 단계 | 포함 내용 |
| --- | --- | --- |
| `00-brief.md` | research, 이후 총괄 관리 | 사용자 원문 요구, 대상 경험/플레이어/플랫폼/입력, 장르, 제약, 범위, 열린 질문과 가정 |
| `sources.json` | research | 출처, 관찰, 해석, 적용 후보, 상충 정보 |
| `01-research.md` | research | 조사 질문·검색 범위·비교·시사점·채택/보류 근거 |
| `02-concept.md` | concept | 한 줄 컨셉, 재미 가설, 핵심 반복, 선택, 성공/실패/재시작, MVP와 제외 범위 |
| `03-systems.md` | systems | 규칙·상태·콘텐츠 명세, 수치의 단위와 근거, 예외·조합·금지 조건 |
| `04-progression.md` | progression | 학습·성장·세션/콘텐츠 진행, 난도와 회복 의도, 연결과 도입 순서 |
| `05-validation.md` | validation | 문서 일관성 결과, 가설별 검증 계획, 실제 실행 근거와 미실행, 수정 우선순위 |
| `workflow.json` | 총괄 | 단계 상태, 입력 해시, 산출물, 결정 이력, 재개 위치 |
| `portal.json` | html | 위 문서로부터 만든 표시용 데이터. 정본이 아님 |
| `index.html` | html | `portal.json`에서 빌드하는 로컬 열람본. 직접 편집하지 않음 |
| `evidence/` | 증거를 생성한 단계 | 실제로 확인한 스크린샷·테스트 결과·출처 발췌 위치. 필요할 때만 생성 |

위 문서의 게임 기획 내용이 정본이다. 외부 프로젝트에서 CSV/JSON/코드가 이미 특정 수치의 정본이면 그 소유권을 brief에 기록하고 참조한다. 같은 수치를 문서에서 독립 관리하지 않는다. 문서 변경 → portal.json 재투영 → index.html 재생성 순서다. 빌더가 Markdown을 자동 의미 해석하거나 동기화하는 것은 아니다.

## 근거 추적

문서의 주요 항목에 안정적인 ID를 둔다. 예: `R-01` 관찰, `D-01` 결정, `C-01` 컨셉 가설, `SYS-01` 시스템, `P-01` 진행 단위, `V-01` 검증. 제목이 바뀌어도 ID를 재활용하거나 삭제된 ID를 다른 의미에 쓰지 않는다. HTML에는 `sys-01` 같은 소문자 앵커로 매핑한다.

각 중요한 결정은 다음 연결을 가진다.

`출처 S → 관찰 R → 결정 D → 명세 SYS/P → 검증 V`

독자적인 아이디어에 외부 출처를 만들어 붙이지 않는다. `근거: 사용자 요구` 또는 `새 가설, 검증 V-03`으로 기록할 수 있다. 단순 장식이나 문장마다 ID를 강제하지 않는다.

### sources.json

```json
{
  "schema_version": 1,
  "sources": [
    {
      "id": "S-01",
      "title": "사용자 브리프",
      "locator": "00-brief.md",
      "accessed_at": "2026-09-24",
      "published_at": null,
      "kind": "user",
      "reliability_note": "사용자 요구이며 시장 검증 자료는 아님"
    }
  ],
  "findings": [
    {
      "id": "R-01",
      "source_ids": ["S-01"],
      "location": "플랫폼과 조작 조건",
      "observation": "사용자가 세로 화면과 한 손 조작을 요청함",
      "interpretation": "짧은 입력으로 읽을 수 있는 선택이 중요할 수 있음",
      "application": "조작 후보를 비교하고 프로토타입에서 확인",
      "confidence": "hypothesis"
    }
  ],
  "conflicts": []
}
```

이는 형식 예시이며 새 프로젝트의 실제 요구로 복사하지 않는다. `kind`: user, official, observed, secondary. `confidence`: observed, supported, hypothesis, unknown. 접근할 수 없었던 페이지는 그 사실만 기록하고 본문을 확인한 것처럼 관찰을 작성하지 않는다. 게시일을 알 수 없으면 null. 충돌은 ID, 서로 다른 주장과 source_ids, 영향받는 결정, 해결 상태/근거로 기록한다. 최신이라는 이유만으로 자동 승자를 정하지 않는다.

## 서로 다른 상태

- **문서 단계**: pending, running, done, stale, blocked. 산출물이 검수되면 done이며 사용자의 승인이나 게임의 재미가 입증됐다는 뜻이 아니다.
- **기획 항목**: proposed, confirmed, deferred. confirmed는 명시된 사용자 결정 또는 기존 승인 자료가 있을 때만 사용한다.
- **구현**: not_started, prototype, implemented, unknown. 기획서를 썼다는 이유로 implemented로 올리지 않는다.
- **검증 근거**: not_run, illustrative, calculated, observed. 도식은 illustrative, 모델 점수는 calculated, 실제 플레이 기록은 observed다.

숫자 0은 관측값 0이다. 모르는 값은 null/미정, 측정하지 않은 값은 미측정이다. 목표·가정·계산·실측을 구분하고 분모·단위·모델 버전·적용 범위를 붙인다. 계산 난도와 실제 성공률, 계산 재미 점수와 사람의 재미를 같은 지표로 합치지 않는다.

## workflow.json

```json
{
  "schema_version": 1,
  "project_id": "my-game",
  "updated_at": "2026-09-24",
  "stages": {
    "research": {
      "status": "pending",
      "input_sha256": {},
      "outputs": [],
      "notes": []
    },
    "concept": {"status":"pending","input_sha256":{},"outputs":[],"notes":[]},
    "systems": {"status":"pending","input_sha256":{},"outputs":[],"notes":[]},
    "progression": {"status":"pending","input_sha256":{},"outputs":[],"notes":[]},
    "validation": {"status":"pending","input_sha256":{},"outputs":[],"notes":[]},
    "html": {"status":"pending","input_sha256":{},"outputs":[],"notes":[]}
  },
  "decisions": [],
  "next_action": "사용자 자료와 기존 프로젝트의 기획 파일을 확인"
}
```

입력 해시의 키는 프로젝트 기획 경로 기준 상대 파일 경로, 값은 실제 바이트의 SHA-256이다. `workflow.json`은 실행 제어 메타데이터이므로 `input_sha256`에서 제외한다. 자신의 완료 기록 때문에 스스로 stale이 되는 순환을 만들지 않는다. 단계가 직접 갱신하는 문서를 다음 실행의 입력으로도 관리한다면 저장을 마친 최종 바이트의 해시를 사용한다. HTML은 표시한 선행 단계 상태를 `input_states` 객체에 기록하고 재개 때 비교한다(예: `{"research":"done","validation":"done"}`). 자신의 html running/done 전환은 콘텐츠 변경이 아니며 이 객체에 넣지 않는다. 결정 이력의 실질적인 규칙 변경은 반드시 해당 정본 문서에도 반영한다. 실제 입력 파일을 읽어 기록하며 예시 해시를 만들지 않는다. 단계 완료 시 소비한 파일 해시와 출력 경로를 기록한다. research가 brief를 동시에 작성하는 첫 실행에서는 브리프를 확정해 저장한 뒤 해시를 잡는다. 사용자가 수정하면 그 해시와 비교한다. 외부 웹페이지 전체를 동결할 필요는 없지만 접근일·해당 관찰을 보존한다.

결정 항목: `id`, `question`, `choice`, `basis_ids`, `status`(proposed/confirmed/deferred/superseded), `owner`(user/agent/source), `affected_ids`. 확인된 사용자 결정과 에이전트의 제안은 구분한다. 변경 이력을 덮어 지우기보다 이전 결정에 superseded를 표시한다.

### 완료 인계

모든 단계는 완료 후 다음을 반환한다: 출력 경로 / 반영한 결정 ID / 남은 가정·충돌 / 검수 결과 / 다음 단계에 필요한 입력. 총괄만 workflow.json을 수정한다. 독립 실행된 단계는 인계 요약을 반환하고 workflow 갱신은 해당 실행의 총괄 역할이 맡는다.

### 재개와 변경 영향

| 변경 입력 | 기본적으로 재검토할 단계 |
| --- | --- |
| 플랫폼·대상·핵심 재미·범위 | research → concept → systems → progression → validation → html |
| 조사 근거·해석 | concept 이후 중 실제로 해당 근거를 참조하는 단계 |
| 컨셉·루프·성공/실패 | systems → progression → validation → html |
| 시스템·상태·수치 | progression → validation → html |
| 진행 순서·배치·성장 | validation → html |
| 검증 결과 | 실패 가설을 소유한 concept/systems/progression과 그 하위 단계, html |
| 오탈자·표현만 변경 | 원문과 html. 의미가 그대로라는 판단을 notes에 기록 |
| HTML 색·간격만 변경 | html |

처음 재개할 때 done의 입력 해시와 출력 존재를 확인한다. HTML에 기록한 선행 `input_states`와 현재 상태가 다르면 표시 내용을 재검토한다. 해시가 없으면 검증되지 않은 기존 완료 상태로 보고 검토한다. 변경이 의미에 영향을 주는지 판단하고 영향 단계에 stale과 이유를 기록한다. 관계가 불명확하면 연결된 하위 단계를 보수적으로 재검토한다. 새 콘텐츠·정책·모델을 발견했다고 완료된 조사 전부를 기계적으로 다시 실행하지 않는다.
