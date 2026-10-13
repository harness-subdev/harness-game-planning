# 검증 기록

## v0.1.0 게시 범위

원작 보고서와 신작 기획의 계약·호출·인계, 실제 자료·영상·UI 조사, 캡처 없는 설명의 근거 상태, 내용 검수와 HTML 렌더러 선택 지침을 갱신했다. 7개 스킬 이름과 기존 Python 빌더 런타임을 유지했다. 세부 변경은 [CHANGELOG](CHANGELOG.md)에 남긴다.

## 실행 명령

저장소 루트에서 Python 3로 실행한다. 빌더는 표준 라이브러리만 사용한다.

```sh
python3 skills/front-game-planning-html/scripts/self_check.py
python3 skills/front-game-planning-html/scripts/build_portal.py portal.json index.html
```

스킬 구조는 Codex skill-creator의 `quick_validate.py`에 각 스킬 폴더를 전달하여 확인했다. 이 검증기는 저장소의 런타임 의존성이 아니다. 내부 상대 참조를 확인하며, 설치 루트의 보조 스킬 `mermaid-diagrams`와 `webapp-testing` 참조는 별도 설치 대상으로 구분한다.

## 이번 게시 작업에서 확인한 내용

- 7개 스킬의 frontmatter, 호출 메타데이터, 내부 상대 참조 검증.
- HTML 빌더: 가변 항목 수, 빈 상태, 상태·근거 표시, ID·링크 검증, HTML 이스케이프, 표 구조, 생성 실패 시 기존 출력 보존.
- 예시 `portal.json`의 형식 검증과 `index.html` 재생성; HTML이 현재 JSON의 빌드 결과와 일치하는지 대조.
- `VERSION`의 의미 버전과 README·CHANGELOG·포털 표시의 일치; `portal.json`의 입력 형식 버전은 정수 `1` 유지.
- README와 데모에서 신작 전용 설계 ID·단계 문서를 원작의 기본값으로 안내하지 않는지 대조.

위 로컬 검사는 원사이트 최신성, 실제 영상 관찰·캡처, Chrome 화면·상호작용 검수 또는 사람의 게임 재미 검증을 수행하지 않는다. 이전 게시본의 브라우저·독립 기획 시험 기록은 현재 수정본의 실행 증거로 사용하지 않는다. 이번 작업에서는 실제 영상·게임·Chrome 검수를 새로 실행하지 않았다.

제공 빌더 형식 `version: 1`은 텍스트·표·한 단계 상세·상태를 지원하며, 이미지·Mermaid·더 깊은 중첩을 지원하지 않는다. 원작 보고서는 HTML 스킬의 지원 가능한 렌더러 선택·보완 경로를 따른다. 이번 예시 HTML 생성은 원작 보고서의 실제 사진·그림 표시 지원을 입증하지 않는다.

개인 설치 경로, 원시 실행 기록, 임시 프로젝트는 배포 파일에 포함하지 않는다.

## 빌드·버전 운영

[VERSION](VERSION)의 `0.1.0`이 의미 버전 정본이고, 정확한 Git 커밋 SHA가 빌드 식별자다. [CHANGELOG](CHANGELOG.md)는 같은 버전의 변경 내용과 호환성·검증 한계를 기록한다. 배포한 내용은 해당 커밋의 `VERSION`과 변경 내역으로 확인한다.

다음 갱신은 `VERSION`과 해당 버전의 변경 내역을 수동으로 수정하고 README·포털의 표시 버전을 맞춘 뒤 위 두 명령을 실행해 함께 커밋한다. 실행마다 자동으로 버전을 증가시키지 않는다. 별도의 GitHub Actions, 자동 배포, 버전 증가 스크립트, 태그·GitHub 릴리스 발행 절차는 없다. 원격 push 성공과 CI 통과는 구별한다.
