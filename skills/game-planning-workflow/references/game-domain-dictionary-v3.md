<!-- game-domain-metadata
{
  "schema": "game-domain-dictionary-query/1",
  "outline_basis": "game-domain-v3-outline.md",
  "query": {
    "node_order": "document order",
    "children": "nodes whose parent equals the selected ID",
    "direct_range": "from this node anchor to the next node anchor, exclusive; last node to EOF",
    "default_scope": "selected node plus recursive children; never traverse references or parent",
    "rows": "key/value table data rows only; key is the actual first-cell term, qualified by node ID",
    "default_mode": "all",
    "modes": {
      "all": "all selected rows",
      "genre_names": "only genre_name_keys",
      "terms": "selected rows minus genre_name_keys"
    },
    "missing_genre_name_keys": [],
    "optional_scope": "direct: selected node only",
    "references": "separate opt-in links to direct ranges; never merge into default rows; follow original prose for relevant terms",
    "kinds": {
      "root": "전체 문서",
      "collection": "상위 사전",
      "genre": "장르",
      "subtype": "확정 하위 유형 절",
      "term_group": "장르 안 공통·기능 용어 묶음",
      "common": "장르 공용 용어 묶음",
      "reference": "번호형 출처"
    }
  },
  "nodes": {
    "dictionary": {"title": "게임 도메인 사전 V3", "parent": null, "kind": "root", "anchor": "gd-dictionary"},
    "1": {"title": "장르별 도메인 명칭 사전", "parent": "dictionary", "kind": "collection", "anchor": "gd-1"},
    "1.1": {"title": "액션", "parent": "1", "kind": "genre", "anchor": "gd-1-1", "genre_name_keys": ["액션(Action)"]},
    "1.1.1": {"title": "캐릭터 액션·핵앤슬래시", "parent": "1.1", "kind": "subtype", "anchor": "gd-1-1-1", "genre_name_keys": ["캐릭터 액션(Character action)", "핵앤슬래시(Hack and slash, 액션)"]},
    "1.1.2": {"title": "비트엠업·벨트스크롤", "parent": "1.1", "kind": "subtype", "anchor": "gd-1-1-2", "genre_name_keys": ["비트엠업(Beat ’em up, Brawler)", "벨트스크롤(Belt-scroll beat ’em up)", "싱글플레인 비트엠업(Single-plane beat ’em up)", "3D 비트엠업(3D beat ’em up)"]},
    "1.2": {"title": "슈팅", "parent": "1", "kind": "genre", "anchor": "gd-1-2", "genre_name_keys": ["슈팅(Shooter)"]},
    "1.2.1": {"title": "FPS", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-1", "genre_name_keys": ["FPS(First-person shooter)"]},
    "1.2.2": {"title": "TPS", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-2", "genre_name_keys": ["TPS(Third-person shooter)"]},
    "1.2.3": {"title": "전술 슈터", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-3", "genre_name_keys": ["전술 슈터(Tactical shooter)"]},
    "1.2.4": {"title": "아레나 슈터", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-4", "genre_name_keys": ["아레나 슈터(Arena shooter)", "아레나 FPS(Arena FPS)"], "references": ["1.2.1"]},
    "1.2.5": {"title": "히어로 슈터", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-5", "genre_name_keys": ["히어로 슈터(Hero shooter)"]},
    "1.2.6": {"title": "루터 슈터", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-6", "genre_name_keys": ["루터 슈터(Looter shooter)"], "references": ["2.5"]},
    "1.2.7": {"title": "런앤건", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-7", "genre_name_keys": ["런앤건(Run and gun, 장르)", "플랫폼 슈터(Platform shooter)"], "references": ["1.2.1", "1.4"]},
    "1.2.8": {"title": "레일 슈터", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-8", "genre_name_keys": ["레일 슈터(Rail shooter)"]},
    "1.2.9": {"title": "슛뎀업·고정 화면·스크롤", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-9", "genre_name_keys": ["슛뎀업(Shoot ’em up, Shmup)", "고정 화면 슈터(Fixed shooter)", "스크롤 슈터(Scrolling shooter)"], "references": ["1.2.10", "1.2.1"]},
    "1.2.10": {"title": "탄막", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-10", "genre_name_keys": ["탄막 슈팅(Bullet hell, Danmaku)"]},
    "1.2.11": {"title": "트윈스틱", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-11", "genre_name_keys": ["트윈스틱 슈터(Twin-stick shooter)"]},
    "1.2.12": {"title": "부머 슈터", "parent": "1.2", "kind": "subtype", "anchor": "gd-1-2-12", "genre_name_keys": ["부머 슈터(Boomer shooter)", "레트로 FPS(Retro FPS)"], "references": ["1.2.1"]},
    "1.3": {"title": "격투", "parent": "1", "kind": "genre", "anchor": "gd-1-3", "genre_name_keys": ["격투(Fighting game)"], "references": ["2.10", "1.1"]},
    "1.3.1": {"title": "2D 대전", "parent": "1.3", "kind": "subtype", "anchor": "gd-1-3-1", "genre_name_keys": ["2D 대전 격투(2D fighter)"]},
    "1.3.2": {"title": "3D 대전", "parent": "1.3", "kind": "subtype", "anchor": "gd-1-3-2", "genre_name_keys": ["3D 대전 격투(3D fighter)"]},
    "1.3.3": {"title": "태그팀", "parent": "1.3", "kind": "subtype", "anchor": "gd-1-3-3", "genre_name_keys": ["태그팀 격투(Tag-team fighter)"]},
    "1.3.4": {"title": "플랫폼 격투", "parent": "1.3", "kind": "subtype", "anchor": "gd-1-3-4", "genre_name_keys": ["플랫폼 격투(Platform fighter)"]},
    "1.4": {"title": "플랫폼", "parent": "1", "kind": "genre", "anchor": "gd-1-4", "genre_name_keys": ["플랫폼(Platformer)"]},
    "1.4.1": {"title": "2D·3D 플랫폼", "parent": "1.4", "kind": "subtype", "anchor": "gd-1-4-1", "genre_name_keys": ["2D 플랫폼(2D platformer)", "2.5D 플랫폼(2.5D platformer)", "3D 플랫폼(3D platformer)"], "references": ["1.4"]},
    "1.4.2": {"title": "퍼즐 플랫폼", "parent": "1.4", "kind": "subtype", "anchor": "gd-1-4-2", "genre_name_keys": ["퍼즐 플랫폼(Puzzle-platformer)"]},
    "1.4.3": {"title": "수집형 플랫폼", "parent": "1.4", "kind": "subtype", "anchor": "gd-1-4-3", "genre_name_keys": ["수집형 플랫폼(Collect-a-thon)"]},
    "1.4.4": {"title": "러너", "parent": "1.4", "kind": "subtype", "anchor": "gd-1-4-4", "genre_name_keys": ["러너(Runner)"]},
    "1.5": {"title": "잠입", "parent": "1", "kind": "genre", "anchor": "gd-1-5", "genre_name_keys": ["잠입(Stealth)"]},
    "1.5.1": {"title": "액션 잠입·샌드박스 잠입", "parent": "1.5", "kind": "subtype", "anchor": "gd-1-5-1", "genre_name_keys": ["액션 잠입(Action stealth)", "샌드박스 잠입(Sandbox stealth)"]},
    "1.6": {"title": "어드벤처·탐색", "parent": "1", "kind": "genre", "anchor": "gd-1-6", "genre_name_keys": ["어드벤처(Adventure)"]},
    "1.6.1": {"title": "포인트앤클릭", "parent": "1.6", "kind": "subtype", "anchor": "gd-1-6-1", "genre_name_keys": ["포인트앤클릭 어드벤처(Point-and-click adventure)"]},
    "1.6.2": {"title": "퍼즐 어드벤처", "parent": "1.6", "kind": "subtype", "anchor": "gd-1-6-2", "genre_name_keys": ["퍼즐 어드벤처(Puzzle adventure)"]},
    "1.6.3": {"title": "워킹 시뮬레이터", "parent": "1.6", "kind": "subtype", "anchor": "gd-1-6-3", "genre_name_keys": ["워킹 시뮬레이터(Walking simulator)"]},
    "1.7": {"title": "서사·인터랙티브 픽션", "parent": "1", "kind": "genre", "anchor": "gd-1-7", "genre_name_keys": ["인터랙티브 픽션(Interactive fiction, IF)"]},
    "1.7.1": {"title": "텍스트 어드벤처", "parent": "1.7", "kind": "subtype", "anchor": "gd-1-7-1", "genre_name_keys": ["텍스트 어드벤처(Text adventure)"]},
    "1.7.2": {"title": "선택형 이야기", "parent": "1.7", "kind": "subtype", "anchor": "gd-1-7-2", "genre_name_keys": ["선택형 이야기(Choice-based narrative)"]},
    "1.7.3": {"title": "비주얼노벨·오토메", "parent": "1.7", "kind": "subtype", "anchor": "gd-1-7-3", "genre_name_keys": ["비주얼노벨(Visual novel)", "키네틱 노벨(Kinetic novel)", "오토메(Otome)"]},
    "1.8": {"title": "퍼즐", "parent": "1", "kind": "genre", "anchor": "gd-1-8", "genre_name_keys": ["퍼즐(Puzzle game)"]},
    "1.8.1": {"title": "논리·공간 퍼즐", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-1", "genre_name_keys": ["논리 퍼즐(Logic puzzle)", "공간 퍼즐(Spatial puzzle)"], "references": ["2.3", "2.8", "1.8.5"]},
    "1.8.2": {"title": "물리 퍼즐", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-2", "genre_name_keys": ["물리 퍼즐(Physics puzzle)"]},
    "1.8.3": {"title": "매치3·블라스트", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-3", "genre_name_keys": ["타일 매칭(Tile-matching)", "매치3(Match-three)", "블라스트(Blast, Collapse-style puzzle)"]},
    "1.8.4": {"title": "블록·발사형 매칭", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-4", "genre_name_keys": ["낙하 블록 퍼즐(Falling-block puzzle)", "발사형 매칭(Shooting tile-matching)", "버블슈터(Bubble shooter)"]},
    "1.8.5": {"title": "소코반", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-5", "genre_name_keys": ["소코반(Sokoban, Box-pushing puzzle)"]},
    "1.8.6": {"title": "숨은그림찾기·탈출", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-6", "genre_name_keys": ["숨은그림찾기(Hidden object game)", "탈출 퍼즐(Escape-room game)"]},
    "1.8.7": {"title": "프로그래밍 퍼즐", "parent": "1.8", "kind": "subtype", "anchor": "gd-1-8-7", "genre_name_keys": ["프로그래밍 퍼즐(Programming puzzle)"]},
    "1.9": {"title": "단어·퀴즈", "parent": "1", "kind": "genre", "anchor": "gd-1-9", "genre_name_keys": ["단어게임(Word game)", "퀴즈(Quiz game)"]},
    "1.9.1": {"title": "낱말·타자·상식", "parent": "1.9", "kind": "subtype", "anchor": "gd-1-9-1", "genre_name_keys": ["문자 배열 게임(Letter arrangement game)", "크로스워드(Crossword)", "타자게임(Typing game)", "상식 퀴즈(Trivia)"], "references": ["2.2", "2.3", "2.8", "2.4"]},
    "1.10": {"title": "RPG", "parent": "1", "kind": "genre", "anchor": "gd-1-10", "genre_name_keys": ["RPG(Role-Playing Game)"]},
    "1.10.1": {"title": "액션 RPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-1", "genre_name_keys": ["액션 RPG(Action RPG, ARPG)"], "references": ["1.10", "2.10"]},
    "1.10.2": {"title": "턴제 RPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-2", "genre_name_keys": ["턴제 RPG(Turn-Based RPG)"]},
    "1.10.3": {"title": "전술 RPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-3", "genre_name_keys": ["전술 RPG(Tactical RPG)"]},
    "1.10.4": {"title": "파티 기반 RPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-4", "genre_name_keys": ["파티 기반 RPG(Party-Based RPG)"]},
    "1.10.5": {"title": "던전크롤러", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-5", "genre_name_keys": ["던전크롤러(Dungeon Crawler)"]},
    "1.10.6": {"title": "방치 RPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-6", "genre_name_keys": ["방치 RPG(Idle RPG)"]},
    "1.10.7": {"title": "MMORPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-7", "genre_name_keys": ["MMORPG"]},
    "1.10.8": {"title": "JRPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-8", "genre_name_keys": ["JRPG(Japanese RPG)"]},
    "1.10.9": {"title": "CRPG", "parent": "1.10", "kind": "subtype", "anchor": "gd-1-10-9", "genre_name_keys": ["CRPG(Computer RPG)"]},
    "1.11": {"title": "전략·전술", "parent": "1", "kind": "genre", "anchor": "gd-1-11", "genre_name_keys": ["전략 게임(Strategy Game)", "4X 전략"], "references": ["1.11.1", "1.13.1", "2.5", "2.10"]},
    "1.11.1": {"title": "실시간 전략(RTS)", "parent": "1.11", "kind": "subtype", "anchor": "gd-1-11-1", "genre_name_keys": ["RTS(Real-Time Strategy)"]},
    "1.11.2": {"title": "기지 건설 전투(Build & Battle)", "parent": "1.11", "kind": "subtype", "anchor": "gd-1-11-2", "genre_name_keys": ["Build & Battle"]},
    "1.12": {"title": "시뮬레이션", "parent": "1", "kind": "genre", "anchor": "gd-1-12", "genre_name_keys": ["시뮬레이션 게임"]},
    "1.12.1": {"title": "생활 시뮬레이션", "parent": "1.12", "kind": "subtype", "anchor": "gd-1-12-1", "genre_name_keys": ["생활 시뮬레이션(Life Simulation)"]},
    "1.12.2": {"title": "농업·동물돌봄·번식", "parent": "1.12", "kind": "subtype", "anchor": "gd-1-12-2", "genre_name_keys": ["농업 시뮬레이션(Farming Simulation)", "동물돌봄 게임", "번식 게임(Breeding Game)"]},
    "1.12.3": {"title": "갓 게임", "parent": "1.12", "kind": "subtype", "anchor": "gd-1-12-3", "genre_name_keys": ["갓 게임(God Game)"]},
    "1.13": {"title": "건설·경영·자동화", "parent": "1", "kind": "genre", "anchor": "gd-1-13", "genre_name_keys": ["건설·경영 게임", "타이쿤(Tycoon)"]},
    "1.13.1": {"title": "공장·생산·물류 자동화", "parent": "1.13", "kind": "subtype", "anchor": "gd-1-13-1", "genre_name_keys": ["공장 자동화 게임(Factory Automation)"]},
    "1.13.2": {"title": "시간관리", "parent": "1.13", "kind": "subtype", "anchor": "gd-1-13-2", "genre_name_keys": ["시간관리 게임(Time Management)"], "references": ["2.2", "2.3", "1.13.1"]},
    "1.13.3": {"title": "스포츠매니저", "parent": "1.13", "kind": "subtype", "anchor": "gd-1-13-3", "genre_name_keys": ["스포츠매니저(Sports Management)"]},
    "1.14": {"title": "스포츠·운동", "parent": "1", "kind": "genre", "anchor": "gd-1-14", "genre_name_keys": ["스포츠 게임(Sports Game)", "아케이드 스포츠(Arcade Sports)", "스포츠 시뮬레이션(Realistic Sports)"]},
    "1.14.1": {"title": "농구 규칙을 사용하는 팀 스포츠", "parent": "1.14", "kind": "subtype", "anchor": "gd-1-14-1", "genre_name_keys": ["팀 스포츠 게임"]},
    "1.15": {"title": "레이싱", "parent": "1", "kind": "genre", "anchor": "gd-1-15", "genre_name_keys": ["레이싱(Racing)", "아케이드 레이싱", "시뮬레이션 레이싱(Sim Racing)"]},
    "1.15.terms": {"title": "공통 용어: 주행·레이스·정비", "parent": "1.15", "kind": "term_group", "anchor": "gd-1-15-terms"},
    "1.16": {"title": "음악·리듬", "parent": "1", "kind": "genre", "anchor": "gd-1-16", "genre_name_keys": ["음악·리듬 게임"]},
    "1.16.1": {"title": "노트 판정형 리듬", "parent": "1.16", "kind": "subtype", "anchor": "gd-1-16-1", "genre_name_keys": ["노트 판정형 리듬 게임"]},
    "1.16.terms": {"title": "기능 용어: 음악 기반 생성·편집", "parent": "1.16", "kind": "term_group", "anchor": "gd-1-16-terms"},
    "1.17": {"title": "카드·덱", "parent": "1", "kind": "genre", "anchor": "gd-1-17", "genre_name_keys": ["카드 게임(Card Game)"]},
    "1.17.1": {"title": "카드배틀러·수집카드", "parent": "1.17", "kind": "subtype", "anchor": "gd-1-17-1", "genre_name_keys": ["카드배틀러(Card Battler)", "수집카드 게임(TCG)"]},
    "1.17.2": {"title": "덱빌딩 게임", "parent": "1.17", "kind": "subtype", "anchor": "gd-1-17-2", "genre_name_keys": ["덱빌딩 게임(Deck-Building Game)"], "references": ["1.17", "1.17.1"]},
    "1.17.3": {"title": "솔리테어", "parent": "1.17", "kind": "subtype", "anchor": "gd-1-17-3", "genre_name_keys": ["솔리테어(Solitaire, Patience)"]},
    "1.18": {"title": "보드·테이블탑", "parent": "1", "kind": "genre", "anchor": "gd-1-18", "genre_name_keys": ["보드게임(Board Game)", "테이블탑(Tabletop)"]},
    "1.18.1": {"title": "체스", "parent": "1.18", "kind": "subtype", "anchor": "gd-1-18-1", "genre_name_keys": ["체스(Chess)"]},
    "1.18.2": {"title": "테이블탑 RPG", "parent": "1.18", "kind": "subtype", "anchor": "gd-1-18-2", "genre_name_keys": ["테이블탑 RPG(TRPG, TTRPG)"]},
    "1.19": {"title": "파티·사회적추론", "parent": "1", "kind": "genre", "anchor": "gd-1-19", "genre_name_keys": ["파티 게임(Party Game)"]},
    "1.19.1": {"title": "숨은 역할·사회적추론", "parent": "1.19", "kind": "subtype", "anchor": "gd-1-19-1", "genre_name_keys": ["숨은 역할 게임(Hidden Role)", "사회적추론(Social Deduction)"]},
    "1.19.2": {"title": "그림·추측 파티", "parent": "1.19", "kind": "subtype", "anchor": "gd-1-19-2", "genre_name_keys": ["그림 추측 게임(Drawing Game)"]},
    "1.20": {"title": "샌드박스·창작", "parent": "1", "kind": "genre", "anchor": "gd-1-20", "genre_name_keys": ["샌드박스(Sandbox)", "물리 샌드박스(디지털)"], "references": ["2.13"]},
    "1.21": {"title": "방치·증분", "parent": "1", "kind": "genre", "anchor": "gd-1-21", "genre_name_keys": ["방치 게임(Idle Game, Idler)", "증분 게임(Incremental Game)"]},
    "1.21.1": {"title": "클리커", "parent": "1.21", "kind": "subtype", "anchor": "gd-1-21-1", "genre_name_keys": ["클리커(Clicker)"]},
    "1.21.terms": {"title": "공통 용어: 생산기·생산량·프레스티지", "parent": "1.21", "kind": "term_group", "anchor": "gd-1-21-terms"},
    "1.22": {"title": "카지노형 플레이", "parent": "1", "kind": "genre", "anchor": "gd-1-22", "genre_name_keys": ["카지노형 플레이", "소셜카지노(Social Casino)"]},
    "1.22.1": {"title": "슬롯", "parent": "1.22", "kind": "subtype", "anchor": "gd-1-22-1", "genre_name_keys": ["슬롯(Slots)"]},
    "1.22.2": {"title": "포커", "parent": "1.22", "kind": "subtype", "anchor": "gd-1-22-2", "genre_name_keys": ["포커(Poker)", "드로 포커(Draw Poker)", "스터드 포커(Stud Poker)"]},
    "1.22.3": {"title": "블랙잭", "parent": "1.22", "kind": "subtype", "anchor": "gd-1-22-3", "genre_name_keys": ["블랙잭(Blackjack)"]},
    "1.23": {"title": "로그 계열", "parent": "1", "kind": "genre", "anchor": "gd-1-23", "genre_name_keys": ["로그 계열(Roguelike family)"]},
    "1.23.1": {"title": "전통 로그라이크", "parent": "1.23", "kind": "subtype", "anchor": "gd-1-23-1", "genre_name_keys": ["전통 로그라이크(Traditional roguelike)"], "references": ["2.6"]},
    "1.23.2": {"title": "로그라이트·액션 로그라이크", "parent": "1.23", "kind": "subtype", "anchor": "gd-1-23-2", "genre_name_keys": ["로그라이트(Roguelite)", "액션 로그라이크(Action roguelike)"], "references": ["2.6"]},
    "1.23.3": {"title": "로그라이크 덱빌더", "parent": "1.23", "kind": "subtype", "anchor": "gd-1-23-3", "genre_name_keys": ["로그라이크 덱빌더(Roguelike deckbuilder)"]},
    "1.24": {"title": "소울라이크", "parent": "1", "kind": "genre", "anchor": "gd-1-24", "genre_name_keys": ["소울라이크(Soulslike)"]},
    "1.25": {"title": "메트로배니아", "parent": "1", "kind": "genre", "anchor": "gd-1-25", "genre_name_keys": ["메트로배니아(Metroidvania)"]},
    "1.25.1": {"title": "2D·3D 메트로배니아", "parent": "1.25", "kind": "subtype", "anchor": "gd-1-25-1", "genre_name_keys": ["2D 메트로배니아(2D Metroidvania)", "3D 메트로배니아(3D Metroidvania)"], "references": ["1.25", "1.4"]},
    "1.25.2": {"title": "로그바니아·지식 기반 탐색", "parent": "1.25", "kind": "subtype", "anchor": "gd-1-25-2", "genre_name_keys": ["로그바니아(RogueVania)", "메트로브레이니아(Metroidbrainia)"]},
    "1.26": {"title": "생존", "parent": "1", "kind": "genre", "anchor": "gd-1-26", "genre_name_keys": ["생존(Survival)"], "references": ["2.10"]},
    "1.26.1": {"title": "생존제작·오픈월드 생존제작", "parent": "1.26", "kind": "subtype", "anchor": "gd-1-26-1", "genre_name_keys": ["생존제작(Survival crafting)", "오픈월드 생존제작(Open-world survival crafting)"]},
    "1.27": {"title": "공포", "parent": "1", "kind": "genre", "anchor": "gd-1-27", "genre_name_keys": ["공포(Horror game)"]},
    "1.27.1": {"title": "생존공포", "parent": "1.27", "kind": "subtype", "anchor": "gd-1-27-1", "genre_name_keys": ["생존공포(Survival horror)"]},
    "1.27.2": {"title": "심리공포", "parent": "1.27", "kind": "subtype", "anchor": "gd-1-27-2", "genre_name_keys": ["심리공포(Psychological horror)"], "references": ["2.8", "1.6.3"]},
    "1.27.3": {"title": "액션공포·점프스케어", "parent": "1.27", "kind": "subtype", "anchor": "gd-1-27-3", "genre_name_keys": ["액션공포(Action horror)", "역공포(Reverse horror)"]},
    "1.28": {"title": "배틀로얄", "parent": "1", "kind": "genre", "anchor": "gd-1-28", "genre_name_keys": ["배틀로얄(Battle royale)"]},
    "1.29": {"title": "익스트랙션·추출형", "parent": "1", "kind": "genre", "anchor": "gd-1-29", "genre_name_keys": ["추출형 슈터(Extraction shooter)"]},
    "1.30": {"title": "MOBA", "parent": "1", "kind": "genre", "anchor": "gd-1-30", "genre_name_keys": ["MOBA(Multiplayer Online Battle Arena)"]},
    "1.31": {"title": "오토배틀러", "parent": "1", "kind": "genre", "anchor": "gd-1-31", "genre_name_keys": ["오토배틀러(Auto Battler)"]},
    "1.32": {"title": "몰입형 시뮬레이션", "parent": "1", "kind": "genre", "anchor": "gd-1-32", "genre_name_keys": ["몰입형 시뮬레이션(Immersive Sim)"]},
    "2": {"title": "장르 공용 명칭 사전", "parent": "dictionary", "kind": "collection", "anchor": "gd-2"},
    "2.1": {"title": "기본 개념", "parent": "2", "kind": "common", "anchor": "gd-2-1"},
    "2.2": {"title": "주체·대상·행동", "parent": "2", "kind": "common", "anchor": "gd-2-2"},
    "2.3": {"title": "상태·조건·판정", "parent": "2", "kind": "common", "anchor": "gd-2-3"},
    "2.4": {"title": "목표·결과·보상", "parent": "2", "kind": "common", "anchor": "gd-2-4"},
    "2.5": {"title": "자원·보유·경제", "parent": "2", "kind": "common", "anchor": "gd-2-5"},
    "2.6": {"title": "시간·진행·성장", "parent": "2", "kind": "common", "anchor": "gd-2-6"},
    "2.7": {"title": "공간·시점·모드", "parent": "2", "kind": "common", "anchor": "gd-2-7"},
    "2.8": {"title": "정보·확률", "parent": "2", "kind": "common", "anchor": "gd-2-8"},
    "2.9": {"title": "인터페이스·피드백", "parent": "2", "kind": "common", "anchor": "gd-2-9"},
    "2.10": {"title": "공통 시스템", "parent": "2", "kind": "common", "anchor": "gd-2-10"},
    "2.11": {"title": "참여·접속·사회적 기능", "parent": "2", "kind": "common", "anchor": "gd-2-11"},
    "2.12": {"title": "시장·플레이어·경험 명칭", "parent": "2", "kind": "common", "anchor": "gd-2-12"},
    "2.13": {"title": "제작·유통·운영·매체", "parent": "2", "kind": "common", "anchor": "gd-2-13"},
    "2.14": {"title": "목적·소재·대상·지역 표현", "parent": "2", "kind": "common", "anchor": "gd-2-14"},
    "3": {"title": "레퍼런스", "parent": "dictionary", "kind": "reference", "anchor": "gd-3"}
  }
}
-->

<a id="gd-dictionary"></a>
# 게임 도메인 사전 V3

> 에이전트 조회: 원문의 `game-domain-metadata` 주석을 먼저 읽고, 선택한 장르·하위 유형의 앵커 범위만 조회하세요. 장르 이름은 `genre_names`, 전문어는 `terms`로 구별하며, `references`는 요청할 때만 별도로 확인하세요.

## 목차

장르·하위 유형은 선택한 절과 그 하위 범위만 조회합니다. 공통·기능 용어 묶음과 공용·다른 절의 참조는 구별합니다.

- [1 장르별 도메인 명칭 사전](#gd-1)
  - [1.1 액션](#gd-1-1)
    - [1.1.1 캐릭터 액션·핵앤슬래시](#gd-1-1-1)
    - [1.1.2 비트엠업·벨트스크롤](#gd-1-1-2)
  - [1.2 슈팅](#gd-1-2)
    - [1.2.1 FPS](#gd-1-2-1)
    - [1.2.2 TPS](#gd-1-2-2)
    - [1.2.3 전술 슈터](#gd-1-2-3)
    - [1.2.4 아레나 슈터](#gd-1-2-4)
    - [1.2.5 히어로 슈터](#gd-1-2-5)
    - [1.2.6 루터 슈터](#gd-1-2-6)
    - [1.2.7 런앤건](#gd-1-2-7)
    - [1.2.8 레일 슈터](#gd-1-2-8)
    - [1.2.9 슛뎀업·고정 화면·스크롤](#gd-1-2-9)
    - [1.2.10 탄막](#gd-1-2-10)
    - [1.2.11 트윈스틱](#gd-1-2-11)
    - [1.2.12 부머 슈터](#gd-1-2-12)
  - [1.3 격투](#gd-1-3)
    - [1.3.1 2D 대전](#gd-1-3-1)
    - [1.3.2 3D 대전](#gd-1-3-2)
    - [1.3.3 태그팀](#gd-1-3-3)
    - [1.3.4 플랫폼 격투](#gd-1-3-4)
  - [1.4 플랫폼](#gd-1-4)
    - [1.4.1 2D·3D 플랫폼](#gd-1-4-1)
    - [1.4.2 퍼즐 플랫폼](#gd-1-4-2)
    - [1.4.3 수집형 플랫폼](#gd-1-4-3)
    - [1.4.4 러너](#gd-1-4-4)
  - [1.5 잠입](#gd-1-5)
    - [1.5.1 액션 잠입·샌드박스 잠입](#gd-1-5-1)
  - [1.6 어드벤처·탐색](#gd-1-6)
    - [1.6.1 포인트앤클릭](#gd-1-6-1)
    - [1.6.2 퍼즐 어드벤처](#gd-1-6-2)
    - [1.6.3 워킹 시뮬레이터](#gd-1-6-3)
  - [1.7 서사·인터랙티브 픽션](#gd-1-7)
    - [1.7.1 텍스트 어드벤처](#gd-1-7-1)
    - [1.7.2 선택형 이야기](#gd-1-7-2)
    - [1.7.3 비주얼노벨·오토메](#gd-1-7-3)
  - [1.8 퍼즐](#gd-1-8)
    - [1.8.1 논리·공간 퍼즐](#gd-1-8-1)
    - [1.8.2 물리 퍼즐](#gd-1-8-2)
    - [1.8.3 매치3·블라스트](#gd-1-8-3)
    - [1.8.4 블록·발사형 매칭](#gd-1-8-4)
    - [1.8.5 소코반](#gd-1-8-5)
    - [1.8.6 숨은그림찾기·탈출](#gd-1-8-6)
    - [1.8.7 프로그래밍 퍼즐](#gd-1-8-7)
  - [1.9 단어·퀴즈](#gd-1-9)
    - [1.9.1 낱말·타자·상식](#gd-1-9-1)
  - [1.10 RPG](#gd-1-10)
    - [1.10.1 액션 RPG](#gd-1-10-1)
    - [1.10.2 턴제 RPG](#gd-1-10-2)
    - [1.10.3 전술 RPG](#gd-1-10-3)
    - [1.10.4 파티 기반 RPG](#gd-1-10-4)
    - [1.10.5 던전크롤러](#gd-1-10-5)
    - [1.10.6 방치 RPG](#gd-1-10-6)
    - [1.10.7 MMORPG](#gd-1-10-7)
    - [1.10.8 JRPG](#gd-1-10-8)
    - [1.10.9 CRPG](#gd-1-10-9)
  - [1.11 전략·전술](#gd-1-11)
    - [1.11.1 실시간 전략(RTS)](#gd-1-11-1)
    - [1.11.2 기지 건설 전투(Build & Battle)](#gd-1-11-2)
  - [1.12 시뮬레이션](#gd-1-12)
    - [1.12.1 생활 시뮬레이션](#gd-1-12-1)
    - [1.12.2 농업·동물돌봄·번식](#gd-1-12-2)
    - [1.12.3 갓 게임](#gd-1-12-3)
  - [1.13 건설·경영·자동화](#gd-1-13)
    - [1.13.1 공장·생산·물류 자동화](#gd-1-13-1)
    - [1.13.2 시간관리](#gd-1-13-2)
    - [1.13.3 스포츠매니저](#gd-1-13-3)
  - [1.14 스포츠·운동](#gd-1-14)
    - [1.14.1 농구 규칙을 사용하는 팀 스포츠](#gd-1-14-1)
  - [1.15 레이싱](#gd-1-15)
    - [공통 용어: 주행·레이스·정비](#gd-1-15-terms)
  - [1.16 음악·리듬](#gd-1-16)
    - [1.16.1 노트 판정형 리듬](#gd-1-16-1)
    - [기능 용어: 음악 기반 생성·편집](#gd-1-16-terms)
  - [1.17 카드·덱](#gd-1-17)
    - [1.17.1 카드배틀러·수집카드](#gd-1-17-1)
    - [1.17.2 덱빌딩 게임](#gd-1-17-2)
    - [1.17.3 솔리테어](#gd-1-17-3)
  - [1.18 보드·테이블탑](#gd-1-18)
    - [1.18.1 체스](#gd-1-18-1)
    - [1.18.2 테이블탑 RPG](#gd-1-18-2)
  - [1.19 파티·사회적추론](#gd-1-19)
    - [1.19.1 숨은 역할·사회적추론](#gd-1-19-1)
    - [1.19.2 그림·추측 파티](#gd-1-19-2)
  - [1.20 샌드박스·창작](#gd-1-20)
  - [1.21 방치·증분](#gd-1-21)
    - [1.21.1 클리커](#gd-1-21-1)
    - [공통 용어: 생산기·생산량·프레스티지](#gd-1-21-terms)
  - [1.22 카지노형 플레이](#gd-1-22)
    - [1.22.1 슬롯](#gd-1-22-1)
    - [1.22.2 포커](#gd-1-22-2)
    - [1.22.3 블랙잭](#gd-1-22-3)
  - [1.23 로그 계열](#gd-1-23)
    - [1.23.1 전통 로그라이크](#gd-1-23-1)
    - [1.23.2 로그라이트·액션 로그라이크](#gd-1-23-2)
    - [1.23.3 로그라이크 덱빌더](#gd-1-23-3)
  - [1.24 소울라이크](#gd-1-24)
  - [1.25 메트로배니아](#gd-1-25)
    - [1.25.1 2D·3D 메트로배니아](#gd-1-25-1)
    - [1.25.2 로그바니아·지식 기반 탐색](#gd-1-25-2)
  - [1.26 생존](#gd-1-26)
    - [1.26.1 생존제작·오픈월드 생존제작](#gd-1-26-1)
  - [1.27 공포](#gd-1-27)
    - [1.27.1 생존공포](#gd-1-27-1)
    - [1.27.2 심리공포](#gd-1-27-2)
    - [1.27.3 액션공포·점프스케어](#gd-1-27-3)
  - [1.28 배틀로얄](#gd-1-28)
  - [1.29 익스트랙션·추출형](#gd-1-29)
  - [1.30 MOBA](#gd-1-30)
  - [1.31 오토배틀러](#gd-1-31)
  - [1.32 몰입형 시뮬레이션](#gd-1-32)
- [2 장르 공용 명칭 사전](#gd-2)
  - [2.1 기본 개념](#gd-2-1)
  - [2.2 주체·대상·행동](#gd-2-2)
  - [2.3 상태·조건·판정](#gd-2-3)
  - [2.4 목표·결과·보상](#gd-2-4)
  - [2.5 자원·보유·경제](#gd-2-5)
  - [2.6 시간·진행·성장](#gd-2-6)
  - [2.7 공간·시점·모드](#gd-2-7)
  - [2.8 정보·확률](#gd-2-8)
  - [2.9 인터페이스·피드백](#gd-2-9)
  - [2.10 공통 시스템](#gd-2-10)
  - [2.11 참여·접속·사회적 기능](#gd-2-11)
  - [2.12 시장·플레이어·경험 명칭](#gd-2-12)
  - [2.13 제작·유통·운영·매체](#gd-2-13)
  - [2.14 목적·소재·대상·지역 표현](#gd-2-14)
- [3 레퍼런스](#gd-3)

<a id="gd-1"></a>
## 1. 장르별 도메인 명칭 사전

<a id="gd-1-1"></a>
### 1.1 액션

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 액션(Action) | 실시간 입력과 움직임·공격의 타이밍으로 과제를 해결하는 장르군. | 판단 내용뿐 아니라 입력 실행의 시점과 위치가 결과에 직접 작용한다. | 공격 범위를 벗어난 뒤 빈틈에 접근하는 액션을 중심으로 설계한다. | — | [1], [2], [3] |

<a id="gd-1-1-1"></a>
#### 1.1.1 캐릭터 액션·핵앤슬래시

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 캐릭터 액션(Character action) | 캐릭터의 근접 기술과 공격 연계를 중심으로 하는 액션 유형. | 조준 사격보다 캐릭터 기술의 연결과 조작이 전투의 중심이다. | 무기를 바꾸며 근접 기술을 이어 가는 캐릭터 액션으로 구성한다. | [1]: 3D 핵앤슬래시를 가리키는 용례; 모든 캐릭터 등장 액션의 이름으로 쓰지 않는다. | [1] |
| 핵앤슬래시(Hack and slash, 액션) | 칼 등 근접 무기로 다수의 적과 싸우는 전투 중심 유형. | 액션 의미에서는 근접 무기 전투를 한정한다. | 근접 무기를 바꾸며 적 집단을 돌파하는 핵앤슬래시 구간을 둔다. | [1]: 무기 중심 액션; [4]: 로그라이크에서 많은 몬스터를 처치하는 성질. | [1], [4] |
| 공격 연계(Attack chain) | 정해진 연결 조건에 따라 다음 공격으로 이어지는 기술 구성. | 연계는 입력 구조이며 모든 후속타가 확정 적중하는 콤보와 같지 않다. | 약공격 이후 강공격으로 이어지는 공격 연계를 제공한다. | 격투의 체인·콤보는 1.3 참조. | [1], [5] |
| 점프 공격(Jumping attack) | 도약 또는 공중 상태에서 수행하는 공격. | 지상 공격과 실행 위치·접근 경로를 구별한다. | 적의 앞줄을 넘는 점프 공격으로 후열에 접근한다. | — | [1] |
| 잡기 공격(Grappling attack) | 가까운 상대를 붙잡아 타격하거나 던지는 공격. | 무기를 휘둘러 적중시키는 공격과 구별한다. | 근접한 적을 붙잡아 뒤쪽으로 던지는 잡기 공격을 둔다. | 격투의 잡기 해제·커맨드 잡기는 1.3 참조. | [1] |

<a id="gd-1-1-2"></a>
#### 1.1.2 비트엠업·벨트스크롤

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 비트엠업(Beat ’em up, Brawler) | 다수의 적을 근접전으로 상대하며 구간을 진행하는 액션 유형. | 전형적인 대전 격투의 한 상대와 경기하는 구조와 구별한다. | 현재 적 집단을 모두 쓰러뜨리면 다음 구간으로 이동할 수 있다. | [1]: brawler는 별칭; 과거 영국 매체는 beat ’em up을 대전 격투까지 넓게 사용했다. | [1] |
| 벨트스크롤(Belt-scroll beat ’em up) | 횡스크롤 전장 안에서 가로 방향과 화면 깊이를 나타내는 세로 방향으로 이동하는 비트엠업. | 한 가로 이동선만 쓰는 싱글플레인 유형과 구별한다. | 세로 위치를 맞춘 뒤 적에게 접근하는 벨트스크롤 전투를 둔다. | [1]: 일본에서 나온 화면 진행 형식 명칭; beat ’em up 전체의 동의어는 아니다. | [1] |
| 싱글플레인 비트엠업(Single-plane beat ’em up) | 한 횡스크롤 이동면에서 다수의 적을 상대하는 비트엠업. | 전장 깊이 방향으로 자유롭게 이동하는 벨트스크롤과 구별한다. | 적과 같은 이동선에서 타격 거리를 조절한다. | — | [1] |
| 3D 비트엠업(3D beat ’em up) | 더 넓은 3차원 공간에서 근접 난투를 중심으로 진행하는 유형. | 비트엠업을 반드시 2D 횡스크롤로 한정하지 않는다. | 주변 적을 살피며 방향을 바꾸는 3D 비트엠업 전투를 구성한다. | — | [1] |

<a id="gd-1-2"></a>
### 1.2 슈팅

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 슈팅(Shooter) | 원거리 무기로 적을 공격하는 행동을 중심으로 하는 장르군. | 근접 기술 중심 액션과 달리 사격의 방향·거리·적중이 중심이다. | 원거리 적중과 위치 변경을 반복하는 슈팅 전투를 구성한다. | — | [2] |

<a id="gd-1-2-1"></a>
<a id="121-fps"></a>
#### 1.2.1 FPS

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| FPS(First-person shooter) | 캐릭터의 눈에 가까운 1인칭 시점에서 사격하는 슈팅 유형. | FPS는 시점과 사격의 결합이며 전술·아레나와 중첩될 수 있다. | 플레이어가 보는 방향을 사격 기준으로 쓰는 FPS를 구성한다. | — | [2] |
| ADS(Aim down sights) | 조준기 너머로 목표를 보는 정조준 방식. | 조준기 없이 전방으로 쏘는 방식과 구별한다. | ADS로 먼 표적을 겨누되 좁아진 주변 시야를 고려한다. | 정확도·시야·이동 속도 영향은 작품별 규칙이다. | [6] |
| 반동(Recoil) | 발사 때문에 조준 방향이 밀리거나 회전하는 변화. | 탄퍼짐은 같은 조준 방향 주변의 탄착 오차이며 반동과 별도다. | 연속 발사할수록 조준이 위로 밀리는 반동을 적용한다. | [7]: 수직 반동과 탄퍼짐을 별도 곡선으로 조정한다. | [7] |
| 탄퍼짐(Spread) | 발사 방향 주변의 일정 범위 안에서 탄착 방향이 분산되는 오차. | 조준 자체를 밀어 올리는 반동과 구별한다. | 이동 사격은 정지 사격보다 탄퍼짐 범위를 넓힌다. | 분산 범위 안의 확률 분포는 균일하거나 중심에 편향될 수 있다. | [7] |
| 반동 곡선(Recoil curve) | 연속 발사 진행에 따른 반동 변화의 패턴. | 퍼짐 곡선은 탄착 분산의 변화이며 조준 이동 패턴과 다르다. | 초기 발사보다 후반 발사의 수직 반동이 크게 증가한다. | — | [7] |
| 퍼짐 곡선(Spread curve) | 연속 발사 수 등에 따라 탄퍼짐이 변하는 관계. | 최초 탄퍼짐 값 하나와 발사 누적에 따른 변화는 다르다. | 연속 발사 횟수가 늘면 최대 탄퍼짐에 도달한다. | — | [7] |
| 히트스캔(Hitscan) | 발사 시 경로의 적중을 이동 시간 없이 판정하는 방식. | 날아가는 시간을 갖는 투사체와 구별한다. | 히트스캔 무기는 발사 시 조준 경로의 대상을 즉시 판정한다. | 화면에 탄도 효과가 보여도 판정은 즉시일 수 있다. | [6] |
| 투사체(Projectile, 사격 판정) | 공간을 이동하며 충돌하는 발사체를 사용하는 판정 방식. | 히트스캔과 달리 이동 시간 때문에 목표 위치 변화를 고려한다. | 먼 적에게는 투사체의 이동 시간을 고려해 앞쪽을 조준한다. | — | [6] |
| 중심 편향(Center biasing) | 탄퍼짐 범위 안에서도 중심 부근에 탄착할 확률을 높이는 조정. | 분산 범위의 크기와 그 안의 확률 분포는 별도다. | 정지 사격은 조준 중심 부근에 더 자주 탄착하도록 조정한다. | [7]: 개발사는 조정 도구를 Error Power라고도 부른다. | [7] |

<a id="gd-1-2-2"></a>
#### 1.2.2 TPS

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| TPS(Third-person shooter) | 플레이어 캐릭터와 주변 환경을 보여 주는 3인칭 시점의 슈팅 유형. | 3인칭 시점만 있는 게임과 달리 사격이 중심 행동이다. | 캐릭터 뒤 카메라로 주변 상황을 보며 사격하는 TPS를 구성한다. | — | [2] |
| 엄폐 사격(Cover shooting) | 보호물로 노출을 줄인 상태에서 사격하는 행동. | 엄폐는 보호물의 활용이며 잠입의 탐지 회피와 목적이 다를 수 있다. | 엄폐물 뒤에서 사격할 때만 몸을 노출한다. | TPS 전용 규칙은 아니며 전술 FPS에도 적용된다. | [2] |

<a id="gd-1-2-3"></a>
#### 1.2.3 전술 슈터

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 전술 슈터(Tactical shooter) | 소규모 교전의 계획·장비·자세와 현실적 전투 대응을 강조하는 슈팅 유형. | 시점 명칭과 달리 전투 설계의 강조점이다. | 팀원이 진입 방향을 나누고 장비를 선택하는 전술 슈터를 구성한다. | 현실성의 정도와 팀 규모는 작품마다 다르다. | [2] |
| 기울이기(Lean) | 엄폐물 옆으로 몸을 기울여 시야와 사격 노출을 조절하는 동작. | 전신을 옆으로 이동시키는 행동과 구별한다. | 기울이기로 몸 일부만 노출해 통로를 확인한다. | — | [2] |
| 장비 관리(전술 슈팅) | 교전에 필요한 무기·도구를 상황에 맞게 준비하고 운영하는 과정. | 루터 슈터의 누적 전리품 성장과 달리 임무 수행 선택을 강조한다. | 진입 전에 관측 도구와 근접 교전 무기를 배분한다. | — | [2] |

<a id="gd-1-2-4"></a>
#### 1.2.4 아레나 슈터

전문 용어 조회: [1.2 FPS의 반동·탄퍼짐·히트스캔·투사체](#121-fps). 아레나 FPS에서 동일 판정 용어를 사용하며, 빠른 이동 중 적중과 위치 조절을 설명할 때 조회한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 아레나 슈터(Arena shooter) | 제한된 전장에서 빠른 이동과 즉각적인 교전을 강조하는 슈팅 유형. | 단순히 작은 맵인 슈팅과 달리 속도·기동이 핵심 강조점이다. | 좁은 전장 안에서 빠르게 이동하며 사격하는 아레나 슈터를 구성한다. | [2]: 다인 FPS 중심 용례와 탑다운 아레나 슈팅 용례가 함께 있다. | [2] |
| 아레나 FPS(Arena FPS) | 아레나 슈터 중 1인칭 시점을 사용하는 유형. | 아레나 슈터 전체가 FPS인 것은 아니다. | 아레나 FPS에서 이동 중 조준 유지가 주요 숙련 과제가 된다. | — | [2] |

<a id="gd-1-2-5"></a>
#### 1.2.5 히어로 슈터

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 히어로 슈터(Hero shooter) | 고유 무기·능력을 가진 사전 설계 캐릭터를 골라 팀으로 교전하는 슈팅 유형. | 외형만 다른 캐릭터 선택과 달리 플레이 역할과 능력 구성이 다르다. | 서로 다른 능력을 가진 캐릭터 조합으로 목표를 공략한다. | FPS·TPS·전술 설계와 중첩될 수 있다. | [2] |
| 영웅 능력(Hero ability) | 선택 캐릭터에 고유하게 배정된 전투 기능. | 공통 무기 목록에서 자유 선택하는 장비와 구별한다. | 캐릭터의 방어 능력을 아군 진입 시점에 맞춰 사용한다. | — | [2] |
| 팀 조합(히어로 슈팅) | 서로 다른 영웅 능력과 역할을 고려한 팀 구성. | 인원 수만 채우는 팀 구성과 구별한다. | 근접 돌파와 원거리 지원이 가능한 팀 조합을 선택한다. | — | [2] |

<a id="gd-1-2-6"></a>
#### 1.2.6 루터 슈터

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 루터 슈터(Looter shooter) | 사격 전투로 얻는 장비를 축적·개선하며 더 큰 도전에 진입하는 슈팅 유형. | 단순 현장 무기 획득보다 지속적인 장비 성장 반복이 중심이다. | 임무 보상으로 장비를 개선한 뒤 더 어려운 임무에 진입한다. | 전리품의 일반 뜻은 [2.5 공용 전리품](#25-자원보유경제) 참조. | [2] |
| 장비 성장 루프(루터 슈팅) | 전투 보상으로 성능을 높이고 다음 고난도 보상을 추구하는 반복 구조. | 한 경기 안 무기를 찾는 배틀로얄 파밍과 구별한다. | 장비 성장 루프가 임무 난도와 보상 단계의 연결을 만든다. | — | [2] |
| 무작위 장비 속성(Randomized gear attributes) | 전리품 장비의 성능·특성 일부를 무작위로 결정하는 구성. | 장비 종류만 무작위로 선택하는 것과 구별한다. | 같은 무기 종류라도 획득 시 부가 속성이 달라진다. | — | [2] |

<a id="gd-1-2-7"></a>
#### 1.2.7 런앤건

전문 용어 조회: [1.2 FPS의 히트스캔·투사체](#121-fps), [1.4 플랫폼의 공중 제어·벽점프·코요테 타임·점프 버퍼](#14-플랫폼). 사격 판정과 도약 규칙을 결합해 설명하며 해당 기능의 존재는 작품별로 확인한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 런앤건(Run and gun, 장르) | 보행 캐릭터의 이동·점프와 원거리 사격을 결합한 슈팅 유형. | 이동하며 쏘는 행동 일반보다 역사적으로 2D 진행형 유형을 가리킨다. | 점프로 장애물을 넘고 전방 적을 사격하는 런앤건을 구성한다. | [2]: 2D 장르 명칭; [7]: FPS에서 이동 사격 행위를 뜻하기도 한다. | [2], [7] |
| 플랫폼 슈터(Platform shooter) | 플랫폼 이동과 사격을 결합한 유형. | 점프 과제와 사격 전투가 함께 진행의 중심을 이룬다. | 발판을 건너면서 사격 각도를 확보하는 플랫폼 슈터 구간을 둔다. | 런앤건과 겹치지만 모든 사격이 있는 플랫폼 게임을 같은 강도로 부르지는 않는다. | [3] |

<a id="gd-1-2-8"></a>
#### 1.2.8 레일 슈터

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 레일 슈터(Rail shooter) | 게임이 정해진 이동 경로를 따라 진행시키고 플레이어가 주로 사격을 조작하는 유형. | 자유 탐색 이동을 하는 FPS/TPS와 구별한다. | 이동은 정해진 경로로 진행하고 플레이어는 표적 사격에 집중한다. | 총 모양 입력 장치의 라이트건 슈터와 항상 같지는 않다. | [2] |
| 레일(Rail, 슈팅) | 플레이어 이동을 유도하는 사전 정의 진행 경로. | 실제 철도나 자유 이동 경로 전체를 뜻하지 않는다. | 레일이 코너를 돌면 새로운 표적군이 등장한다. | — | [2] |

<a id="gd-1-2-9"></a>
#### 1.2.9 슛뎀업·고정 화면·스크롤

전문 용어 조회: [탄막의 탄막 패턴·소형 피격 판정](#1210-탄막), [FPS의 투사체](#121-fps). 발사된 탄의 이동과 회피 배열을 설명할 때 조회하며, 모든 슛뎀업이 고밀도 탄막이나 소형 피격 판정을 사용하는 것은 아니다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 슛뎀업(Shoot ’em up, Shmup) | 화면상 기체·캐릭터를 움직여 다수 표적을 쏘고 공격을 피하는 전통 슈팅 유형. | 슈터 전체와 달리 화면 이동·사격을 중심으로 하는 역사적 장르 용례다. | 화면 안에서 위치를 바꾸며 적 탄을 피하는 슛뎀업을 구성한다. | 플랫폼 가이드의 편집 범위는 더 넓을 수 있다. | [2] |
| 고정 화면 슈터(Fixed shooter) | 화면 진행 공간이 고정된 슛뎀업 유형. | 화면이 한 방향으로 계속 진행하는 스크롤 슈터와 구별한다. | 고정 화면 안의 적 배열을 순서대로 파괴한다. | — | [2] |
| 스크롤 슈터(Scrolling shooter) | 전장이 주로 일정 방향으로 스크롤하며 진행하는 슛뎀업 유형. | 플레이어가 모든 경로 이동을 정하는 탐색형 슈팅과 다르다. | 전장이 세로로 스크롤하는 동안 새 적이 등장한다. | — | [2] |

<a id="gd-1-2-10"></a>
<a id="1210-탄막"></a>
#### 1.2.10 탄막

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 탄막 슈팅(Bullet hell, Danmaku) | 많은 투사체의 패턴을 읽고 좁은 틈으로 피하는 슈팅 유형. | 탄환이 조금 등장하는 모든 슈팅과 달리 고밀도 패턴 회피를 강조한다. | 넓게 퍼지는 탄막 사이의 통로를 찾아 이동한다. | 탄막 요소는 RPG 등 다른 장르에도 결합된다. | [8] |
| 탄막 패턴(Bullet pattern) | 탄환들의 배치·방향·시간 변화가 만드는 공격 배열. | 단일 탄환의 속성보다 여러 탄의 공간·시간 관계를 뜻한다. | 반복되는 원형 탄막 패턴의 빈 방향으로 이동한다. | — | [8] |
| 소형 피격 판정(탄막) | 기체 외형보다 작게 설정하여 탄막 틈 통과를 허용하는 피격 영역. | 화면상 그림 크기 전체와 실제 충돌 판정을 구별한다. | 기체 중심의 소형 피격 판정이 탄을 피하면 생존한다. | 많은 탄막 슈팅의 구성이나 모두 같은 크기는 아니다. | [8] |

<a id="gd-1-2-11"></a>
#### 1.2.11 트윈스틱

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 트윈스틱 슈터(Twin-stick shooter) | 이동과 사격 방향을 독립적으로 조작하는 슈팅 유형. | 이동 방향에 묶인 사격과 구별한다. | 오른쪽으로 이동하면서 왼쪽의 적을 사격한다. | 탑다운 시점과 자주 결합하지만 시점 자체와 같은 개념은 아니다. | [2] |
| 독립 조준(트윈스틱) | 이동 입력과 별도로 사격 방향을 정하는 조작 구성. | 두 스틱이라는 하드웨어 명칭과 별개로 키보드·포인터에도 구현할 수 있다. | 이동을 유지한 상태에서 조준 방향만 회전한다. | — | [2] |

<a id="gd-1-2-12"></a>
#### 1.2.12 부머 슈터

전문 용어 조회: [1.2 FPS의 반동·탄퍼짐·히트스캔·투사체](#121-fps). 복고 명칭이 특정 사격 판정이나 반동 규칙을 강제하지 않으므로 실제 규칙을 이 용어로 구별한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 부머 슈터(Boomer shooter) | 1990년대 FPS의 미학과 설계 원리를 의도적으로 되살리는 후대 슈팅 유형. | 오래된 FPS 전체나 플레이어 연령대를 뜻하지 않는다. | 복고식 전장 구성과 빠른 전투를 강조하는 부머 슈터로 설계한다. | [2]: 2010년대 이후 복고 FPS 용례; boomer는 오래됨을 나타내는 속어로 쓰인다. | [2] |
| 레트로 FPS(Retro FPS) | 과거 FPS의 표현·규칙을 재현하는 FPS 명칭. | 과거에 실제 출시된 고전 FPS와 재현 목적의 후대 작품을 구별한다. | 현대 입력 환경에서 고전적 사격 경험을 재현하는 레트로 FPS를 구성한다. | 부머 슈터와 겹치지만 동일한 고정 분류 표준은 아니다. | [2] |

<a id="gd-1-3"></a>
### 1.3 격투

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 격투(Fighting game) | 캐릭터의 공격·방어 기술로 상대와 대전하는 장르군. | 적 무리를 지나가는 비트엠업과 달리 대전 상대와 경기의 기술 교환이 중심이다. | 상대의 공격을 막고 빈틈에 반격하는 격투 경기를 구성한다. | 역사적 beat ’em up의 넓은 용례는 1.1 참조. | [1], [5] |
| 프레임(Frame, 격투 시간) | 기술의 발동·지속·회복 등을 세는 게임의 시간 단위. | 렌더링 그림 수를 말하는 문맥과 기술 판정의 시간 단위를 구별한다. | 두 기술의 발동이 3프레임과 4프레임이면 같은 시작 조건에서 앞 기술이 1프레임 빠르다. | 초 단위 길이는 게임의 동작 기준에 따르며 모든 게임을 60fps로 고정하지 않는다. | [9] |
| 발동(Startup) | 공격 시작부터 공격 판정이 발생하기 전까지의 구간. | 판정이 존재하는 지속, 이후 회복과 구별한다. | 발동이 긴 공격은 상대의 빠른 기술에 끊길 수 있다. | — | [5] |
| 지속(Active) | 공격 판정이 존재하여 상대에게 적중할 수 있는 구간. | 모션 전체 길이나 발동 시간과 구별한다. | 지속 구간이 끝난 공격은 상대에게 피해를 주지 못한다. | — | [5] |
| 회복(Recovery) | 공격의 유효 구간 뒤 다시 행동할 수 있을 때까지의 구간. | 피해 후 행동 불능인 피격 경직과 구별한다. | 공격이 빗나가면 회복 중 상대의 반격을 받을 수 있다. | — | [5] |
| 프레임 유불리(Frame advantage) | 공격 적중·가드 후 두 캐릭터가 다시 행동 가능해지는 시점의 차이. | 유리 여부만으로 사거리나 모든 후속타의 성공을 보장하지 않는다. | 가드 후 공격자가 먼저 움직일 수 있어 프레임 유리 상태가 된다. | 안전한 공격 중에도 소폭 불리한 공격이 있을 수 있다. | [10] |
| 가드(격투 적용) | 일반 뜻은 [공용 가드·블록](#210-공통-시스템) 참조. | 격투에서는 공격의 상·하단에 맞는 가드와 가드 경직·칩 피해 여부를 별도 규칙으로 정한다. | 하단 공격은 앉은 가드로 방어하고 가드 경직을 적용한다. | 가드 방향·입력 방식·잔여 피해는 작품마다 다르다. | [5] |
| 가드 경직(Block stun) | 공격을 막은 뒤 일반 행동을 할 수 없는 구간. | 피격 경직은 실제 적중 뒤 발생한다. | 후속 공격이 가드 경직 안에 들어오면 계속 방어 상태가 유지된다. | 일부 게임은 경직 중 전용 방어 행동을 허용한다. | [5] |
| 피격 경직(Hit stun) | 공격에 맞은 뒤 캐릭터가 일반 행동을 할 수 없는 구간. | 가드 경직·공격자 회복과 구별한다. | 후속타가 피격 경직 안에 적중하면 콤보가 이어진다. | — | [6], [5] |
| 히트박스(Hitbox, 공격) | 공격의 피해·효과를 전달하는 판정 영역. | 공격을 받는 허트박스와 구별한다. | 칼끝 히트박스가 상대 허트박스와 겹치면 타격을 판정한다. | [6]: 넓은 용례에서는 피격 영역까지 hitbox라고 부른다. | [6] |
| 허트박스(Hurtbox) | 대상이 공격을 받는 위치를 나타내는 판정 영역. | 렌더링 외형이나 공격 판정 영역과 반드시 같지 않다. | 숙일 때 허트박스가 낮아져 높은 공격을 피한다. | — | [6] |
| 콤보(Combo, 격투) | 첫 타가 맞은 뒤 상대가 일반 방어로 피할 수 없는 후속타의 연속. | 단순 입력 연계나 상대가 막을 수 있는 공격열과 구별한다. | 첫 타의 피격 경직 안에 다음 타격이 들어가 콤보가 성립한다. | 전용 탈출 수단이 있는 게임도 있다; 퍼즐·리듬의 콤보와 다르다. | [5] |
| 캔슬(Cancel) | 현재 기술의 남은 회복 등을 생략하고 다른 행동으로 전환하는 규칙. | 기술 종료 뒤 정상적으로 다음 기술을 실행하는 연결과 구별한다. | 기본기를 필살기로 캔슬해 후속타를 연결한다. | 허용 행동과 적중 조건은 작품마다 다르다. | [5] |
| 체인(Chain) | 기본기를 다른 기본기로 캔슬해 잇는 공격 연결. | 캔슬 없는 연결이나 일반 콤보 전체와 구별한다. | 약공격을 반복 캔슬해 짧은 체인을 만든다. | [5]: 좁게는 약기본기 반복, 넓게는 기본기 간 캔슬 전반. | [5] |
| 카운터 히트(Counter hit) | 상대 공격의 발동 등 지정된 취약 상태를 타격한 적중. | 단순히 뒤늦게 반격한 상황 전체를 뜻하지 않는다. | 상대 기술 발동을 끊으면 카운터 히트 보너스를 적용한다. | 회복까지 카운터 상태로 지정하는 게임도 있다. | [5] |
| 칩 데미지(Chip damage) | 가드했는데도 발생하는 잔여 피해. | 가드 실패로 받는 정상 피해와 구별한다. | 필살기를 막아도 소량의 칩 데미지가 남는다. | 이 피해로 KO가 가능한지는 작품마다 다르다. | [5] |
| 블록 스트링(Block string) | 방어 중인 상대를 압박하도록 이어지는 공격열. | 첫 적중 후 확정인 콤보와 구별한다. | 상대에게 연속 가드를 요구하는 블록 스트링을 구성한다. | 틈이 없는 경우만 지칭하거나 작은 틈도 허용하는 용례가 있다. | [5] |
| BnB(Bread and butter) | 자주 발생하는 상황에서 반복 사용하는 실용적인 기본 콤보. | 최대 피해·특수 상황 전용 콤보와 구별한다. | 초급 교육은 짧고 안정적인 BnB부터 제시한다. | — | [5] |
| 커맨드 기본기(Command normal) | 방향과 버튼을 함께 입력하는 특수 기본기. | 복잡한 필살기 입력이나 일반 앉은 기본기와 구별하는 관용 명칭이다. | 전방 입력과 강공격을 조합해 커맨드 기본기를 발동한다. | 일부 게임은 unique attack이라는 이름을 쓴다. | [5] |
| 커맨드 잡기(Command throw, Command grab) | 필살기 입력으로 발동하는 잡기 기술. | 일반 잡기와 해제 가능성·성능이 다를 수 있다. | 접근에 성공하면 커맨드 잡기로 가드를 공략한다. | 많은 작품에서 일반 잡기 해제가 통하지 않지만 보편 필수 규칙은 아니다. | [5] |
| 차지 입력(Charge input) | 지정 방향을 일정 시간 유지한 뒤 기술을 실행하는 입력. | 버튼을 눌러 공격 위력을 모으는 차지와 구별한다. | 뒤 방향 유지 후 전방과 공격을 입력해 차지 기술을 쓴다. | 유지 시간은 작품별 규칙이다. | [5] |

<a id="gd-1-3-1"></a>
#### 1.3.1 2D 대전

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 2D 대전 격투(2D fighter) | 주로 좌우·점프 축의 대전 공간에서 기술을 교환하는 격투 유형. | 그래픽이 3D여도 대전 이동이 한 면이면 이 용례에 포함될 수 있다. | 좌우 거리와 점프 높이를 관리하는 2D 대전을 구성한다. | — | [5] |
| 코너(Corner, 격투) | 대전 공간 끝에 몰려 더 뒤로 물러날 수 없는 위치. | 화면 가운데에서는 뒤로 이동할 공간이 남아 있다. | 코너에서는 후퇴가 막혀 상대의 압박을 피하기 어렵다. | — | [5] |
| 공중 대시(Air dash) | 공중에서 추가로 급속 이동하는 동작. | 일반 점프 궤적이나 지상 대시와 구별한다. | 점프 뒤 공중 대시로 접근 각도를 바꾼다. | 모든 2D 격투에 존재하는 기능은 아니다. | [5] |
| 백대시(Backdash) | 뒤쪽으로 빠르게 물러나 간격을 만드는 동작. | 계속 걷는 후퇴와 구별한다. | 백대시로 상대 공격을 헛치게 만든다. | 무적 여부와 입력 방식은 작품마다 다르다. | [5] |

<a id="gd-1-3-2"></a>
#### 1.3.2 3D 대전

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 3D 대전 격투(3D fighter) | 카메라 깊이 방향까지 이동하여 상대와 대전하는 격투 유형. | 입체 모델을 쓰면서 2D 이동만 하는 격투와 구별한다. | 상대 공격축에서 옆으로 벗어나는 3D 대전을 구성한다. | 렌더링이 아니라 이동 선택이 구별 기준이다. | [11] |
| 사이드스텝(Sidestep) | 3D 대전에서 카메라 쪽이나 반대쪽으로 이동해 공격축을 비키는 동작. | 상대와의 좌우 거리만 바꾸는 전후 이동과 구별한다. | 사이드스텝으로 직선 공격을 헛치게 만든다. | — | [11] |

<a id="gd-1-3-3"></a>
#### 1.3.3 태그팀

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 태그팀 격투(Tag-team fighter) | 여러 캐릭터를 한 팀으로 편성하고 교대하며 대전하는 유형. | 여러 참가자가 있는 경기 전체와 다르다. | 주력 캐릭터를 교대하며 팀 체력을 관리한다. | 어시스트가 없는 태그 구조도 가능하다. | [5] |
| 어시스트(Assist, 격투) | 화면 밖 팀 캐릭터가 잠시 등장해 행동을 지원하는 기능. | 직접 조작 캐릭터를 바꾸는 태그와 구별한다. | 어시스트 공격 중 주력 캐릭터가 접근한다. | 지원 캐릭터가 피격될 수 있는지는 규칙에 따른다. | [5] |
| 액티브 태그(Active tag) | 지원 행동 중 등장한 팀 캐릭터를 직접 조작 대상으로 전환하는 교대 방식. | 지원만 수행하고 물러나는 어시스트와 구별한다. | 어시스트 등장 중 액티브 태그로 조작 캐릭터를 바꾼다. | 제품별 교대 명칭은 다를 수 있다. | [5] |

<a id="gd-1-3-4"></a>
#### 1.3.4 플랫폼 격투

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 플랫폼 격투(Platform fighter) | 발판 이동과 상대를 전장 밖으로 밀어내는 대전을 결합한 유형. | 체력 소진만으로 끝내는 전통 대전과 대표 승리 구조가 다르다. | 발판 높이를 활용해 상대를 전장 밖으로 밀어낸다. | 피해 누적과 밀려남 관계는 대표 작품의 규칙이며 모든 변형에 동일 적용하지 않는다. | [12], [13] |
| 넉백(Knockback, 플랫폼 격투) | 타격으로 상대를 이동시켜 전장 이탈 위험을 만드는 효과. | 피해량과 별개로 위치·방향 변화가 승부에 중요하다. | 강한 넉백으로 가장자리의 상대를 바깥으로 날린다. | — | [12] |
| 복귀(Recovery, 플랫폼 격투) | 전장 밖으로 밀려난 캐릭터가 발판으로 돌아오는 행동. | 공격 뒤 회복 프레임의 recovery와 의미가 다르다. | 공중 기술을 사용해 전장으로 복귀한다. | — | [12] |
| 누적 피해(플랫폼 격투) | 타격받은 양을 누적하여 밀려나는 거리 등에 반영하는 값. | 남은 체력을 직접 나타내는 값과 구별한다. | 피해가 누적되면 같은 공격에도 더 멀리 날아간다. | 공식 자료의 대표 규칙; 제품별 예외가 있다. | [12] |

<a id="gd-1-4"></a>
<a id="14-플랫폼"></a>
### 1.4 플랫폼

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 플랫폼(Platformer) | 발판·높낮이·장애물 사이 이동을 주요 과제로 삼는 장르. | 점프가 등장하는 모든 액션과 달리 공간 통과가 중심 과제다. | 움직이는 발판 사이를 건너 목표에 도달한다. | 점프 없는 플랫폼 작품도 있어 점프 버튼만으로 판정하지 않는다. | [3] |
| 공중 제어(Air control) | 떠 있는 동안 이동 입력으로 궤적을 바꾸는 조작 성질. | 도약 때 정해진 궤적을 유지하는 방식과 구별한다. | 점프 중 방향 입력으로 착지 위치를 수정한다. | 공용 이동의 장르 한정 용례다. | [3] |
| 벽점프(Wall jump) | 벽에 닿거나 붙은 상태를 이용해 다시 도약하는 동작. | 바닥에서 점프하거나 공중에서 재도약하는 동작과 구별한다. | 양쪽 벽을 번갈아 차고 위로 올라간다. | — | [3] |
| 점프 버퍼(Jump input buffering) | 점프 가능한 조건이 생기기 전 입력을 짧게 보존하고 조건이 충족되면 실행하는 방식. | 코요테 타임은 지면 이탈 뒤 점프 자격을 유예하고 버퍼는 입력 뒤 실행 기회를 기다린다. | 착지 직전에 누른 점프가 버퍼 안에 남아 있으면 착지하자마자 실행한다. | 착지가 대표 조건이며 입력 저장 범위·허용 조건·기간은 작품별 규칙이다. | [14], [15] |
| 코요테 타임(Coyote time, 플랫폼) | 지면에서 벗어난 직후에도 잠깐 점프 입력을 인정하는 유예. | 착지 전 입력을 저장하는 점프 버퍼와 방향이 다르다. | 발판 끝을 막 벗어난 입력도 코요테 타임 안이면 점프한다. | 다른 장르에서는 늦은 입력 유예를 비유적으로 가리키기도 한다. | [6] |

<a id="gd-1-4-1"></a>
#### 1.4.1 2D·3D 플랫폼

전문 용어 조회: [1.4 플랫폼의 공중 제어·벽점프·코요테 타임·점프 버퍼](#14-플랫폼). 같은 도약 용어를 사용하되 3D에서는 깊이와 카메라 방향까지 착지 판단에 포함한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 2D 플랫폼(2D platformer) | 주로 한 평면에서 좌우·상하 이동으로 발판 과제를 수행하는 유형. | 시각적 입체 표현과 플레이 이동 차원을 구별한다. | 횡스크롤 화면에서 발판 높이와 거리를 읽는다. | — | [3] |
| 2.5D 플랫폼(2.5D platformer) | 입체 그래픽을 사용하면서 이동을 주로 2차원에 제한하는 플랫폼 유형. | 자유 깊이 이동이 가능한 3D 플랫폼과 구별한다. | 입체 배경을 보여 주되 이동은 좌우·상하 평면에 제한한다. | 2.5D는 다른 기술적 표현을 포함하는 넓은 용어이기도 하다. | [3] |
| 3D 플랫폼(3D platformer) | 깊이를 포함한 3차원 공간에서 이동·착지 과제를 수행하는 유형. | 발판 거리 판단에 카메라 방향과 깊이가 작용한다. | 카메라를 회전해 다음 발판의 깊이를 확인한다. | — | [3] |

<a id="gd-1-4-2"></a>
#### 1.4.2 퍼즐 플랫폼

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 퍼즐 플랫폼(Puzzle-platformer) | 플랫폼 이동 구조 안에서 환경 규칙 풀이를 중심 과제로 삼는 유형. | 정밀 입력만으로 통과하는 플랫폼 과제와 구별한다. | 환경 장치를 조작해 건널 수 있는 발판 배열을 만든다. | 물리 퍼즐과도 중첩될 수 있다. | [3] |
| 환경 조작(퍼즐 플랫폼) | 발판·장치 등 이동 조건을 바꿔 경로를 만드는 행동. | 기존 발판 위를 이동하는 실행 과제와 구별한다. | 스위치로 발판을 옮긴 뒤 열린 경로를 통과한다. | — | [3] |

<a id="gd-1-4-3"></a>
#### 1.4.3 수집형 플랫폼

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 수집형 플랫폼(Collect-a-thon) | 공간을 탐색하며 여러 수집 목표를 완수하는 플랫폼 유형. | 단일 출구까지 이동하는 선형 통과 구조와 구별한다. | 각 지역에서 수집 목표를 달성해 다음 지역을 연다. | 동전 등 아이템이 조금 등장한다는 사실만으로 이 유형이 되지 않는다. | [3] |
| 수집 목표(Collectible objective) | 분산된 수집물을 찾는 일을 진행 목표로 사용하는 구성. | 전투 성능용 전리품 획득과 목적이 다르다. | 숨겨진 수집 목표를 달성하면 추가 지역이 열린다. | — | [3] |

<a id="gd-1-4-4"></a>
#### 1.4.4 러너

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 러너(Runner) | 전진을 지속하며 장애물을 회피하거나 뛰어넘는 유형. | 전진 입력을 매번 선택하는 일반 플랫폼과 구별한다. | 자동 전진 중 점프 시점을 선택해 장애물을 넘는다. | 러너가 반드시 무한 진행인 것은 아니다. | [3] |
| 자동 전진(Auto-run) | 게임이 캐릭터의 앞으로 가는 이동을 지속적으로 수행하는 구성. | 이동 방향을 완전히 자유롭게 정하는 방식과 다르다. | 자동 전진 속도를 유지한 채 장애물 대응만 조작한다. | — | [3] |

<a id="gd-1-5"></a>
### 1.5 잠입

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 잠입(Stealth) | 적에게 들키는 일을 피하거나 통제하며 목표를 수행하는 장르·플레이 유형. | 단순히 적을 쓰러뜨리는 전투와 달리 적의 인지가 주요 제약이다. | 순찰자의 관측을 피해 목표 지점에 침투한다. | 잠입 기능은 다른 장르에도 결합된다. | [16] |
| 시야선(Line of sight, 잠입) | 관측자와 대상 사이에 시각 탐지가 가능한 연결. | 거리 조건만 만족해도 벽 등 장애물로 차단될 수 있다. | 벽이 시야선을 차단하면 순찰자가 플레이어를 보지 못한다. | 시야각·거리·조명은 별도 탐지 조건이다. | [16] |
| 소음(Noise, 잠입) | 적이 위치·이상 상황을 알아차리게 하는 행동의 청각 신호. | 보이는 여부와 독립적으로 탐지를 유발할 수 있다. | 금속 바닥의 달리기 소음이 가까운 적을 부른다. | — | [16] |
| 경보 단계(Alert phase) | 탐지 사건 뒤 적이 적극적으로 탐색·추격하는 상태. | 아직 플레이어를 인지하지 않은 일상 순찰과 구별한다. | 경보 단계에 진입하면 적이 마지막 목격 장소를 수색한다. | 즉시 임무 실패인지 회복 가능한지는 작품에 따른다. | [16] |
| 가시성(Visibility, 잠입) | 조명·그림자 등 때문에 캐릭터가 관측될 정도. | 탐지가 이미 성립했는지와 노출 가능성은 다르다. | 어두운 구역에서 가시성이 낮아진다. | 화면 표시 수치가 없는 작품도 있다. | [16] |
| 변장(Disguise) | 외양이나 신분 표식을 바꿔 적의 식별을 피하는 방법. | 물체 뒤에 몸을 가리는 은폐와 구별한다. | 경비 복장으로 통과하되 가까운 관측은 피한다. | — | [16] |
| 유인(Distraction, 잠입) | 소리·물체 등으로 적의 주의를 다른 곳으로 돌리는 행동. | 적을 직접 무력화하는 공격과 구별한다. | 소리를 내 순찰자의 시선을 통로 밖으로 돌린다. | — | [16] |
| 고스팅(Ghosting) | 어떤 적에게도 탐지되지 않고 목표를 완료하는 잠입 접근. | 비살상 성공과 같지 않으며 탐지 여부가 기준이다. | 적을 건드리지 않고 목표를 마쳐 고스팅 조건을 충족한다. | — | [16] |

<a id="gd-1-5-1"></a>
#### 1.5.1 액션 잠입·샌드박스 잠입

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 액션 잠입(Action stealth) | 탐지 회피와 직접 전투를 함께 허용하는 잠입 유형. | 발견 시 즉시 실패하는 잠입 구성과 구별한다. | 들키면 전투로 돌파하거나 다시 은폐할 수 있다. | 전투 허용 비중은 작품마다 다르다. | [16] |
| 샌드박스 잠입(Sandbox stealth) | 여러 경로·도구·접근을 조합해 침투 목표를 수행하는 잠입 유형. | 사전 지정 단일 잠입 절차만 따르는 구성과 구별한다. | 변장과 우회 중 하나를 골라 목표에 접근한다. | 기존 공식 자료의 freeform sandbox stealth 용례를 좁게 사용한다. | [17] |

<a id="gd-1-6"></a>
### 1.6 어드벤처·탐색

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 어드벤처(Adventure) | 이야기·탐색·상호작용과 퍼즐 풀이를 중심으로 진행하는 장르군. | 액션 도전을 중심으로 하는 액션 어드벤처와 구별한다. | 장소를 조사하고 필요한 아이템을 사용해 이야기를 진행한다. | 액션 요소가 전혀 없어야 한다는 필수 조건은 아니다. | [18] |

<a id="gd-1-6-1"></a>
#### 1.6.1 포인트앤클릭

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 포인트앤클릭 어드벤처(Point-and-click adventure) | 포인터로 장소·사물·인물을 지정하며 상호작용하는 어드벤처 유형. | 화면을 클릭한다는 사실만으로 모든 장르를 이 유형이라 부르지 않는다. | 사물을 선택해 조사하고 보유 아이템을 적용한다. | — | [18] |
| 인벤토리 퍼즐(Inventory puzzle) | 가진 아이템을 적절한 대상·상황에 사용해 풀어야 하는 과제. | 아이템 목록을 단순 관리하는 기능과 구별한다. | 보유한 열쇠를 올바른 문에 사용해 인벤토리 퍼즐을 해결한다. | 공용 인벤토리 정의는 공용 사전 참조. | [18] |
| 픽셀 헌팅(Pixel hunting) | 아주 작은 상호작용 위치를 화면에서 찾아야 하는 탐색. | 규칙을 추론하는 어려움과 위치 자체를 찾는 어려움은 다르다. | 조사 가능한 위치를 강조해 픽셀 헌팅 부담을 줄인다. | 대체로 가독성 문제를 지적하는 표현으로 쓰인다. | [18] |
| 대화 트리(Dialogue tree) | 대화 선택지와 그 응답·후속 선택이 연결된 구조. | 대사 목록의 단순 재생과 구별한다. | 질문을 선택하면 응답과 새로운 대화 가지가 열린다. | 선택·분기는 1.7 및 공용 선택 참조. | [18] |

<a id="gd-1-6-2"></a>
#### 1.6.2 퍼즐 어드벤처

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 퍼즐 어드벤처(Puzzle adventure) | 독립적인 장치·논리 과제를 풀며 세계와 이야기를 여는 어드벤처 유형. | 아이템 사용 퍼즐 중심 포인트앤클릭과 강조점이 다르다. | 장치의 규칙을 파악해 다음 공간을 연다. | 포인트앤클릭 조작과 중첩될 수 있다. | [18] |
| 장치 퍼즐(Mechanism puzzle) | 환경 장치의 작동 관계를 파악하고 조작해 목표 상태를 만드는 과제. | 단서를 찾는 탐색과 장치를 작동시키는 해법을 구별한다. | 레버 연결을 시험해 문이 열리는 조합을 찾는다. | — | [19], [18] |

<a id="gd-1-6-3"></a>
<a id="163-워킹-시뮬레이터"></a>
#### 1.6.3 워킹 시뮬레이터

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 워킹 시뮬레이터(Walking simulator) | 이동과 환경 상호작용을 통해 서사를 발견하는 탐색 중심 유형. | 걷기 동작의 현실적 재현을 뜻하는 명칭은 아니다. | 공간을 걸으며 기록물을 발견해 사건의 흐름을 이해한다. | 처음에는 적은 전통적 과제를 비판하는 용례도 있었고 environmental narrative game이라는 명칭도 쓴다. | [18] |
| 환경 서사(Environmental narrative) | 공간의 물체·배치·기록 등에서 이야기를 읽게 하는 구성. | 대사·영상의 직접 설명과 구별한다. | 방 안의 기록과 흔적을 연결해 사건을 해석한다. | 이 기법만으로 특정 장르를 판정하지 않는다. | [18] |

<a id="gd-1-7"></a>
### 1.7 서사·인터랙티브 픽션

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 인터랙티브 픽션(Interactive fiction, IF) | 입력이나 선택으로 읽을 내용·서사 진행에 참여하는 이야기 형식. | 텍스트 출력만 있는 모든 게임이나 단순 전자책과 구별한다. | 선택에 따라 다른 사건을 읽는 인터랙티브 픽션을 구성한다. | 역사적으로 텍스트 어드벤처와 겹치지만 현대 IF는 퍼즐이 없는 서사도 포함한다. | [18], [20] |

<a id="gd-1-7-1"></a>
#### 1.7.1 텍스트 어드벤처

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 텍스트 어드벤처(Text adventure) | 텍스트로 환경을 설명하고 명령을 받아 탐색·과제를 진행하는 유형. | 미리 제시된 선택지만 고르는 이야기와 조작 방식이 다르다. | 장소 설명을 읽고 조사 명령을 입력한다. | 현대 IF 전체와 동일 범위는 아니다. | [18] |
| 파서(Parser, 텍스트 어드벤처) | 플레이어의 텍스트 명령을 게임 행동으로 해석하는 처리 구성. | 선택 버튼의 사전 연결과 다르다. | 파서가 대상과 행동을 읽어 조사 결과를 출력한다. | 일반 프로그래밍 파서의 장르 적용이다. | [18] |

<a id="gd-1-7-2"></a>
#### 1.7.2 선택형 이야기

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 선택형 이야기(Choice-based narrative) | 제시된 선택을 통해 읽을 사건과 이야기 흐름을 결정하는 유형. | 자유 문장 명령 입력 중심 텍스트 어드벤처와 구별한다. | 선택형 이야기에서 방문할 장소를 두 후보 중 고른다. | — | [20] |
| 서사 분기(Narrative branch) | 선택·조건에 따라 이야기 흐름이 다른 내용 경로로 나뉘는 구조. | 선택지가 달라도 같은 내용으로 즉시 이어질 수 있다. | 앞선 선택에 따라 다른 장면으로 서사가 분기한다. | 공용 선택과 달리 내용 흐름의 결과를 뜻한다. | [20] |
| 서사 합류(Rejoin, Gather) | 갈라진 이야기 경로가 다시 같은 흐름으로 모이는 구조. | 앞선 선택의 상태까지 모두 지운다는 뜻은 아니다. | 두 조사 경로가 다음 장면에서 합류한다. | gather는 ink의 구체적 합류 구성 명칭이다. | [20] |
| 서사 플래그(Narrative flag) | 과거 사건·선택을 기억해 후속 내용 조건에 사용하는 상태값. | 현재 화면의 선택지 자체와 구별한다. | 약속을 지킨 플래그가 후반 선택지를 연다. | 변수는 숫자·내용도 저장하고 플래그는 주로 조건 상태를 가리킨다. | [20] |
| 조건부 선택지(Conditional choice) | 현재 상태가 조건을 만족할 때만 제공되는 선택지. | 항상 제공되는 고정 선택지와 구별한다. | 이전 장면을 본 경우에만 질문 선택지가 나타난다. | — | [20] |
| 루트(Route, 서사) | 특정 인물·사건·결말을 따라 이어지는 이야기 경로. | 개별 분기 하나보다 긴 내용 진행을 가리킨다. | 특정 인물 관련 선택을 누적하면 그 인물의 루트로 진입한다. | 격투에서는 콤보 경로를 route라고도 부른다. | [20], [21] |

<a id="gd-1-7-3"></a>
#### 1.7.3 비주얼노벨·오토메

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 비주얼노벨(Visual novel) | 대사·서술 텍스트와 배경·캐릭터 이미지 등을 결합해 이야기를 제시하는 형식. | 이미지가 있는 모든 어드벤처를 뜻하지 않는다. | 캐릭터 이미지와 대사를 중심으로 장면을 진행한다. | 선택 분기가 필수는 아니다. | [22] |
| 키네틱 노벨(Kinetic novel) | 선택 분기 없이 정해진 이야기 흐름을 읽는 비주얼노벨 유형. | 선택형 비주얼노벨과 상호작용 구조가 다르다. | 키네틱 노벨은 선택지 없이 결말까지 이어진다. | — | [22] |
| 오토메(Otome) | 여성 주인공과 남성 캐릭터들의 관계·연애 서사를 중심으로 하는 유형. | 비주얼노벨 표현 형식과 연애 대상 구성을 구별한다. | 남성 캐릭터별 관계 선택에 따라 다른 이야기 경로가 열린다. | 관계·루트 구조와 연애 비중은 작품마다 다르다. | [21] |
| 엔딩(Ending, 서사) | 이야기 진행의 결과를 마무리하는 종결 내용. | 세션 종료나 중간 실패 화면과 구별한다. | 누적 선택에 맞는 엔딩 장면을 재생한다. | — | [22] |
| 캐릭터 스프라이트(Character sprite, VN) | 배경 위에 표시하여 인물의 모습·표정을 전달하는 이미지. | 배경 이미지와 화면상 역할이 다르다. | 대화 변화에 맞춰 캐릭터 스프라이트 표정을 바꾼다. | — | [22] |

<a id="gd-1-8"></a>
### 1.8 퍼즐

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 퍼즐(Puzzle game) | 주어진 규칙·상태에서 해법을 찾는 과제를 중심으로 하는 장르군. | 빠른 입력 수행만이 아니라 관계·패턴·순서의 풀이가 중심이다. | 제한된 조작으로 목표 상태를 만드는 퍼즐을 구성한다. | 실시간 요소가 있어도 퍼즐일 수 있다. | [19] |

<a id="gd-1-8-1"></a>
#### 1.8.1 논리·공간 퍼즐

전문 용어 조회: [2.3 공용 제약](#23-상태조건판정), [2.8 공용 단서](#28-정보확률), [1.8 소코반의 상자 밀기](#185-소코반). 조건의 제한, 해법 정보, 실제 배치 조작을 각각 구별해 조회한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 논리 퍼즐(Logic puzzle) | 조건과 관계를 적용해 가능한 해법을 추론하는 퍼즐 유형. | 주로 반사 입력으로 성공하는 과제와 구별한다. | 서로 양립할 수 없는 조건을 제거해 해답을 찾는다. | — | [19] |
| 공간 퍼즐(Spatial puzzle) | 형태·위치·방향·배치 관계의 파악과 조작이 중심인 퍼즐 유형. | 단어 지식이나 수치 계산 중심 과제와 구별한다. | 도형 방향을 바꿔 빈 공간에 맞춘다. | 논리·물리 퍼즐과 중첩 가능하다. | [19] |

<a id="gd-1-8-2"></a>
#### 1.8.2 물리 퍼즐

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 물리 퍼즐(Physics puzzle) | 게임의 물리 작동과 환경을 활용해 해결하는 퍼즐 유형. | 추상적인 배치 규칙만으로 해결하는 과제와 구별한다. | 물체의 충돌과 낙하를 이용해 목표를 작동시킨다. | 실제 자연법칙과 완전히 같은 시뮬레이션일 필요는 없다. | [19] |
| 물리 연쇄(Physics chain reaction) | 한 물리 사건이 다음 운동·충돌을 이어 발생시키는 구성. | 단순 타일 자동 매칭 연쇄와 작동 기준이 다르다. | 첫 물체를 떨어뜨려 연속 충돌을 만든다. | — | [19] |

<a id="gd-1-8-3"></a>
#### 1.8.3 매치3·블라스트

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 타일 매칭(Tile-matching) | 타일을 조작해 매칭 조건을 만들고 제거하는 퍼즐 유형. | 모든 타일 배치 게임이 제거·매칭 중심인 것은 아니다. | 같은 색 타일을 모아 제거 조건을 만든다. | — | [23] |
| 매치3(Match-three) | 같은 종류 타일 셋 이상을 맞추는 조건을 중심으로 하는 유형. | 매칭 일반 중 최소 일치 수 조건을 한정한다. | 같은 색 세 타일을 이어 제거한다. | 인접 교환이 대표 방식이지만 매치3 명칭만으로 모든 조작이 교환인 것은 아니다. | [19], [23] |
| 매치(Match, 퍼즐) | 제거·보상 조건을 만족하는 타일 집합. | 타일 한 번 이동이나 격투 경기의 match와 구별한다. | 이번 교환으로 세 타일 매치가 성립한다. | — | [23] |
| 인접 교환(Adjacent swap) | 맞닿은 두 타일의 위치를 맞바꾸는 조작. | 임의 위치끼리 교환하거나 한 묶음을 선택 제거하는 방식과 다르다. | 인접 교환으로 가로 매치를 만든다. | — | [23] |
| 블라스트(Blast, Collapse-style puzzle) | 이미 인접한 동일 타일 묶음을 선택해 제거하는 매칭 유형. | 교환으로 매치를 만드는 방식과 구별한다. | 같은 색 묶음을 선택해 한 번에 제거한다. | blast는 상업적 명칭이며 학술 원문은 Chain Shot·Collapse 계열 규칙을 설명한다. | [19], [23] |
| 퍼즐 콤보(Combo, 동시 매치) | 한 조작으로 여러 매치를 동시에 성립시키는 결과. | 격투의 확정 연속 타격과 다르다. | 한 번의 교환으로 가로·세로 매치를 동시에 만들어 콤보 보상을 받는다. | [23]의 용례; 작품에 따라 시간 내 연속 성공도 콤보라고 부른다. | [23] |
| 특수 타일(Special tile) | 큰 매치 등으로 생성되거나 고유 제거 효과를 가진 타일. | 일반 일치 타일과 효과가 다르다. | 네 타일 매치가 줄 제거용 특수 타일을 만든다. | 생성 조건과 효과는 제품별 규칙이다. | [23] |
| 필수 매치(Obligatory match) | 유효 조작이 반드시 매치를 발생시켜야 한다는 규칙. | 매치 없는 준비 이동도 허용하는 규칙과 구별한다. | 매치를 만들지 않는 교환은 실행되지 않는다. | — | [23] |

<a id="gd-1-8-4"></a>
#### 1.8.4 블록·발사형 매칭

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 낙하 블록 퍼즐(Falling-block puzzle) | 내려오는 조각을 이동·회전·배치해 조건을 완성하는 유형. | 이미 놓인 타일을 교환하는 매칭 퍼즐과 조작 시점이 다르다. | 낙하 중 조각을 회전해 빈칸 없는 줄을 만든다. | 모든 낙하 블록 퍼즐이 색 매치나 줄 완성 같은 단일 조건을 공유하지 않는다. | [23] |
| 줄 완성(Line completion) | 가로줄을 빈칸 없이 채워 제거 조건을 만족시키는 규칙. | 동일 색·종류의 일치와 구별한다. | 모양이 다른 블록이라도 줄이 가득 차면 제거한다. | — | [23] |
| 발사형 매칭(Shooting tile-matching) | 타일·구슬을 쏘아 기존 배열에 붙여 매치를 만드는 유형. | 원거리 적을 처치하는 슈팅과 목표가 다르다. | 구슬을 배열의 빈 위치로 쏘아 같은 색을 모은다. | 버블슈터는 이 구성의 대표적 명칭이지만 모든 발사형이 같은 배열 규칙은 아니다. | [23] |
| 버블슈터(Bubble shooter) | 구슬을 발사해 같은 종류 묶음을 만드는 매칭 퍼즐 유형. | 일반 탄환 전투가 아니라 구슬 배열을 조작한다. | 발사 각도를 골라 같은 색 구슬 옆에 붙인다. | — | [23] |

<a id="gd-1-8-5"></a>
<a id="185-소코반"></a>
#### 1.8.5 소코반

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 소코반(Sokoban, Box-pushing puzzle) | 격자 공간의 상자를 밀어 지정 위치에 보내는 퍼즐 유형. | 길 찾기뿐 아니라 이동 물체의 배치와 막힘을 함께 관리한다. | 상자가 통로를 막지 않도록 순서를 정해 목표 칸으로 민다. | 원작 이름이 유형 명칭으로 확장됐다; 변형은 당기기를 허용하기도 한다. | [19] |
| 상자 밀기(Box pushing) | 인접한 상자를 밀어 위치를 바꾸는 조작. | 캐릭터만 이동하는 동작이나 먼 물체 직접 배치와 구별한다. | 상자 뒤로 돌아간 뒤 빈칸 방향으로 민다. | — | [19] |

<a id="gd-1-8-6"></a>
#### 1.8.6 숨은그림찾기·탈출

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 숨은그림찾기(Hidden object game) | 장면에 숨겨진 목록의 대상을 찾아내는 퍼즐 유형. | 자유롭게 모든 물체를 조사하는 어드벤처와 목표 형식이 다르다. | 목록에 적힌 다섯 물체를 복잡한 장면에서 찾는다. | HOPA는 어드벤처 결합 용례도 포함한다. | [19] |
| 탐색 목록(Object list) | 숨은그림 장면에서 찾아야 할 대상을 지정하는 목록. | 단서의 자유 수집보다 완료 판정 대상을 명시한다. | 찾은 대상은 탐색 목록에서 지워진다. | — | [19] |
| 탈출 퍼즐(Escape-room game) | 제한된 공간의 사물·단서를 사용해 탈출 조건을 해결하는 유형. | 일반 탐색 어드벤처보다 공간과 탈출 목표를 한정한다. | 방의 장치를 풀어 출구 잠금을 해제한다. | — | [19], [18] |

<a id="gd-1-8-7"></a>
#### 1.8.7 프로그래밍 퍼즐

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 프로그래밍 퍼즐(Programming puzzle) | 명령·코드를 구성하여 자동 동작이 목표를 충족하게 만드는 유형. | 플레이어가 매 순간 직접 조작하는 퍼즐과 구별한다. | 명령 순서를 작성해 기계가 목표 물자를 운반하게 한다. | 텍스트 코드와 시각적 명령 배열 모두 가능하다. | [19] |
| 명령 배열(Instruction sequence) | 자동 실행될 행동을 순서대로 지정한 구성. | 조작의 실시간 반응보다 실행 순서가 결과를 만든다. | 반복 실행 전에 명령 배열을 수정한다. | — | [19] |

<a id="gd-1-9"></a>
### 1.9 단어·퀴즈

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 단어게임(Word game) | 문자·낱말의 구성이나 의미를 핵심 규칙으로 사용하는 유형군. | 단지 텍스트로 표현된 모든 게임과 다르다. | 주어진 문자로 허용된 낱말을 만든다. | — | [24] |
| 퀴즈(Quiz game) | 문항의 답을 찾아 제출하고 정오를 판정하는 유형군. | 낱말 조합만을 목표로 하는 퍼즐과 다르다. | 제시된 문항에 답을 제출해 정답 점수를 받는다. | 지식·추론·파티 요소가 결합될 수 있다. | [25] |

<a id="gd-1-9-1"></a>
#### 1.9.1 낱말·타자·상식

전문 용어 조회: 타자게임의 입력 수행은 [2.2 공용 입력·행동](#22-주체대상행동)과 [2.3 공용 판정](#23-상태조건판정), 상식 퀴즈의 지식 제시와 결과는 [2.8 공용 정보·단서](#28-정보확률)와 [2.4 공용 점수·성공](#24-목표결과보상)을 참조한다. 실제 입력 판정 방식, 단서 제공 여부, 점수 규칙은 작품별로 확인한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 문자 배열 게임(Letter arrangement game) | 주어진 문자들을 배열해 낱말을 만드는 단어게임 유형. | 단서에서 낱말을 먼저 추론하는 크로스워드와 구별한다. | 제한된 문자 묶음으로 가장 긴 낱말을 만든다. | — | [24] |
| 크로스워드(Crossword) | 단서에 맞는 낱말을 교차하는 격자에 채우는 퍼즐. | 교차 문자와 문항 단서를 함께 활용한다. | 이미 채운 교차 문자를 이용해 다음 낱말을 추론한다. | — | [24] |
| 교차 문자(Crossing letter) | 서로 다른 낱말이 같은 격자 칸에서 공유하는 문자. | 한 낱말 안의 문자만 확인하는 제약과 다르다. | 교차 문자가 두 답의 후보를 동시에 제한한다. | — | [24] |
| 타자게임(Typing game) | 문자·단어의 키보드 입력을 주요 수행 행동으로 삼는 유형. | 낱말의 의미를 알아도 입력 수행이 별도 과제가 된다. | 표시된 단어를 입력해 적의 공격을 막는다. | 타자게임이 반드시 교육용이거나 단어 추론 게임인 것은 아니다. | [26] |
| 상식 퀴즈(Trivia) | 여러 주제의 사실 지식을 묻는 퀴즈 유형. | 주어진 단서만으로 푸는 순수 추론 과제와 구별한다. | 주제별 사실 문항에서 정답을 고른다. | 파티형 구성은 결합 형식이며 trivia의 필수 조건은 아니다. | [25] |

<a id="gd-1-10"></a>
### 1.10 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| RPG(Role-Playing Game) | 캐릭터나 파티의 능력·역할을 발전시키며 세계의 도전과 이야기를 진행하는 게임. | 캐릭터 육성과 역할 구성이 중심이며 수치 하나의 존재만으로 판정하지 않는다. | 캐릭터의 직업과 능력 구성이 탐험과 전투에서 가능한 행동을 바꾼다. | [27]은 모바일 전투·성장 중심; [28]은 공동 서사와 역할 연기를 포함한다. | [27], [28] |
| 능력치(캐릭터, Stat) | 캐릭터의 힘·민첩·지능 등 수행 능력을 수치로 표현한 값. | 현재 체력 같은 소모 상태와 기본 능력의 표현을 구별한다. | 힘 능력치는 무기 공격 판정에 적용된다. | — | [29] |
| 클래스(Class) | 캐릭터의 역할·특기·사용 능력에 규칙상 차이를 주는 직업 분류. | 외형이나 종족과 달리 행동과 능력 구성을 정한다. | 치유 클래스는 회복 주문을 사용할 수 있다. | 직업(Job)이 클래스에서 발전하는 별도 분류일 수도 있다. | [29], [30] |
| 빌드(Build) | 특정 목적을 위해 선택한 능력치·능력·장비 등의 조합. | 클래스 이름 하나보다 실제 선택의 구성을 가리킨다. | 방어 빌드는 체력과 피해 감소 능력에 투자한다. | [29]는 캐릭터 생성 선택; [31]은 경기 중 능력·아이템 구성. | [29], [31] |
| 기능 숙련(Proficiency) | 특정 무기·기술·도구·내성 판정을 잘 수행하도록 주어지는 규칙상 자격과 보정. | 플레이어의 실제 조작 숙련과 구별한다. | 도구 숙련이 있는 캐릭터는 잠금 해제 판정에 보너스를 더한다. | D&D 계열 용례이며 모든 RPG의 스킬을 뜻하지 않는다. | [29] |
| 클래스 특성(Class Feature) | 클래스 선택이나 클래스 레벨에 따라 얻는 고유 능력. | 일반 장비 효과와 달리 클래스 규칙에 귀속된다. | 클래스 특성으로 같은 행동에서 추가 공격을 수행한다. | — | [29] |
| 능력 수정치(Ability Modifier) | 능력치에서 산출해 관련 판정에 더하거나 빼는 보정값. | 능력치 원값과 판정에 쓰이는 값을 구별한다. | 공격 주사위에 힘 수정치를 더한다. | — | [29] |
| 최대 체력(Maximum HP) | 캐릭터가 보유할 수 있는 체력의 상한. | 현재 체력과 구별한다. | 회복 효과는 최대 체력을 넘겨 체력을 올리지 않는다. | — | [29] |
| 배경(Background) | 캐릭터의 이전 삶을 표현하면서 기술·도구 등 선택에 영향을 주는 설정. | 전투 직업인 클래스와 구별한다. | 학자 배경은 지식 기술 숙련을 제공한다. | 규칙 효과가 없는 서사 설정만인 작품도 있으므로 기능을 확인한다. | [29] |

<a id="gd-1-10-1"></a>
#### 1.10.1 액션 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 액션 RPG(Action RPG, ARPG) | 캐릭터 육성과 플레이어의 직접 이동·공격·능력 조작을 결합한 RPG. | 전투 명령을 차례별 메뉴로만 제출하는 턴제와 구별한다. | 이동과 회피를 직접 조작하면서 장비로 공격 능력을 강화한다. | — | [27] |

액션 RPG의 캐릭터 구성은 1.10의 **클래스·빌드·능력치(캐릭터)**, 적과의 행동 교환은 공용 사전의 **전투(combat)**를 참조한다.

<a id="gd-1-10-2"></a>
#### 1.10.2 턴제 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 턴제 RPG(Turn-Based RPG) | 캐릭터나 팀의 행동을 차례와 판정 단위로 해결하는 RPG. | 턴은 공용 시간 규칙이며 파티 규모와 별개다. | 각 캐릭터가 자신의 차례에 이동과 공격을 선택한다. | — | [27], [32] |
| 행동 순서(Initiative) | 전투 참가자가 행동하는 차례를 결정한 순서. | 행동 가능 횟수나 이동량과 구별한다. | 행동 순서가 앞선 캐릭터가 적보다 먼저 공격한다. | D&D에서는 주도권 판정으로 순서를 정한다. | [32] |
| 이동 속도(턴제 RPG, Speed) | 한 차례에 이동할 수 있는 거리의 기준값. | 초당 이동 속도와 구별한다. | 이동 속도만큼 이동한 뒤 추가 이동에는 별도 행동이 필요하다. | — | [32] |
| 험지(Difficult Terrain) | 통과할 때 평지보다 많은 이동량을 소비하는 지형. | 단순 통행 불가 지형과 구별한다. | 진흙 구간에서는 이동 거리에 추가 비용이 붙는다. | 비용 배율은 작품마다 다르다. | [32] |
| 반응 행동(Reaction) | 정해진 사건에 응답해 자신의 차례 밖에서도 수행할 수 있는 행동. | 차례에 자유롭게 선택하는 기본 행동과 구별한다. | 적이 사정거리 밖으로 나가면 반응 공격을 선택한다. | — | [32] |
| 보너스 행동(Bonus Action) | 특정 능력이나 규칙이 허용하는 추가 행동 단위. | 모든 상황에서 자유롭게 얻는 추가 턴이 아니다. | 특수 능력이 허용할 때만 보너스 행동으로 이동한다. | D&D 계열 행동 경제의 한 단위. | [32] |
| 준비 행동(Ready) | 먼저 조건과 대응 행동을 정해 두고 조건 발생 시 실행하는 행동. | 즉시 실행과 구별한다. | 문이 열리면 공격하도록 준비한다. | — | [32] |
| 기회 공격(Opportunity Attack) | 적의 이동 등 규칙상 빈틈을 계기로 허용되는 반응 공격. | 무조건 매 이동에 발생하는 자동 공격으로 일반화하지 않는다. | 적이 근접 사정거리를 벗어나면 기회 공격을 받는다. | 발동 조건과 면제 규칙은 작품별. | [32] |
| 공격 굴림(Attack Roll) | 명중 여부를 정하기 위해 주사위와 보정을 계산하는 판정. | 명중 뒤 피해량 굴림과 구별한다. | 공격 굴림이 방어 기준값을 넘으면 명중한다. | — | [32] |
| 방어도(Armor Class, AC) | 공격 굴림이 명중하기 위해 충족해야 하는 방어 기준값. | 피해량을 직접 차감하는 방어력과 다를 수 있다. | 높은 방어도는 공격의 명중을 어렵게 한다. | D&D 계열 정의이며 일반 RPG 방어력과 동의어가 아니다. | [32] |

<a id="gd-1-10-3"></a>
#### 1.10.3 전술 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 전술 RPG(Tactical RPG) | 캐릭터 육성과 팀의 배치·능력 조합·공격 계획을 중심 판단으로 결합하는 RPG. | 반드시 턴제일 필요는 없다. | 전투를 일시정지해 팀의 공격 순서와 능력 조합을 계획한다. | 실시간 일시정지 전술 RPG 용례도 있다. | [33] |
| 실시간 일시정지(RTWP) | 진행 중인 전투 시간을 멈춰 상황을 판단하고 명령을 계획하는 시간 방식. | 자동 차례 교대와 구별한다. | 시간을 멈추고 다음 공격 대상을 지정한다. | RPG와 전술에 공통 적용하는 방식이며 별도 장르로 고정하지 않는다. | [33] |

<a id="gd-1-10-4"></a>
#### 1.10.4 파티 기반 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 파티 기반 RPG(Party-Based RPG) | 여러 캐릭터를 하나의 모험 집단으로 구성하고 역할을 함께 운용하는 RPG. | 플레이어 인원과 통제 캐릭터 수는 별개다. | 한 플레이어가 세 캐릭터의 역할과 장비를 구성한다. | RPG 구조 속성이기도 하며 턴제·액션과 중첩한다. | [28], [34] |
| 파티(Party) | 함께 모험하거나 전투하는 캐릭터 집단. | 참가자 모두가 인간 플레이어일 필요는 없다. | 파티에는 플레이어 캐릭터와 동료 NPC가 함께 포함된다. | — | [28], [35] |

<a id="gd-1-10-5"></a>
#### 1.10.5 던전크롤러

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 던전크롤러(Dungeon Crawler) | 던전 탐색과 그 안의 반복 도전·전투를 중심으로 삼는 게임 양식. | 카메라 시점·턴제·RPG 여부를 한 가지로 고정하지 않는다. | 던전의 방을 탐색하며 전투와 위험을 넘는다. | 액션 던전크롤러라는 결합 용례도 있다. | [36] |
| 던전(던전크롤러) | 적·위험을 상대하며 탐색하는 구획과 경로로 이루어진 공간. | 공간과 게임 양식인 던전크롤러를 구별한다. | 던전 안의 위험을 넘겨 다음 구역으로 진행한다. | 절차생성·격자 이동·1인칭은 필수 조건이 아니다. | [36] |

<a id="gd-1-10-6"></a>
#### 1.10.6 방치 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 방치 RPG(Idle RPG) | 지속 입력이 적거나 접속하지 않은 동안에도 캐릭터의 전투·성장·획득이 진행되는 RPG. | 자동 전투 하나만 있는 RPG보다 방치 진행이 중심이다. | 재접속하면 자동 진행 중 얻은 전리품을 확인한다. | [27]은 로그오프 진행을 강조한다. | [27] |
| 방치 진행(Idle Progression, RPG) | 플레이어의 지속 조작 없이 캐릭터가 활동하고 성장·전리품 상태가 바뀌는 진행. | 화면상의 자동전투와 접속 밖 진행을 구별한다. | 접속하지 않은 동안 캐릭터가 얻은 전리품을 재접속 때 확인한다. | 일반 성장·전리품은 공용 사전 참조. | [27] |

<a id="gd-1-10-7"></a>
#### 1.10.7 MMORPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| MMORPG | 다수 플레이어가 동시에 공유 온라인 세계에서 캐릭터를 발전시키며 활동하는 RPG. | MMO 접속 규모에 RPG의 역할·성장 구조가 결합한다. | 공유 세계에서 다른 플레이어와 파티를 구성한다. | 특정 동시 인원 수를 보편 임계값으로 정하지 않는다. | [27] |
| 탱커(Tank) | 적의 주의를 유지하고 공격을 주로 받아 동료를 보호하는 전투 역할. | 단순히 체력이 높은 캐릭터와 구별한다. | 탱커는 적을 자신에게 묶어 후방 동료를 보호한다. | — | [30] |
| 힐러(Healer) | 동료의 체력을 회복하고 생존을 지원하는 전투 역할. | 회복 아이템을 한 번 쓰는 행동보다 지속 역할을 가리킨다. | 힐러는 부상한 파티원의 체력을 회복한다. | 피해 감소·해로운 상태 제거·부활을 겸하기도 한다. | [30] |
| 딜러(DPS 역할) | 적에게 피해를 주는 데 주된 책임을 갖는 전투 역할. | DPS 수치인 초당 피해량과 구별한다. | 근접 딜러는 위치와 공격 연계로 피해를 확보한다. | 같은 약어가 역할과 피해량 지표로 쓰인다. | [30] |
| 적개심(Enmity, Threat) | 적이 어느 캐릭터를 공격할지 결정하는 데 사용하는 주의·위협 수치. | 탐지 여부나 플레이어의 실제 적대 감정과 구별한다. | 공격과 회복이 적개심을 발생시킨다. | 어그로는 표적을 끌거나 표적이 된 상태를 넓게 가리키기도 한다. | [35] |
| 어그로 유지 | 자신이 적의 공격 대상으로 남도록 적개심을 관리하는 것. | 한 번 탐지되는 것과 구별한다. | 탱커는 적개심 생성 능력으로 어그로를 유지한다. | — | [35] |
| 시전 시간(Cast Time) | 주문 등 행동이 완료되기까지 필요한 시간. | 재사용 가능해질 때까지의 시간과 구별한다. | 시전 시간이 있는 주문은 즉시 효과를 내지 않는다. | — | [30], [35] |

<a id="gd-1-10-8"></a>
#### 1.10.8 JRPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| JRPG(Japanese RPG) | 일본 RPG의 역사와 그로부터 이어진 캐릭터·서사·전투 관습을 가리키는 명칭. | 제작국이나 턴제 여부만으로 판정하지 않는다. | 정해진 주인공들의 서사와 파티 전투를 결합한 JRPG 양식을 따른다. | 역사적으로 일본의 콘솔 RPG를 구별; 현재는 양식·영향을 뜻하기도 하며 경계는 논쟁적이다. | [37] |
| 고정 캐릭터(Preset Character) | 이름·성격·과거 등을 작가가 정해 둔 플레이 캐릭터. | 플레이어가 처음부터 설정하는 캐릭터와 구별한다. | 정해진 주인공들의 배경을 중심으로 이야기가 진행된다. | JRPG의 역사적 경향이며 필수 조건은 아니다. | [37] |

<a id="gd-1-10-9"></a>
#### 1.10.9 CRPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| CRPG(Computer RPG) | 컴퓨터 RPG의 역사에서 나온 명칭으로, 캐릭터 구성과 역할·선택을 강조하는 PC RPG 전통을 가리키기도 한다. | PC 출시 여부만으로 현재의 양식 용례를 판정하지 않는다. | 캐릭터를 직접 구성하고 역할에 맞는 선택으로 문제를 해결하는 CRPG 양식이다. | 문자적 뜻은 컴퓨터 RPG; 역사적 JRPG 대비에서는 PC 양식 RPG를 가리켰다. 현대 혼합으로 경계는 고정되지 않는다. | [37], [29] |
| 캐릭터 생성(Character Creation, RPG) | 클래스·능력치·배경 등 선택으로 플레이할 캐릭터를 구성하는 절차. | 진행 중 레벨 성장이나 단순 외형 선택과 구별한다. | 모험 전에 캐릭터의 역할과 능력을 구성한다. | CRPG의 역사적 경향이며 다른 RPG에도 적용된다. | [37], [29] |

<a id="gd-1-11"></a>
### 1.11 전략·전술

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 전략 게임(Strategy Game) | 자원·세력·부대의 운영과 계획으로 목표를 달성하는 게임. | 개별 행동의 실행과 장기 운영 판단을 함께 구별한다. | 자원 배분과 부대 확충 계획이 승패에 영향을 준다. | [38]의 시장 정의는 건물·군대·전쟁에 초점을 둔다. | [38] |
| 전술(Tactics) | 현재 전투·상황에서 배치와 행동 조합을 정하는 판단. | 장기 자원 운영·세력 확대 계획과 구별한다. | 적의 접근 방향에 맞춰 방어 부대를 배치한다. | — | [38], [33] |
| 4X 전략 | 탐험·확장·개발·적 세력 제압의 네 활동을 중심으로 세력을 운영하는 전략 양식. | 실시간·턴제 여부가 아니라 세력 운영 범위를 가리킨다. | 미지의 지역을 탐험하고 거점을 확장해 자원을 개발한다. | 네 X는 eXplore/eXpand/eXploit/eXterminate. | [38] |

4X의 세력 운용은 아래 RTS 용어 표의 **진영·유닛·정찰·매크로·빌드 오더**, 생산망은 1.13.1의 **생산 체인·처리량**, 자원·건설·생산 자체는 공용 사전을 참조한다. 이 연결은 4X를 실시간 전략으로 분류한다는 뜻이 아니다.

<a id="gd-1-11-1"></a>
#### 1.11.1 실시간 전략(RTS)

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| RTS(Real-Time Strategy) | 자원·경제·부대를 운용하며 양측 행동이 실시간으로 진행되는 전략 게임. | 순차적인 턴 제출과 구별한다. | 자원을 모으는 동안 전선의 부대도 계속 싸운다. | 일시정지가 가능한 싱글플레이도 존재한다. | [39] |
| 마이크로(Micro, Micromanagement) | 개별 유닛의 이동·공격·작업을 세밀하게 조작하는 것. | 생산·연구 등 전체 운영 계획인 매크로와 구별한다. | 부상 유닛을 물리고 공격 대상을 조정하는 마이크로가 필요하다. | 연구에서는 채집 등 개별 유닛 제어도 포함한다. | [40] |
| 매크로(Macro, Macromanagement) | 생산·연구·자원 등 전체 전황을 고려해 상위 운영 전략을 실행하는 것. | 개별 유닛의 즉각적인 행동 제어와 구별한다. | 경제와 생산 계획을 유지하는 매크로가 장기 병력 규모를 결정한다. | 입력 자동화 명령인 매크로와 다른 뜻이다. | [40] |
| 빌드 오더(Build Order) | 유닛 훈련·건물 건설·기술 연구 등을 수행하는 계획된 순서. | 캐릭터 능력 조합인 RPG 빌드와 구별한다. | 자원 확보 뒤 생산 시설과 연구를 잇는 빌드 오더를 사용한다. | — | [40] |
| 유닛(Unit, 전략) | 플레이어가 명령해 이동·전투·작업 등에 투입하는 개별 단위. | 고정 구조물과 구별하는 RTS 용례. | 유닛을 선택해 정찰과 공격 명령을 내린다. | 모든 장르의 유닛이 이동체인 것은 아니다. | [39] |
| 유닛 훈련(Train) | 자원과 생산 시설의 규칙을 통해 새로운 부대를 생성하는 것. | 기존 부대의 숙련 상승과 구별한다. | 자원을 지불해 보병을 훈련한다. | 생산의 범용 뜻은 공용 사전 참조. | [41], [39] |
| 인구 한도(Population Cap) | 현재 지원할 수 있는 유닛 수의 상한. | 보유 유닛 수와 구별한다. | 주거 시설을 늘리면 인구 한도가 증가한다. | — | [41] |
| 정찰(Scouting) | 유닛을 보내 지역·자원·적 행동에 관한 정보를 확보하는 것. | 단순 이동보다 정보 획득 목적에 초점을 둔다. | 기병을 보내 적의 새 생산 시설을 발견한다. | — | [41] |
| 전장의 안개(Fog of War) | 이미 탐험했지만 현재 관측하지 않는 구역의 최신 정보를 제한하는 규칙. | 아직 탐험하지 않은 미지 구역과 구별한다. | 정찰 유닛이 떠난 지역의 새 적 유닛은 보이지 않는다. | 표시 방식은 작품마다 다르다. | [41], [39] |
| 미탐험 구역(Shroud) | 아직 탐험하지 않아 지형·대상이 공개되지 않은 구역. | 과거에 본 지형이 남는 전장의 안개와 구별한다. | 정찰 전에는 미탐험 구역의 자원 위치를 알 수 없다. | — | [39] |
| 시야 범위(LOS, 전략) | 유닛이나 건물이 현재 정보를 관측할 수 있는 주변 영역. | 공격 사거리와 구별한다. | 시야가 긴 유닛을 앞세워 적 위치를 파악한다. | 기하학적 가시선 의미의 LOS와 구분해 읽는다. | [39] |
| 자원 반납 지점(Dropsite) | 일꾼이 운반한 자원을 저장·경제에 편입시키는 장소. | 채집 원천과 구별한다. | 일꾼은 운반 한도에 도달하면 반납 지점으로 돌아간다. | — | [41], [39] |
| 주둔(Garrison) | 유닛을 건물 안에 넣어 보호·방어에 사용하는 것. | 건물 주변 배치와 구별한다. | 일꾼을 주둔시키면 보호받지만 채집은 중단된다. | — | [41] |
| 태세(Stance) | 유닛이 발견·피격 등 상황에 자동으로 반응하는 행동 정책. | 개별 공격 명령과 구별한다. | 수비 태세의 부대는 짧게 추격한 뒤 원위치로 돌아간다. | — | [41] |
| 공성 유닛(Siege Unit) | 건물·방어 구조물 공격을 주된 용도로 삼는 부대. | 일반 전투 유닛과 목표 효율이 다르다. | 공성 유닛을 준비해 성벽을 공격한다. | — | [39] |
| 지원 유닛(Support Unit) | 직접 전투보다 회복·거래·경제 등의 지원 기능을 맡는 부대. | 전투 병종과 역할을 구별한다. | 지원 유닛을 보호해 전선의 보조 기능을 유지한다. | — | [39] |
| 진영(Faction, 전략) | 서로 다른 특성·유닛·구조물을 갖는 플레이 세력. | 같은 진영의 여러 플레이어 팀과 구별한다. | 진영마다 생산 가능한 부대 구성이 다르다. | 문명(Civilization)이라는 소재 명칭으로도 쓰인다. | [39] |

<a id="gd-1-11-2"></a>
#### 1.11.2 기지 건설 전투(Build & Battle)

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| Build & Battle | 기지를 발전시키고 자원을 생산해 부대를 구성한 뒤 배치·능력 사용으로 싸우는 전략 양식. | 모든 건설게임이 아니라 전투 준비와 운용이 결합한 형식. | 기지에서 부대를 준비한 뒤 적 방어에 맞춰 투입한다. | GameRefinery의 모바일 시장 분류명. | [38] |
| 부대 배치(Deployment) | 전투에 투입할 부대의 위치·투입 시점을 정하는 것. | 유닛 생산과 전투 실행을 구별한다. | 방어 시설의 사거리를 피해 부대를 배치한다. | — | [38] |

<a id="gd-1-12"></a>
### 1.12 시뮬레이션

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 시뮬레이션 게임 | 대상의 상태와 행동·반응을 모델화하여 조작·관찰·운영하게 하는 게임. | 현실 정확도를 자동으로 보증하지 않는다. | 생물과 환경의 반응을 바꾸며 세계를 운영한다. | [42]은 모바일 건설·작업 진행 중심의 협의 시장 분류다. | [42], [43] |

<a id="gd-1-12-1"></a>
#### 1.12.1 생활 시뮬레이션

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 생활 시뮬레이션(Life Simulation) | 인물의 일상·삶의 단계·욕구·관계를 관리하고 그 변화를 경험하는 양식. | 단일 작업 수행보다 지속적인 생활 상태를 다룬다. | 가족의 돌봄과 관계 변화가 생활 진행에 영향을 준다. | — | [44] |
| 욕구(생활) | 생활 주체가 충족하려는 돌봄·휴식 등 필요 상태. | 감정이나 성격과 구별한다. | 보호자는 아이의 욕구를 돌보면서 자신의 휴식도 관리한다. | 구체 욕구 목록·수치는 작품별. | [44] |
| 인생 단계(Life Stage) | 나이에 따라 행동·능력·돌봄 요구가 달라지는 생애 구간. | 공용 캐릭터 레벨과 구별한다. | 영아 단계에서 성장하면 새로운 상호작용이 가능해진다. | — | [44] |
| 성향(Quirk) | 인물의 특정 행동 방식에 차이를 주는 개별 성질. | 현재 욕구·기분과 구별한다. | 수면 성향에 따라 돌봄 일정이 달라진다. | — | [44] |
| 생활 이정표(Milestone) | 삶의 경험·관계·발달에서 달성하거나 겪은 주요 사건의 기록. | 점수 목표나 레벨 상승만을 뜻하지 않는다. | 새로운 경험이 이정표로 남아 이후 행동에 영향을 준다. | — | [44] |
| 사교적 상성(Social Compatibility) | 인물의 선호 조합에 따라 관계 형성의 잘 맞음·맞지 않음이 달라지는 상태. | 이미 쌓인 친밀도와 구별한다. | 상성이 좋은 인물끼리는 친구가 되기 쉽다. | — | [44] |
| 가족 관계성(Family Dynamics) | 가족 구성원 간 상호작용 방식에 영향을 주는 관계의 성격. | 가계도상 혈연 연결만과 구별한다. | 경쟁적인 관계성은 가족의 사교 행동을 바꾼다. | — | [44] |

<a id="gd-1-12-2"></a>
#### 1.12.2 농업·동물돌봄·번식

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 농업 시뮬레이션(Farming Simulation) | 작물 재배와 농장 운영·가축 돌봄을 주요 활동으로 삼는 양식. | 농업 소재의 존재보다 재배·운영 규칙이 중심이다. | 작물의 성장 기간과 계절을 고려해 파종한다. | — | [45], [46] |
| 작물(Crop) | 씨앗에서 재배해 수확하는 농업 대상. | 자연에서 바로 줍는 채집물과 구별한다. | 작물을 수확해 판매하거나 식재료로 쓴다. | — | [46] |
| 경작(Tilling) | 씨앗·비료를 놓을 수 있게 땅을 준비하는 작업. | 씨앗을 심는 파종과 구별한다. | 경작한 칸에 씨앗을 심는다. | — | [46] |
| 파종(Planting) | 준비된 땅에 씨앗을 심어 재배를 시작하는 것. | 성장 완료 뒤 산출물을 얻는 수확과 구별한다. | 계절이 끝나기 전에 익을 작물을 파종한다. | — | [46] |
| 관수(Watering) | 재배 칸에 물을 공급하는 것. | 비료 적용이나 파종과 구별한다. | 물을 주지 않은 날에는 작물 성장이 멈춘다. | 성장 정지·고사는 작품별 다른 규칙. | [46] |
| 성장 기간(Grow Time) | 파종 후 수확 가능 상태까지 필요한 시간. | 반복 수확의 재성장 기간과 구별한다. | 성장 기간이 긴 작물은 계절 종료를 고려해 심는다. | 날짜 포함 방식은 작품별. | [46] |
| 재성장 기간(Regrow Time) | 한 번 수확한 반복 생산 작물이 다음 수확까지 요구하는 시간. | 최초 성장 기간과 구별한다. | 첫 수확 뒤에는 재성장 기간마다 다시 수확한다. | — | [46] |
| 수확(Harvest) | 성장한 작물에서 생산물을 거두는 것. | 제작이나 판매와 구별한다. | 수확한 작물의 품질에 따라 판매값이 달라진다. | — | [45], [46] |
| 작물 품질(Crop Quality) | 수확물의 가치·효과 차이를 나타내는 등급. | 작물 종류와 별개다. | 비료와 농업 능력이 높은 품질의 확률을 바꾼다. | — | [45], [46] |
| 계절성(작물) | 특정 계절에만 심거나 성장·생존할 수 있는 성질. | 단순 시각적 날씨 변화와 구별한다. | 계절이 바뀌면 맞지 않는 작물은 시든다. | — | [46] |
| 지지대 작물(Trellis Crop) | 지지 구조가 있어 이동을 가로막는 재배 대상. | 일반 작물과 달리 수확 접근 경로가 중요하다. | 안쪽 작물에도 접근하도록 재배 간격을 둔다. | — | [46] |
| 동물돌봄 게임 | 동물의 돌봄·상태·생산 또는 관계를 주요 활동으로 다루는 양식. | 동물 조작 액션이나 동물 소재만과 구별한다. | 동물을 쓰다듬고 생산물을 거두는 돌봄을 반복한다. | 농장 시뮬레이션과 중첩할 수 있다. | [45] |
| 번식 게임(Breeding Game) | 기존 생물·캐릭터를 짝지어 새로운 개체를 얻는 규칙이 중심인 양식. | 단순 획득·소환과 구별한다. | 두 개체를 번식시켜 새로운 종류를 얻는다. | — | [42] |
| 부화 기간(Incubation Time) | 알 등에서 새 개체가 나오기까지 걸리는 시간. | 부모의 관계 형성 기간과 구별한다. | 부화 기간이 끝나면 새 동물을 돌볼 수 있다. | — | [45] |

<a id="gd-1-12-3"></a>
#### 1.12.3 갓 게임

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 갓 게임(God Game) | 초월적 능력으로 지형·자원·세계와 주민에 영향을 주는 양식. | 주민을 하나씩 직접 명령하는 경영과 통제 범위를 구별한다. | 지형과 자원에 개입해 주민의 생활 조건을 바꾼다. | 직접 통제의 허용 범위는 작품마다 다르다. | [43] |
| 간접 통제(갓 게임) | 환경·자원을 바꿔 자율 행위자의 행동에 영향을 주는 것. | 행위자에게 직접 행동 명령을 주는 것과 구별한다. | 자원을 배치해 주민이 정착할 조건을 만든다. | — | [43] |

<a id="gd-1-13"></a>
### 1.13 건설·경영·자동화

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 건설·경영 게임 | 시설·공간을 구성하고 자원·운영 상태를 관리해 발전시키는 양식. | 건설은 공용 사전의 배치·구축, 경영은 운영 판단을 가리킨다. | 시설 배치와 자원 배분으로 운영을 개선한다. | — | [42] |
| 타이쿤(Tycoon) | 사업·도시·농장 등 운영 대상의 규모와 성과를 발전시키는 경영 양식. | 운영 대상에 따라 다른 규칙을 갖는 넓은 관습명. | 자원과 생산을 관리해 사업 규모를 키운다. | GameRefinery는 도시·농장 경영도 포함한다. | [42] |

<a id="gd-1-13-1"></a>
#### 1.13.1 공장·생산·물류 자동화

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 공장 자동화 게임(Factory Automation) | 원료 확보·운송·가공을 연결해 자동 생산 체계를 구성하는 양식. | 수동 제작 기능 하나보다 생산망 설계가 중심이다. | 원료 채굴과 가공을 벨트로 연결해 자동화한다. | — | [47] |
| 생산 체인(Production Chain) | 한 단계의 산출물이 다음 단계의 입력이 되는 연결 구조. | 단일 생산법과 구별한다. | 채굴한 원료를 운송해 중간재와 완제품으로 가공한다. | 생산의 범용 뜻은 공용 사전 참조. | [47] |
| 처리량(Throughput) | 일정 시간에 통과하거나 완료되는 산출량. | 이동 속도·저장량·명목 용량과 구별한다. | 운송 처리량을 초당 아이템 수로 비교한다. | 벨트에서는 속도와 적재 밀도의 곱으로 설명한다. | [48] |
| 병목(Bottleneck) | 연결된 흐름의 처리량을 제한하는 구간. | 상류 재고 증가라는 증상과 제한 원인을 구별한다. | 느린 분배기가 전체 운송망의 병목이 된다. | — | [48] |
| 벨트(Transport Belt) | 아이템을 연결된 경로를 따라 연속 운송하는 설비. | 저장함이나 순간 이동 운송과 구별한다. | 벨트로 원료를 가공 시설까지 운반한다. | — | [48] |
| 벨트 레인(Lane) | 벨트 안에서 아이템 흐름을 나누는 개별 줄. | 맵의 전투 레인과 구별한다. | 두 레인에 서로 다른 재료를 실어 보낸다. | — | [48] |
| 적재 밀도(Density) | 운송 공간에 아이템이 얼마나 촘촘히 채워져 있는지 나타내는 값. | 벨트 이동 속도와 구별한다. | 빈틈을 줄이면 같은 속도에서도 처리량이 증가한다. | — | [48] |
| 분배기(Splitter) | 입력 아이템을 여러 출력 경로로 나누거나 합치는 설비. | 아이템 종류를 바꾸는 가공 시설과 구별한다. | 분배기로 원료를 두 생산 라인에 나눈다. | — | [48] |
| 운송 필터(Filter) | 지정한 아이템만 특정 출력·경로로 보내는 설정. | 입력량을 균등하게 나누는 분배와 구별한다. | 금속 원료만 지정 출력으로 보낸다. | — | [48] |
| 입출력 우선순위(Priority) | 여러 입력·출력 중 먼저 사용할 경로를 지정하는 설정. | 필터는 종류, 우선순위는 처리 순서를 지정한다. | 우선 출력이 가득 차면 보조 출력으로 보낸다. | — | [48] |
| 밸런서(Balancer) | 여러 운송 경로나 레인에 아이템을 고르게 분산하는 구성. | 가장 빠른 단일 운송 경로와 구별한다. | 밸런서로 생산 라인의 공급 편중을 줄인다. | — | [48] |
| 지하 벨트(Underground Belt) | 다른 흐름·설비 아래를 통과해 입구와 출구를 잇는 운송 설비. | 서로 교차하는 흐름을 섞지 않는다. | 지하 벨트로 두 물류 경로를 교차시킨다. | — | [48] |
| 회로 조건(Circuit Condition) | 물류·설비에서 신호를 기준으로 동작 여부 등을 결정하는 논리 조건. | 플레이어의 수동 켜기·끄기와 구별한다. | 감지한 아이템 수에 따라 벨트 가동을 제어한다. | — | [48] |
| 청사진(Blueprint) | 시설 배치를 기록해 다시 배치·건설할 때 재사용하는 설계 데이터. | 완성 시설 자체나 제작법과 구별한다. | 검증한 생산 라인을 청사진으로 반복 배치한다. | — | [47] |

<a id="gd-1-13-2"></a>
#### 1.13.2 시간관리

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 시간관리 게임(Time Management) | 여러 작업을 빠르고 정확하며 적절한 순서로 수행하는 양식. | 단순 대기 타이머가 있는 모든 경영게임을 뜻하지 않는다. | 준비와 제공 작업의 순서를 정해 요청을 처리한다. | — | [42] |

시간관리의 작업 실행과 허용 순서는 공용 사전의 **행동(action)·조건(condition)·제약(constraint)·비용(cost)**, 완료 흐름은 1.13.1의 **처리량·병목**을 참조한다.

<a id="gd-1-13-3"></a>
#### 1.13.3 스포츠매니저

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 스포츠매니저(Sports Management) | 선수·팀의 훈련·전술·운영을 관리하는 양식. | 경기 중 선수 직접 조작과 구별한다. | 주간 훈련과 팀 전술을 조정한다. | — | [49] |
| 훈련 일정(팀 경영) | 기간별 훈련 작업과 배분을 정한 계획. | 경기 중 행동 명령과 구별한다. | 다음 경기를 준비하도록 주간 훈련을 배분한다. | — | [49] |
| 훈련 유닛(Training Unit) | 훈련 계획에서 선수들을 묶는 관리 집단. | 전략게임의 개별 유닛과 구별한다. | 선수들을 훈련 유닛으로 나누어 계획을 조정한다. | — | [49] |

<a id="gd-1-14"></a>
### 1.14 스포츠·운동

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 스포츠 게임(Sports Game) | 스포츠 경기나 스포츠의 동작·경쟁을 주요 플레이로 삼는 게임. | 팀 경영만을 다루는 스포츠매니저와 구별한다. | 선수의 동작을 조작해 경기 목표를 달성한다. | 종목·재현 정도·입력 방식은 별도 축이다. | [50] |
| 아케이드 스포츠(Arcade Sports) | 스포츠 규칙·물리를 간략화하거나 변형해 직접 플레이를 구성한 양식. | 현실 종목의 충실한 재현 지향과 구별한다. | 과장된 공의 움직임과 간략한 판정으로 경기를 진행한다. | 쉬운 난도나 실제 오락실 매체를 뜻하지 않는다. | [50] |
| 스포츠 시뮬레이션(Realistic Sports) | 실제 종목의 규칙·물리·경기 표현을 재현하려는 스포츠 양식. | 재현 지향과 실측 정확도는 별개다. | 실제 종목의 경기 규칙을 반영해 반칙을 판정한다. | — | [50] |

<a id="gd-1-14-1"></a>
#### 1.14.1 농구 규칙을 사용하는 팀 스포츠

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 팀 스포츠 게임 | 팀의 선수들이 역할을 나누어 공동 득점·승리를 추구하는 스포츠 게임. | 플레이어 인원과 팀 선수 수는 별개다. | 조작 선수와 동료 선수들이 함께 공격을 구성한다. | 종목에 따른 묶음이며 모든 팀 스포츠가 같은 판정을 쓰지는 않는다. | [51] |
| 드리블(농구) | 공을 바닥으로 던지거나 두드려 이동시키면서 통제하는 행동. | 공을 잡고 이동하는 것과 구별한다. | 이동 중 드리블을 유지하다 패스를 선택한다. | — | [51] |
| 피벗(Pivot, 농구) | 한 발을 축으로 바닥에 유지하며 다른 발로 방향을 바꾸는 동작. | 자유 이동과 구별한다. | 공을 잡은 선수는 축발을 유지해 피벗한다. | — | [51] |
| 트래블링(Traveling) | 공을 보유한 상태에서 허용된 발 이동 규칙을 위반하는 것. | 정당한 드리블 이동과 구별한다. | 허용 범위를 넘는 발 이동은 트래블링으로 판정한다. | — | [51] |
| 스크린(Screen, 농구) | 불필요한 접촉 없이 상대가 원하는 위치로 가는 것을 지연·제한하는 동작. | 반칙이 되는 불법 접촉과 구별한다. | 동료가 스크린으로 수비 이동을 지연시킨다. | — | [51] |
| 개인 파울(Personal Foul) | 상대와의 불법적인 신체 접촉으로 발생하는 반칙. | 비신사적 행위에 대한 테크니컬 파울과 구별한다. | 불법 접촉이 개인 파울로 판정된다. | — | [51] |
| 테크니컬 파울(Technical Foul) | 비신사적 행위나 팀원의 특정 규칙 위반에 부과하는 파울. | 통상적인 경기 중 접촉 반칙과 구별한다. | 비신사적 행동에 테크니컬 파울을 부과한다. | — | [51] |
| 자유투(Free Throw) | 정해진 위치에서 방해 없이 득점을 시도하는 슛 기회. | 일반 플레이 중 슛과 구별한다. | 자유투 기회에 정해진 위치에서 슛을 시도한다. | — | [51] |
| 스로인(Throw-In, 농구) | 경계 밖에서 공을 안으로 넣어 플레이를 재개하는 방법. | 자유투나 경기 중 패스와 구별한다. | 공이 나가면 지정 선수의 스로인으로 재개한다. | — | [51] |

<a id="gd-1-15"></a>
### 1.15 레이싱

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 레이싱(Racing) | 경주 순위·기록 경쟁이나 경주 중심의 행동을 주요 플레이로 삼는 양식. | 운전 자체를 재현하는 모든 게임을 뜻하지 않는다. | 정해진 코스를 달려 가장 먼저 결승점을 통과한다. | — | [52] |
| 아케이드 레이싱 | 현실 물리의 충실한 재현보다 변형·과장된 주행 규칙을 사용하는 레이싱 양식. | 난도보다 주행 모델의 성격을 가리킨다. | 후방 차량의 가속 보조로 순위 경쟁을 압축한다. | — | [52], [53] |
| 시뮬레이션 레이싱(Sim Racing) | 차량 물리와 주행 조건의 현실 재현을 지향하는 레이싱 양식. | 소개상의 지향과 실제 정확도를 구별한다. | 타이어 상태와 연료를 고려해 주행과 정비를 계획한다. | — | [52], [53] |

<a id="gd-1-15-terms"></a>
#### 공통 용어: 주행·레이스·정비

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 랩(Lap) | 코스를 한 바퀴 완주하는 경주 단위. | 경기 전체나 부분 구간과 구별한다. | 마지막 랩을 마치면 경기가 끝난다. | — | [53] |
| 그리드(Grid) | 출발을 위해 차량이 정렬하는 위치·순서. | 현재 주행 순위와 구별한다. | 사전 기록에 따라 그리드를 정한다. | — | [53] |
| 정지 출발(Grid Start) | 차량이 멈춘 출발 위치에서 경주를 시작하는 방식. | 이미 움직이며 시작하는 롤링 스타트와 구별한다. | 출발 신호 전 움직이면 부정 출발로 판정한다. | — | [53] |
| 롤링 스타트(Rolling Start) | 차량들이 이동 중인 상태에서 경주를 시작하는 방식. | 정지 출발과 구별한다. | 차량들이 달리는 상태로 출발 구간을 통과한다. | — | [53] |
| 슬립스트림(Slipstream) | 앞 차량 뒤에서 공기 저항이 줄어 추격에 유리해지는 효과. | 임의 가속 보조인 부스트와 구별한다. | 앞 차량 뒤에 붙어 슬립스트림으로 속도를 확보한다. | 다운포스 감소를 함께 모델링하기도 한다. | [53] |
| 부스트(레이스 보조) | 뒤처진 차량에 속도 이점을 주어 경쟁 간격을 줄이는 보조. | 차량별 소비형 니트로와 반드시 같은 규칙은 아니다. | 후방 차량의 속도를 보정하는 부스트를 사용한다. | 게임마다 Boost는 능력·소모 가속을 뜻하기도 한다. | [53] |
| 성능 균형(BoP) | 차종 간 경쟁 성능을 맞추기 위해 무게·출력 등을 조절하는 규칙. | 플레이어 실력을 맞추는 매칭과 구별한다. | BoP 규칙으로 참가 차량의 무게와 출력을 조정한다. | — | [53] |
| 타이어 마모(Tyre Wear) | 사용에 따라 타이어 상태가 나빠지고 접지력이 줄어드는 변화. | 외형 손상과 구별한다. | 마모된 타이어를 바꾸기 위해 피트에 들어간다. | — | [53], [54] |
| 접지력(Grip) | 타이어가 노면과 접촉해 주행력을 유지하는 성질. | 엔진 출력이나 최고 속도와 구별한다. | 코스 밖에서는 접지력이 감소한다. | — | [53] |
| 연료 소비(Fuel Consumption) | 주행 중 연료 보유량이 감소하는 규칙. | 시작 연료와 소비 속도는 별개다. | 남은 연료에 맞춰 가속과 정비 시점을 조정한다. | — | [53] |
| 기계적 손상(Mechanical Damage) | 충돌 등이 엔진·서스펜션 같은 주행 기능을 저하시키는 상태. | 보이는 외형 손상과 구별한다. | 기계적 손상으로 직진과 가속이 어려워진다. | — | [53] |
| 피트스톱(Pit Stop) | 경주 중 피트에서 타이어 교환·급유·수리를 하는 정비 과정. | 일반 경주 일시정지와 구별한다. | 타이어 교환과 급유를 한 번의 피트스톱에서 수행한다. | — | [54] |
| 피트 레인(Pit Lane) | 주행 코스와 피트 정비를 연결하는 진입·이탈 경로. | 코스 주행 경로와 구별한다. | 피트 레인 진입선 위반을 페널티로 처리한다. | — | [54] |
| 의무 타이어(Mandatory Tyre) | 경기 규정에 따라 반드시 사용해야 하는 타이어 종류. | 단순 권장 선택과 구별한다. | 의무 타이어 조건을 충족하도록 정비 계획을 세운다. | — | [54] |

<a id="gd-1-16"></a>
### 1.16 음악·리듬

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 음악·리듬 게임 | 음악의 박자·동작 대응을 주요 과제로 삼거나 음악으로 플레이 콘텐츠를 구성하는 양식. | 배경음악이 있다는 이유만으로 판정하지 않는다. | 음악의 박자에 맞춰 회전과 탭 입력을 수행한다. | 리듬 판정·음악 생성·음악 기반 콘텐츠 생성은 서로 다른 기능. | [55], [56] |

<a id="gd-1-16-1"></a>
#### 1.16.1 노트 판정형 리듬

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 노트 판정형 리듬 게임 | 정해진 시점의 노트에 대응하는 입력을 평가하는 리듬 양식. | 곡을 재생하거나 생성하는 기능만과 구별한다. | 각 노트의 기준 시점에 맞춰 키를 누른다. | — | [57] |
| 노트(Note) | 정해진 시점·입력 요구를 갖는 판정 대상. | 실제 연주 음표와 일대일 대응한다고 가정하지 않는다. | 노트를 제때 누르면 판정 등급을 얻는다. | — | [57] |
| 판정(Judgement, 리듬) | 노트에 대한 입력 결과를 시간 정확도 등으로 평가한 등급. | 점수·정확도는 이 판정들에서 계산하는 결과값이다. | 늦은 입력은 낮은 판정으로 기록한다. | — | [57] |
| 판정창(Hit Window) | 특정 노트 입력을 유효하게 받아들이거나 등급을 부여하는 시간 범위. | 화면에 노트가 보이는 기간과 구별한다. | 판정창 밖의 입력은 노트를 처리하지 못한다. | 앞·뒤 범위와 등급 경계는 작품별. | [57] |
| 시간 오차(Hit Error) | 입력 시점과 노트 기준 시점 사이의 시간 차이. | 곡 재생 지연이나 단순 점수 손실과 구별한다. | 입력의 시간 오차를 밀리초로 측정한다. | — | [57] |
| 롱노트(Hold Note) | 시작 입력 후 일정 구간 동안 입력을 유지하는 판정 대상. | 단발 노트와 달리 유지·해제 규칙이 있다. | 롱노트의 시작을 누르고 끝까지 유지한다. | 시작·종료를 합쳐 판정하거나 별도로 판정한다. | [57] |
| 롱노트 머리(Head) | 롱노트의 시작 입력을 요구하는 부분. | 종료 해제를 요구하는 꼬리와 구별한다. | 머리 시점에 키를 눌러 유지 판정을 시작한다. | — | [57] |
| 롱노트 꼬리(Tail) | 롱노트의 종료·입력 해제에 대응하는 부분. | 시작 입력 시점과 구별한다. | 꼬리에서의 해제 오차도 결과에 반영한다. | — | [57] |
| 미스(Miss, 리듬) | 요구 입력을 처리하지 못한 실패 판정. | 낮은 성공 판정과 구별한다. | 노트를 누르지 않으면 미스로 처리한다. | — | [57] |
| 정확도(Accuracy, 리듬) | 받은 판정의 품질을 종합해 입력 수행을 나타내는 지표. | 성공 노트 수나 총점과 반드시 같지는 않다. | 같은 완주라도 판정 분포에 따라 정확도가 달라진다. | 산식은 작품별. | [57] |

<a id="gd-1-16-terms"></a>
#### 기능 용어: 음악 기반 생성·편집

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 음악 기반 콘텐츠 생성 | 음악 데이터의 특성에 따라 주행 경로 등 플레이 콘텐츠를 만드는 기능. | 결과물이 음악인 작곡·음악 생성과 구별한다. | 선택한 곡이 플레이 경로의 형태를 바꾼다. | 독립된 보편 하위 장르가 아니라 생성 기능. | [56] |
| 리듬 레벨 편집 | 곡에 맞춘 입력 과제·배치 등을 제작하는 기능. | 플레이 중 노트 입력이나 음악 작곡과 구별한다. | 편집기로 곡의 리듬 과제를 제작한다. | — | [55] |

<a id="gd-1-17"></a>
### 1.17 카드·덱

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 카드 게임(Card Game) | 카드를 주요 정보·행동·조합 대상으로 사용하는 게임. | 카드가 UI로 표시될 뿐인 게임과 규칙 역할을 구별한다. | 카드를 뽑고 사용해 행동을 결정한다. | [58]의 Card Games는 수집형 대전 카드배틀러에 한정한 시장 분류. | [58], [59], [60] |
| 덱(Deck) | 플레이에 사용하는 카드의 묶음. | 사용 가능한 모든 카드의 풀이나 현재 패와 구별한다. | 덱을 섞은 뒤 일부 카드를 뽑는다. | — | [59] |
| 패(Hand) | 현재 보유하며 사용·선택할 수 있는 카드 집합. | 덱의 미공개 카드 묶음과 구별한다. | 패에서 비용을 낼 수 있는 카드를 선택한다. | 솔리테어의 Hand는 Stock 별칭이므로 의미가 다르다. | [59], [60] |
| 드로우(Draw) | 덱·서고에서 카드를 가져와 패 등 지정 위치에 넣는 것. | 카드를 영구 소유하는 획득과 구별한다. | 차례가 시작되면 카드를 한 장 드로우한다. | — | [59] |

<a id="gd-1-17-1"></a>
#### 1.17.1 카드배틀러·수집카드

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 카드배틀러(Card Battler) | 덱과 카드 효과로 상대·적과 전투하는 양식. | 카드 정리 퍼즐이나 전통 트릭게임과 구별한다. | 카드 효과를 조합해 적의 체력을 줄인다. | [58]은 턴제 PvP·수집을 강조하는 협의 시장 정의. | [58], [59] |
| 수집카드 게임(TCG) | 서로 다른 카드들을 수집해 선택한 카드 구성으로 플레이하는 형식. | 정해진 한 벌만 사용하는 전통카드와 구별한다. | 보유 카드 중에서 전투 덱을 구성한다. | TCG의 거래 가능 여부와 디지털 컬렉션 규칙은 작품별. | [59], [61] |
| 덱 구성(Deck Construction) | 시작 전 사용할 카드 묶음을 카드 풀·포맷 조건에 맞게 정하는 것. | 플레이 중 덱이 발전하는 덱빌딩과 구별한다. | 경기 전에 카드 풀에서 덱을 구성한다. | — | [61] |
| 카드 풀(Card Pool) | 특정 구성·선택 상황에서 사용할 수 있는 카드의 전체 범위. | 실제 선택한 덱이나 소유 컬렉션과 구별한다. | 제한된 카드 풀에서 덱에 넣을 카드를 고른다. | 사용 허가와 소유가 일치하지 않을 수 있다. | [61] |
| 드래프트(Draft) | 제공되는 카드 후보에서 순차적으로 카드를 선택해 구성 재료를 확보하는 절차. | 보유 카드 전체에서 자유롭게 구성하는 방식과 구별한다. | 드래프트에서 고른 카드로 이후 경기용 덱을 만든다. | 카드의 영구 귀속은 포맷별로 다르다. | [61] |
| 포맷(Format, 카드) | 허용 카드·덱 조건·플레이 방식 등을 정한 규칙 묶음. | 개별 경기 결과나 카드 효과와 구별한다. | 선택한 포맷에 따라 사용할 수 있는 카드가 달라진다. | — | [61] |
| 멀리건(Mulligan) | 시작 패를 받아들일지 판단해 정해진 규칙으로 다시 준비하는 절차. | 일반 차례의 드로우와 구별한다. | 시작 패가 맞지 않으면 멀리건을 선택한다. | 카드 수·불이익·재선택 방식은 작품별. | [59] |
| 카드 비용(Cost) | 카드를 사용하기 위해 지불해야 하는 자원 조건. | 카드의 공격력·효과량과 구별한다. | 마나가 부족한 카드는 사용할 수 없다. | — | [59] |
| 마나(Mana, 카드) | 주문·카드의 사용 비용을 지불하는 자원. | 카드게임에서의 자원 의미와 RPG 상태량을 구별한다. | 자원 카드를 사용해 마나를 만든다. | — | [59] |
| 서고(Library) | 아직 뽑지 않은 덱 카드가 놓이는 구역. | 손패·무덤과 구별한다. | 서고에서 카드를 뽑아 패에 넣는다. | MTG의 구역명. | [59] |
| 전장(Battlefield, 카드) | 사용 뒤 지속되는 카드 등이 놓이는 활성 구역. | 즉시 해결 후 버려지는 구역과 구별한다. | 소환한 지속 카드가 전장에 남는다. | — | [59] |
| 무덤(Graveyard) | 해결된 일회 주문·파괴된 카드 등이 가는 구역. | 영구 컬렉션 삭제와 구별한다. | 일회 주문은 효과를 해결한 뒤 무덤으로 간다. | 일반 버림 더미와 접근·재사용 규칙이 다를 수 있다. | [59] |
| 탭(Tap) | 카드를 가로로 돌려 사용·소모 상태를 표시하는 조작. | 카드를 버리거나 파괴하는 것과 구별한다. | 자원 카드를 탭해 마나를 생성한다. | — | [59] |
| 언탭(Untap) | 탭 상태의 카드를 되돌려 다시 사용할 상태로 만드는 것. | 새 카드 획득과 구별한다. | 차례 시작에 카드를 언탭한다. | — | [59] |
| 공격자 선언 | 해당 전투에서 공격할 카드·유닛을 지정하는 단계. | 실제 피해 계산과 구별한다. | 공격자를 지정한 뒤 방어자가 대응한다. | — | [59] |
| 방어자 선언 | 공격을 막을 카드·유닛을 지정하는 단계. | 공격을 무조건 취소시키는 효과와 구별한다. | 방어 유닛을 지정해 해당 공격을 막는다. | — | [59] |

<a id="gd-1-17-2"></a>
#### 1.17.2 덱빌딩 게임

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 덱빌딩 게임(Deck-Building Game) | 플레이 진행 중 카드 묶음을 변화·발전시키는 결정이 중심인 양식. | 경기 전 덱 구성과 구별한다. | 처음의 작은 덱을 진행하면서 강화한다. | — | [62] |
| 덱빌딩(Deck Building, 진행 중) | 플레이 중 카드 획득·변경으로 자신의 덱을 발전시키는 과정. | 정적 경기 전 구성과 구별한다. | 새 행동 카드를 추가해 덱의 선택지를 늘린다. | — | [62] |

덱빌딩의 카드 보유·이동은 1.17의 **덱·패·드로우**, 사용 자원은 1.17.1의 **카드 비용·마나**, 시작 전 선택 절차는 **덱 구성·카드 풀·드래프트**를 참조한다. **무덤**은 특정 카드전투의 구역명으로, 덱빌딩의 버림·폐기 규칙과 자동으로 동일시하지 않는다.

<a id="gd-1-17-3"></a>
#### 1.17.3 솔리테어

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 솔리테어(Solitaire, Patience) | 혼자 카드 배열을 규칙에 맞게 정리·이동해 목표 상태를 만드는 카드 형식. | 하나의 배치만이 아니라 여러 변형을 포함한다. | 카드를 이동해 목표 더미를 완성한다. | — | [60] |
| 타블로(Tableau, 솔리테어) | 카드를 배치·이동하는 주요 카드 더미 영역. | 완성 목표인 파운데이션과 구별한다. | 타블로의 카드를 옮겨 아래 카드를 공개한다. | — | [60] |
| 파운데이션(Foundation) | 정해진 무늬·순서대로 카드를 쌓아 완성하는 목표 더미. | 임시 작업 배열과 구별한다. | 같은 무늬의 카드를 순서대로 파운데이션에 쌓는다. | — | [60] |
| 스톡(Stock) | 처음 배열에 쓰지 않고 남겨 두어 이후 공급하는 카드 더미. | 이미 공개한 웨이스트와 구별한다. | 이동할 카드가 없으면 스톡에서 새 카드를 공개한다. | Hand라는 별칭은 보통 손패와 다른 뜻이다. | [60] |
| 웨이스트(Waste, Talon) | 스톡에서 공개했지만 다른 더미에 놓지 않은 카드가 모이는 더미. | 카드를 게임에서 완전히 제거하는 폐기와 구별한다. | 놓을 수 없는 공개 카드는 웨이스트로 보낸다. | — | [60] |

<a id="gd-1-18"></a>
### 1.18 보드·테이블탑

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 보드게임(Board Game) | 판·말·카드 등 구성물의 상태와 행동 규칙으로 플레이하는 형식. | 디지털 전환 여부와 구성물 역할은 별개다. | 디지털 판에서 말을 움직여 위치 규칙을 적용한다. | 모바일 시장에서는 전통 보드 형식과 그 메커니즘을 사용하는 변형도 묶는다. | [63], [64] |
| 테이블탑(Tabletop) | 테이블 위 구성물이나 그 재현을 통해 플레이하는 형식의 넓은 명칭. | 보드게임 외 카드·미니어처·TRPG도 포함할 수 있다. | 참가자가 가상 테이블에서 구성물을 조작한다. | 디지털 플랫폼은 규칙 강제 여부가 별도다. | [28], [64] |

<a id="gd-1-18-1"></a>
#### 1.18.1 체스

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 체스(Chess) | 두 진영이 번갈아 말을 움직여 상대 왕의 체크메이트를 목표로 하는 보드게임. | 상대 왕을 실제로 잡는 게임으로 설명하지 않는다. | 상대 왕이 공격받고 합법 대응이 없으면 승리한다. | — | [65] |
| 말(Piece, 체스) | 판에서 위치와 고유 이동 규칙을 갖는 구성물. | 칸이나 점수 토큰과 구별한다. | 말의 종류에 따라 가능한 이동이 다르다. | — | [65] |
| 수(Move, 체스) | 자신의 차례에 규칙에 따라 말을 움직여 판 상태를 바꾸는 단위. | 한 경기나 양측 차례 묶음과 구별한다. | 합법 수만 선택할 수 있다. | — | [65] |
| 포획(Capture, 체스) | 규칙에 따라 상대 말을 판에서 제거하는 것. | 일반 포획은 상대 말의 칸으로 이동하지만 앙파상은 다른 칸에 도착한다. | 상대 폰의 두 칸 전진 직후 앙파상으로 그 폰을 제거한다. | 왕은 포획하지 않고 체크메이트로 승패를 정한다. | [65] |
| 체크(체스, Check) | 자신의 왕이 상대 말의 공격을 받고 있는 상태. | 대응할 수 없는 체크메이트와 구별한다. | 체크 상태를 해소하는 수를 선택한다. | — | [65] |
| 체크메이트(Checkmate) | 왕이 공격받고 이를 해소할 합법 수가 없는 패배 상태. | 체크나 스테일메이트와 구별한다. | 체크메이트가 성립하면 경기가 끝난다. | — | [65] |
| 승격(Promotion, 체스) | 폰이 마지막 가로줄에 도착해 규정된 다른 말로 바뀌는 것. | 일반 캐릭터 레벨 성장과 구별한다. | 마지막 줄에 도달한 폰을 새 말로 승격한다. | — | [65] |
| 캐슬링(Castling) | 조건을 충족할 때 왕과 룩을 함께 움직이는 특수한 한 수. | 말을 두 번 자유 이동하는 것이 아니다. | 왕과 룩의 이동 이력과 공격 경로 조건을 확인한다. | — | [65] |
| 앙파상(En Passant) | 바로 전 수에서 두 칸 전진한 인접 폰을 특정 조건으로 잡는 특수 포획. | 언제나 가능한 대각 포획이 아니다. | 해당 전진 직후 차례에만 앙파상을 선택할 수 있다. | — | [65] |
| 세로줄(File, 체스) | 체스판의 세로 방향 칸 배열. | 가로줄 Rank와 구별한다. | 룩은 같은 세로줄의 경로를 따라 움직인다. | — | [65] |
| 가로줄(Rank, 체스) | 체스판의 가로 방향 칸 배열. | 순위나 카드 랭크와 구별한다. | 폰이 마지막 가로줄에 도달하면 승격한다. | — | [65] |

<a id="gd-1-18-2"></a>
#### 1.18.2 테이블탑 RPG

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 테이블탑 RPG(TRPG, TTRPG) | 참가자들이 캐릭터의 행동을 선언하고 규칙·판정·서술로 공동 이야기를 진행하는 역할극 형식. | 컴퓨터가 모든 행동·서사를 고정 실행하는 RPG와 판정 주체가 다를 수 있다. | 참가자가 행동을 선언하면 진행자가 결과를 판정해 서술한다. | 게임 마스터·주사위의 필수 여부는 시스템별. | [28] |
| 게임 마스터(GM) | 상황·도전을 제시하고 판정·서술을 진행하는 참가자 역할. | 다른 참가자의 캐릭터 역할과 구별한다. | GM이 환경을 설명하고 선언한 행동의 결과를 정한다. | D&D의 이름은 Dungeon Master(DM). | [28] |
| 행동 선언 | 플레이어가 캐릭터에게 수행시키려는 행동을 설명하는 것. | 성공 결과를 플레이어가 확정하는 것과 구별한다. | 플레이어는 문을 조사한다고 선언한다. | — | [28] |
| 주사위 판정 | 주사위 결과와 규칙 보정을 사용해 불확실한 행동의 결과를 정하는 절차. | 모든 서술에 굴림이 필요한 것은 아니다. | 위험한 행동에 주사위 판정을 적용한다. | — | [28] |
| 캐릭터 시트(Character Sheet) | 캐릭터의 능력·특성·보유물 등 플레이 상태를 기록하는 문서. | 캐릭터의 이야기 설정만과 구별한다. | 캐릭터 시트에 능력치와 숙련을 기록한다. | — | [29] |

<a id="gd-1-19"></a>
### 1.19 파티·사회적추론

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 파티 게임(Party Game) | 여러 참가자의 함께하는 놀이·반응·상호작용을 중심으로 구성한 양식. | 파티는 참여 경험이며 숨은 역할 규칙과 동의어가 아니다. | 참가자들이 서로의 행동을 보고 토론한다. | — | [66], [67] |

<a id="gd-1-19-1"></a>
#### 1.19.1 숨은 역할·사회적추론

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 숨은 역할 게임(Hidden Role) | 참가자 일부의 역할·진영을 다른 참가자가 알 수 없게 하는 정보 구조 중심 형식. | 다른 종류의 비공개 카드·랜덤 결과와 구별한다. | 참가자는 행동 단서로 숨은 적 역할을 찾는다. | — | [66] |
| 사회적추론(Social Deduction) | 참가자의 정체·의도·발언·행동을 해석해 판단하는 플레이 양식. | 논리 퍼즐의 고정 단서 해석과 대인 기만 가능성이 다르다. | 토론과 관찰로 누가 적 역할인지 추론한다. | — | [66] |
| 진영(숨은 역할) | 역할에 따라 목표와 협력 관계를 공유하는 집단. | 전략게임의 기술·유닛 분류와 구별한다. | 같은 진영은 공동 목표를 수행한다. | — | [66] |
| 임무(Task, 사회적추론) | 협력 진영이 완료해 공동 목표를 진행시키는 작업. | 적 역할이 흉내 내는 행동과 실제 완료를 구별한다. | 협력 진영이 임무 진행량을 채우면 승리한다. | — | [66] |
| 사보타주(Sabotage) | 적 역할이 시설·작업을 방해해 혼란이나 위험을 만드는 행동. | 정상 목표 수행과 구별한다. | 사보타주를 복구하기 위해 협력 진영이 이동한다. | — | [66] |
| 긴급 회의(Emergency Meeting) | 의심 행동·사건을 계기로 참가자들이 토론하도록 플레이를 전환하는 절차. | 일반 플레이 중 자유 발언과 구별한다. | 수상한 행동을 발견해 긴급 회의를 연다. | — | [66] |
| 투표(사회적추론) | 참가자들의 선택을 모아 의심 대상 등에 대한 집단 결정을 내리는 절차. | 개별 주장·의심과 구별한다. | 토론 뒤 의심 대상을 투표한다. | 모든 사회적추론 게임의 필수 규칙은 아니다. | [66] |
| 추방(Ejection) | 집단 결정 등에 따라 대상 참가자를 현재 생존 플레이에서 제외하는 것. | 정체 공개나 경기 종료와 별개다. | 최다 득표 대상을 추방한다. | 추방 뒤 역할·행동 허용은 작품별. | [66] |
| 알리바이(Alibi) | 사건 당시 자신의 행동·위치를 설명해 의심에 대응하는 정보·주장. | 검증된 사실인지 거짓 주장인지 별도다. | 참가자가 자신의 이동 경로를 알리바이로 제시한다. | — | [66] |
| 기만(Deception) | 상대가 잘못된 정체·의도를 믿도록 행동·발언하는 것. | 정보가 단순히 숨겨진 상태와 구별한다. | 적 역할이 정상 임무를 수행하는 척한다. | — | [66] |

<a id="gd-1-19-2"></a>
#### 1.19.2 그림·추측 파티

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 그림 추측 게임(Drawing Game) | 참가자가 그린 그림을 다른 참가자가 해석·추측하는 형식. | 자유 그림 편집기와 과제·상호작용 구조가 다르다. | 참가자가 그림에 맞는 답을 추측한다. | — | [67] |
| 가짜 답안 | 다른 참가자가 정답이라고 믿게 하려고 제출하는 오답 후보. | 단순 추측 답변과 목적을 구별한다. | 그림의 가짜 제목으로 다른 참가자의 선택을 유도한다. | — | [67] |

<a id="gd-1-20"></a>
### 1.20 샌드박스·창작

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 샌드박스(Sandbox) | 정해진 순서의 과제보다 세계에서 자유로운 탐색·조작·창작을 허용하는 양식. | 오픈월드의 공간 규모와 동의어가 아니다. | 참가자가 세계의 물체를 자유롭게 배치하고 실험한다. | 목표·제약의 유무는 모드별로 다르다. | [42], [64] |
| 사용자 제작 콘텐츠(샌드박스·창작 적용) | 일반 뜻은 [공용 사용자 제작 콘텐츠(UGC)](#213-제작유통운영매체) 참조. | 이 장르에서는 사용자가 레벨·월드·시나리오 등을 직접 제작하는지 확인하며, 플레이 중 획득 아이템이나 자동 생성물과 구별한다. | 편집기로 만든 레벨을 사용자 제작 콘텐츠로 저장한다. | 공유 기능의 존재는 별도 확인 대상. | [42], [47], [55] |
| 맵 편집기(Map Editor) | 맵의 지형·대상·배치를 제작·변경하는 도구. | 기본 플레이의 건설 행동과 구별한다. | 맵 편집기로 시작 지형과 자원 배치를 정한다. | — | [47] |
| 시나리오(창작) | 시작 상태·목표·조건 등을 정해 구성한 플레이 콘텐츠. | 맵 배치 데이터만과 구별한다. | 시나리오마다 목표와 시간 조건을 다르게 정한다. | — | [47] |
| 규칙 설정(창작) | 콘텐츠 안에서 조건·행동·판정의 동작을 변경하는 것. | 시각 배치 편집만과 구별한다. | 특정 사건이 발생하면 새 목표를 주도록 규칙을 설정한다. | — | [47] |
| 스크립트(시나리오) | 사건·조건에 따른 동작을 작성해 시나리오 규칙을 실행시키는 코드. | 구성물의 수동 조작과 구별한다. | 스크립트로 임무 시작과 완료 조건을 구현한다. | — | [47] |
| 물리 샌드박스(디지털) | 물체의 배치·운동·접촉을 자유롭게 조작하는 디지털 도구·플레이 형식. | 개별 보드게임의 자동 규칙 실행과 구별한다. | 참가자가 가상 구성물을 움직이고 뒤집는다. | — | [64] |

<a id="gd-1-21"></a>
### 1.21 방치·증분

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 방치 게임(Idle Game, Idler) | 지속 입력이 적은 동안에도 자원·진행이 자동으로 늘어나는 양식. | 자동 기능이 하나 있다는 사실만과 구별한다. | 입력하지 않아도 자원이 누적되고 돌아와 재투자한다. | [42]은 앱을 닫은 동안의 진행까지 포함한다. | [42], [68] |
| 증분 게임(Incremental Game) | 자원 축적과 재투자를 반복해 생산 역량·수치를 확대하는 양식. | 입력 없는 진행 여부와 축적·투자 구조는 별개다. | 얻은 자원을 생산기에 투자해 다음 수입을 늘린다. | 방치·클리커와 중첩하지만 동일 조건은 아니다. | [69], [68] |

<a id="gd-1-21-1"></a>
#### 1.21.1 클리커

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 클리커(Clicker) | 반복 클릭 등의 직접 입력을 자원 축적 수단으로 강조하는 양식. | 자동 생산이 없는 게임만을 뜻하지 않는다. | 클릭으로 자원을 모아 자동 생산을 확장한다. | — | [69] |

<a id="gd-1-21-terms"></a>
#### 공통 용어: 생산기·생산량·프레스티지

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 주 화폐(Primary Currency, 증분) | 핵심적으로 축적·증가시키는 대표 수치 자원. | 현금 화폐라는 뜻은 아니다. | 생산기가 주 화폐를 누적한다. | — | [68] |
| 생산기(Generator, 증분) | 주 화폐 등 자원을 반복적으로 산출하는 구입·운영 대상. | 일회 보상과 구별한다. | 생산기를 구매해 자동 수입을 늘린다. | — | [68] |
| 초당 수입(Income per Second) | 생산기가 단위 시간에 만들어내는 화폐량. | 현재 보유 화폐와 구별한다. | 생산기와 배율을 늘려 초당 수입을 높인다. | — | [68] |
| 중개 생산 자원(Primary Exchange Currency) | 생산 뒤 교환·변환을 통해 주 화폐를 얻는 중간 수치. | 주 화폐를 직접 만드는 생산과 구별한다. | 공격력을 생산하고 적 처치로 이를 화폐 수입에 연결한다. | — | [68] |
| 생산 배율(Multiplier, 증분) | 생산기의 수입·효율에 곱하는 강화값. | 정액으로 더하는 보너스와 구별한다. | 생산 배율 강화로 같은 생산기 수의 수입이 증가한다. | — | [68] |
| 프레스티지(Prestige) | 현재 생산·진행의 상당 부분을 초기화하는 대가로 다음 진행을 가속할 지속 보너스를 얻는 것. | 일반 재시작이나 아무것도 남지 않는 초기화와 구별한다. | 생산기를 초기화하고 영구 배율을 얻는다. | 초기화·보존 범위는 작품별. | [68] |
| 프레스티지 화폐 | 프레스티지로 얻어 이후 진행 강화에 사용하는 지속 자원. | 현재 회차의 주 화폐와 구별한다. | 프레스티지 화폐로 다음 회차의 생산을 강화한다. | — | [68] |
| 구매 비용 성장(Cost Growth) | 보유 수 등의 조건에 따라 다음 생산기 구입 비용이 높아지는 규칙. | 고정 가격 구매와 구별한다. | 같은 생산기를 많이 보유할수록 다음 가격이 오른다. | 지수 성장만이 필수 규칙은 아니다. | [68] |
| 일괄 구매(Bulk Buy) | 여러 생산기 등을 한 번에 구입하는 조작·구매 방식. | 비용·효율 규칙 자체와 구별한다. | 생산기를 정해진 묶음 수로 일괄 구매한다. | — | [68] |

<a id="gd-1-22"></a>
### 1.22 카지노형 플레이

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 카지노형 플레이 | 슬롯·포커·블랙잭 등 카지노에서 쓰이는 게임 규칙·형식을 사용하는 플레이. | 현실 금전 베팅·환전·상품 지급은 별도다. | 가상 칩으로 카지노 카드 규칙을 플레이한다. | 시장의 Casino 분류와 현실 도박 여부를 동일시하지 않는다. | [70], [71] |
| 소셜카지노(Social Casino) | 카지노 형식을 가상 자원과 온라인·사회적 기능으로 제공하는 서비스 양식. | 현실 돈을 얻는 도박인지와 별개로 구별한다. | 가상 아이템 구매와 친구 기능을 제공하되 현금 지급은 하지 않는다. | 실제 구매 가능성과 현실 지급 가능성은 별도. | [71] |

<a id="gd-1-22-1"></a>
#### 1.22.1 슬롯

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 슬롯(Slots) | 슬롯머신 형식의 결과 추첨·지급 규칙을 주요 플레이로 삼는 양식. | 포커처럼 패 선택·배팅으로 진행하는 형식과 구별한다. | 가상 자원으로 슬롯 형식의 결과를 확인한다. | 릴·라인·보너스 상세 규칙은 작품별. | [70], [71] |
| 릴(Reel, 슬롯) | 기호를 표시하며 회전하는 물리 원판 또는 디지털 회전 구조. | 결과를 판정하는 페이라인과 구별한다. | 스핀 뒤 각 릴에 표시된 기호를 확인한다. | 디지털 슬롯은 실제 회전 부품이 없어도 릴이라 부른다. | [72] |
| 스핀(Spin, 슬롯) | 릴을 작동시켜 한 번의 기호 조합 결과를 만드는 플레이 단위. | 릴이라는 구조물이나 여러 결과를 포함하는 세션과 구별한다. | 스핀 한 번의 결과를 페이테이블 조건에 대조한다. | 무료 스핀·재스핀은 별도의 비용·발동 조건을 갖는다. | [72] |
| 페이라인(Payline) | 당첨 기호 조합을 평가하는 릴 위의 지정 배열 경로. | 기호 조합별 지급값을 정한 페이테이블과 구별한다. | 활성 페이라인에 놓인 기호 조합으로 당첨 여부를 판정한다. | 클러스터·ways 방식은 고정 페이라인과 다른 판정 구조다. | [72] |
| 페이테이블(Paytable) | 당첨 조합과 그에 대응하는 지급값을 제시한 표. | 당첨 배열의 경로인 페이라인과 구별한다. | 결과 조합에 해당하는 지급값을 페이테이블에서 찾는다. | — | [72] |

<a id="gd-1-22-2"></a>
#### 1.22.2 포커

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 포커(Poker) | 카드 패의 순위와 베팅·기만 결정을 조합해 팟을 두고 경쟁하는 카드 형식. | 가장 좋은 패가 항상 승리하는 것은 아니다. | 상대가 모두 폴드하면 패 공개 없이 팟을 얻는다. | — | [73] |
| 핸드(포커 패, Hand) | 패의 순위 판정에 사용하는 카드 조합. | 배분·베팅 한 회차를 뜻하는 핸드와 구별한다. | 최종 핸드의 조합 순위를 비교한다. | 같은 단어가 패와 한 판을 모두 가리킨다. | [73] |
| 핸드(포커 한 판, Hand) | 카드 배분과 베팅으로 진행되는 한 회차의 플레이 단위. | 순위 판정에 사용하는 카드 조합인 핸드와 구별한다. | 이번 핸드가 끝나면 다음 핸드의 카드를 배분한다. | 한 핸드 안의 베팅 라운드와 전체 플레이 회차를 구별한다. | [73] |
| 칩(Chip) | 베팅·보유량을 표시하는 단위 토큰. | 반드시 현실 돈과 교환된다는 뜻은 아니다. | 가상 칩을 팟에 넣어 베팅한다. | — | [73] |
| 팟(Pot) | 참가자가 해당 판에 베팅한 칩이 모인 공동 획득 대상. | 개인 보유 칩과 구별한다. | 승자가 팟을 가져간다. | — | [73] |
| 앤티(Ante) | 패를 배분하기 전 규칙상 넣는 초기 베팅 기여. | 선택적 추가 베팅과 구별한다. | 판을 시작하기 전에 앤티를 넣는다. | — | [73] |
| 콜(Call) | 현재 요구되는 베팅액에 맞춰 판에 남는 선택. | 베팅액을 올리는 레이즈와 구별한다. | 상대의 베팅에 콜해 다음 공개를 기다린다. | — | [73] |
| 레이즈(Raise) | 콜에 필요한 금액을 넘겨 베팅액을 올리는 선택. | 동일 금액을 맞추는 콜과 구별한다. | 레이즈로 다른 참가자의 대응을 요구한다. | — | [73] |
| 폴드(Fold) | 해당 판의 경쟁을 포기하고 이후 베팅·판정에서 물러나는 선택. | 세션 종료와 구별한다. | 폴드하면 이미 넣은 칩을 되돌려받지 않는다. | — | [73] |
| 체크(포커, Check) | 추가 베팅 없이 차례를 넘기며 판에 남는 선택. | 이미 대응할 베팅이 있을 때의 콜과 구별한다. | 요구 베팅이 없을 때 체크한다. | — | [73] |
| 쇼다운(Showdown) | 최종 베팅 뒤 남은 참가자들이 패를 공개해 순위를 비교하는 단계. | 모두 폴드해 공개 없이 끝나는 판과 구별한다. | 쇼다운에서 가장 높은 조합이 팟을 얻는다. | — | [73] |
| 블러핑(Bluffing, 포커) | 패의 강함에 대한 상대 판단을 흔들어 베팅·포기를 유도하는 플레이. | 단순 비공개 패 보유와 구별한다. | 약한 패로 강한 베팅을 해 폴드를 유도한다. | 사회적추론의 기만과 적용 대상이 다르다. | [73] |
| 스트레이트(Straight) | 연속된 랭크로 구성된 패 조합. | 같은 무늬를 요구하는 플러시와 구별한다. | 연속 랭크 조합을 스트레이트로 판정한다. | 카드 수와 상위 조합은 포맷별. | [73] |
| 플러시(Flush) | 같은 무늬의 카드로 구성된 패 조합. | 연속 랭크를 요구하는 스트레이트와 구별한다. | 같은 무늬의 패를 플러시로 판정한다. | — | [73] |
| 풀하우스(Full House) | 같은 랭크 세 장과 다른 랭크 두 장으로 구성된 패 조합. | 서로 다른 두 쌍이나 포카드와 구별한다. | 세 장과 한 쌍의 조합을 풀하우스로 판정한다. | — | [73] |
| 와일드 카드(Wild Card, 포커) | 규칙상 다른 랭크·무늬를 대신할 수 있는 카드. | 카드 원래 값과 별개인 대체 자격이다. | 와일드 카드로 부족한 조합을 채운다. | 허용 대체 범위는 규칙별. | [73] |
| 드로 포커(Draw Poker) | 비공개로 받은 패를 교환해 개선하는 포커 형식. | 일부 카드가 공개되며 진행하는 스터드와 구별한다. | 카드를 교환한 뒤 다시 베팅한다. | — | [73] |
| 스터드 포커(Stud Poker) | 베팅 진행 중 일부 패가 공개되는 포커 형식. | 전부 비공개로 배분되는 드로 형식과 구별한다. | 공개 카드와 베팅을 보고 상대를 판단한다. | — | [73] |
| 고정 한도(Fixed Limit) | 베팅·레이즈의 증액 크기를 정해 둔 규칙. | 팟 크기에 따라 한도가 바뀌는 포트리밋과 구별한다. | 정해진 증액 단위로만 레이즈한다. | — | [73] |
| 팟 한도(Pot Limit) | 팟 규모를 기준으로 최대 베팅·레이즈액을 제한하는 규칙. | 고정 수량 한도와 구별한다. | 현재 팟 규모에 맞춰 레이즈 한도를 계산한다. | — | [73] |

<a id="gd-1-22-3"></a>
#### 1.22.3 블랙잭

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 블랙잭(Blackjack) | 합계 21을 넘지 않으면서 딜러보다 좋은 패를 만드는 카드 형식. | 다른 참가자와 패 순위로 팟을 다투는 포커와 구별한다. | 딜러를 상대로 카드 합계를 비교한다. | 처음의 에이스와 10값 카드 조합도 블랙잭이라 부른다. | [74] |
| 히트(Hit, 블랙잭) | 패에 카드를 추가로 받는 선택. | 현재 합계로 종료하는 스탠드와 구별한다. | 합계를 개선하려고 히트한다. | — | [74] |
| 스탠드(Stand) | 추가 카드를 받지 않고 자신의 선택 차례를 끝내는 것. | 베팅 포기인 폴드와 구별한다. | 현재 합계를 유지하며 스탠드한다. | — | [74] |
| 버스트(Bust) | 패 합계가 허용 상한 21을 초과하는 실패 상태. | 딜러보다 합계가 낮아서 지는 것과 구별한다. | 추가 카드로 21을 넘으면 버스트한다. | — | [74] |
| 더블 다운(Double Down) | 베팅을 늘리고 마지막 카드 하나를 받은 뒤 멈추는 선택. | 여러 번 자유롭게 히트하는 것과 구별한다. | 더블 다운 뒤에는 추가 카드를 받지 않는다. | 허용 조건은 변형별. | [74] |
| 스플릿(Split) | 동일 랭크의 시작 패를 나누어 두 패로 따로 플레이하는 것. | 같은 패에 추가 카드를 받는 것과 구별한다. | 추가 베팅을 내고 시작 쌍을 스플릿한다. | — | [74] |
| 푸시(Push) | 딜러와 동점 등으로 원래 베팅을 돌려받는 결과. | 승리 지급과 구별한다. | 동점은 푸시로 처리해 베팅을 반환한다. | — | [74] |
| 인슈어런스(Insurance) | 딜러의 블랙잭 여부를 대상으로 하는 별도의 보조 베팅. | 현재 패의 주 베팅과 결과가 별개다. | 주 패 결과와 인슈어런스 결과를 따로 판정한다. | — | [74] |

<a id="gd-1-23"></a>
### 1.23 로그 계열

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 로그 계열(Roguelike family) | 절차적 변화와 실패 뒤 재도전 구조를 공유하는 전통·변형 로그 유형군. | 공통 진행·생성 성질을 묶는 조회 항목이며 단일 장르 규약은 아니다. | 매번 다른 환경에서 새 시도를 시작하는 로그 계열 구조를 구성한다. | [4]: 전통 커뮤니티 기준; [6]: 현대 넓은 roguelike·roguelite 용례. | [4], [6] |

<a id="gd-1-23-1"></a>
#### 1.23.1 전통 로그라이크

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 전통 로그라이크(Traditional roguelike) | 턴·격자 기반 탐색과 자원 관리, 무작위 환경과 영구 사망을 강조하는 전통 유형. | 현대 실시간 변형과 역사적 규칙 강조점을 구별한다. | 격자에서 행동을 선택하며 미식별 아이템과 위험을 관리한다. | Berlin Interpretation은 가중 요인 해석이며 모든 항목이 필수라는 규칙이 아니다. | [4], [6] |
| 격자 행동(Grid-based action, 로그) | 캐릭터와 대상이 격자 칸을 단위로 배치·이동하는 구성. | 자유 연속 좌표 이동과 구별한다. | 한 번 이동하면 인접한 격자 칸으로 옮겨진다. | 격자 기반은 다른 장르에도 존재한다. | [4] |
| 비모달(Non-modal, 로그) | 이동·전투 등 행동이 서로 분리된 전용 모드 없이 같은 공간 규칙에서 진행되는 성질. | 전투 진입 시 별도 화면·규칙으로 전환하는 구조와 구별한다. | 탐색 중에도 같은 격자에서 아이템 사용과 공격을 선택한다. | 전통 로그라이크 해석의 한 요인이다. | [4] |
| 아이템 식별(Item identification, 로그) | 미지의 아이템이 어떤 효과인지 탐색·사용 등으로 알아내는 과정. | 이미 표시된 능력치 비교와 구별한다. | 이번 시도에서 처음 찾은 물약의 효과를 식별한다. | 이름·효과 재설정 방식은 작품별 규칙이다. | [4] |
| 영구 사망(로그 적용) | 일반 뜻은 [공용 영구 사망](#26-시간진행성장) 참조. | 전통 로그 해석에서는 사망한 시도를 처음부터 재시작하며 중단 저장과 사망 복원을 구별한다. | 중단 저장으로 런을 이어갈 수 있지만 사망한 런은 복원할 수 없다. | 전체 시도 종료는 로그 맥락이며 개별 캐릭터 영구 제외와 범위가 다르다. | [4] |

<a id="gd-1-23-2"></a>
#### 1.23.2 로그라이트·액션 로그라이크

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 로그라이트(Roguelite) | 전통 로그라이크의 재시도·생성 성질 일부를 다른 규칙과 결합한 변형 명칭. | 전통 규칙을 모두 재현한다는 뜻이 아니다. | 실시간 전투와 반복 시도 구조를 결합한 로그라이트를 구성한다. | [6]: 넓은 변형 구별 명칭; 런 간 영구 성장이 반드시 있어야 한다는 단일 표준은 아니다. | [6], [75] |
| 액션 로그라이크(Action roguelike) | 로그 계열의 반복 시도 구조에 실시간 액션을 결합한 유형. | 턴 선택 기반 전통 로그라이크와 실행 방식이 다르다. | 실시간 공격과 회피를 수행하며 매번 다른 전장을 통과한다. | 현대 넓은 roguelike 용례여서 roguelite와 명칭이 겹칠 수 있다. | [6] |
| 런 내 성장(In-run progression) | 이번 시도가 유지되는 동안 얻는 능력·장비 개선. | 다음 시도에도 남는 성장과 구별한다. | 이번 런에서 얻은 강화는 런이 끝나면 사라진다. | 런의 공용 정의는 공용 사전 참조. | [76], [75] |
| 런 간 성장(Between-run progression, Persistent progression) | 시도가 끝나도 다음 시도에 유지되는 능력·시설·선택지 개선. | 런 내 성장은 이번 시도에서만 유효하며 런 간 성장은 후속 시도의 출발 조건에 영향을 준다. | 런 종료 뒤 얻은 재화로 영구 강화를 구매해 다음 시도에 적용한다. | 영구 강화의 존재는 로그라이트 전체의 필수 정의가 아니다. | [77] |

<a id="gd-1-23-3"></a>
#### 1.23.3 로그라이크 덱빌더

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 로그라이크 덱빌더(Roguelike deckbuilder) | 반복 시도 중 카드 선택으로 덱을 변화시키며 전투하는 결합 유형. | 사전 구성 덱을 그대로 쓰는 카드 경기와 구별한다. | 매 전투 보상에서 카드를 골라 이번 시도의 덱을 바꾼다. | 로그라이크 용례는 현대 넓은 의미이며 턴·격자 탐색을 모두 요구하지 않는다. | [76] |
| 런 중 덱 구축(In-run deckbuilding) | 한 시도 안에서 카드를 추가·제거하여 전투 덱을 만드는 과정. | 경기 전에 덱 목록을 완성하는 덱 구성과 구별한다. | 다음 경로의 적을 고려해 런 중 덱 구축 선택을 한다. | 카드 공용 덱·패·드로우는 카드 사전 참조. | [76] |

<a id="gd-1-24"></a>
### 1.24 소울라이크

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 소울라이크(Soulslike) | 반복 실패와 적 패턴 학습, 신중한 전투·탐색을 강조하는 영향 계열 명칭. | 높은 난도 하나만으로 판정하지 않는다. | 반복 실패에서 적 패턴을 익혀 다음 탐색 구간으로 진행한다. | 공유 특징의 정도와 필수 조건에 합의된 단일 표준은 없다. | [78] |
| 스태미나 관리(Stamina management, 소울 전투) | 공격·방어·이동 행동으로 소모되는 수행 자원을 남길지 쓰는 판단. | 체력 피해 관리와 달리 다음 행동 가능성의 비용을 다룬다. | 공격 후 회피할 스태미나를 남겨 둔다. | 소모 행동과 회복 규칙은 작품마다 다르다. | [78] |
| 사망 자원 회수(Death recovery) | 사망으로 잃거나 남긴 화폐·경험 자원을 다시 확보하는 과정. | 로그의 캐릭터 영구 사망과 구별한다. | 사망 위치로 돌아가 남긴 자원을 회수한다. | 재사망 시 소멸 여부 등은 개별 규칙이다. | [78] |
| 휴식 체크포인트(Rest checkpoint) | 회복·저장·이동 등의 거점이며 휴식 시 적 배치 등이 다시 시작될 수 있는 지점. | 단순 사망 재개 위치와 기능 범위가 다르다. | 휴식 체크포인트에서 회복하면 일반 적이 다시 나타난다. | 모든 체크포인트가 적을 재생성하는 것은 아니다. | [78] |

<a id="gd-1-25"></a>
<a id="125-메트로배니아"></a>
### 1.25 메트로배니아

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 메트로배니아(Metroidvania) | 연결된 세계를 탐색하며 획득 능력·도구 등으로 이전의 막힌 경로를 여는 유형. | 비선형 맵만 있거나 선형 스테이지에서 능력만 얻는 구성과 구별한다. | 새 이동 능력을 얻어 이전 지역의 막힌 경로를 연다. | 주로 플랫폼 결합 용례지만 3D 적용도 있다. | [79] |
| 능력 게이트(Ability gate) | 특정 캐릭터 능력이 없으면 통과할 수 없는 접근 조건. | 숫자 난도나 일반 자물쇠와 조건의 성질이 다르다. | 높은 발판은 추가 도약 능력을 얻은 뒤 통과한다. | — | [79] |
| 백트래킹(Backtracking, 메트로배니아) | 새 능력·정보를 활용하려고 이전 공간으로 돌아가는 탐색. | 단순 되돌아가기가 아니라 접근·발견 변화가 중요하다. | 백트래킹으로 처음에는 못 열던 통로를 탐색한다. | — | [79] |
| 연결 맵(Interconnected map) | 지역들이 여러 통로로 하나의 탐색 세계를 이루는 공간 구조. | 메뉴에서 별도 스테이지를 선택하는 구조와 구별한다. | 새 통로가 두 지역을 연결해 이동 선택을 늘린다. | — | [79] |
| 지름길(Shortcut, 탐색) | 기존 목적지까지 더 짧거나 쉬운 이동 경로를 제공하는 연결. | 완전히 새 지역 해금과 이동 효용이 다르다. | 문을 열어 거점으로 돌아가는 지름길을 확보한다. | — | [79] |

<a id="gd-1-25-1"></a>
#### 1.25.1 2D·3D 메트로배니아

전문 용어 조회: [1.25 메트로배니아의 능력 게이트·백트래킹·연결 맵·지름길](#125-메트로배니아), [1.4 플랫폼의 공중 제어·벽점프](#14-플랫폼). 이동 차원과 별개로 접근 조건과 재방문 흐름은 부모 정의를 사용한다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 2D 메트로배니아(2D Metroidvania) | 주로 2차원 이동 공간에서 연결 탐색과 능력 해금을 수행하는 유형. | 그래픽의 렌더링 차원과 실제 이동 공간을 구별한다. | 횡스크롤 연결 맵에서 이동 능력으로 갈 수 있는 곳을 늘린다. | — | [79] |
| 3D 메트로배니아(3D Metroidvania) | 3차원 탐색 공간에 연결 맵·능력 해금 구조를 적용한 유형. | 카메라가 입체적이라는 사실만으로 판정하지 않는다. | 획득한 도구를 이전의 입체 공간에 적용해 새 경로를 연다. | 경계가 넓거나 논쟁적인 용례도 있어 규칙을 함께 밝힌다. | [79] |

<a id="gd-1-25-2"></a>
#### 1.25.2 로그바니아·지식 기반 탐색

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 로그바니아(RogueVania) | 로그라이트의 반복 시도와 메트로배니아 영향의 액션 탐색을 결합한 명칭. | 모든 로그라이크나 모든 비선형 플랫폼을 뜻하지 않는다. | 반복 시도 안에서 해금한 이동 능력으로 경로 선택을 넓힌다. | [75]의 개발사 자칭 결합명이며 독립적인 보편 분류 규약이 아니다. | [75] |
| 메트로브레이니아(Metroidbrainia) | 캐릭터 장비보다 플레이어가 얻는 지식이 접근과 진행을 크게 여는 탐색 유형. | 능력 게이트는 캐릭터 상태, 지식 게이트는 플레이어 이해에 중심을 둔다. | 이미 열린 장소라도 작동 방법을 알아야 새로운 경로로 사용할 수 있다. | 비교적 후대의 결합 명칭이며 모든 탐색 퍼즐의 동의어는 아니다. | [79] |
| 지식 게이트(Knowledge gate) | 방법·규칙을 몰라 접근하거나 활용하지 못하는 진행 조건. | 아이템 소유 여부로 잠기는 접근 조건과 구별한다. | 장치의 원리를 이해하면 초기 장소에서 바로 목표로 접근할 수 있다. | — | [79] |

<a id="gd-1-26"></a>
### 1.26 생존

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 생존(Survival) | 적대적 환경에서 필요한 자원과 상태를 관리해 살아남는 일을 중심으로 하는 유형. | 모든 죽지 않기 과제나 생존 모드의 이름과 구별한다. | 먹을 것과 안전한 장소를 확보하며 생존 상태를 유지한다. | 영구 사망과 오픈월드는 자주 결합되지만 필수 조건은 아니다. | [80] |
| 허기(Hunger, 생존 상태) | 음식 부족을 나타내어 생존 행동이나 실패에 영향을 주는 상태. | 일반 체력과 같은 수치로 통합되지 않을 수 있다. | 음식을 먹지 않으면 허기가 누적되어 불이익을 받는다. | — | [80] |
| 갈증(Thirst, 생존 상태) | 수분 부족을 나타내는 생존 상태. | 허기와 별도 자원·조건으로 관리할 수 있다. | 물을 확보해 갈증 상태를 낮춘다. | — | [80] |
| 정신 상태(Mental state, 생존) | 환경·사건 등이 정신적 안정에 미치는 영향을 규칙화한 상태. | 플레이어의 실제 감정이 아니라 게임 내 상태다. | 위험한 환경에 오래 머물면 정신 상태가 악화된다. | 모든 생존게임의 필수 지표는 아니다. | [80] |
| 도구 내구도(생존 적용) | 일반 뜻은 [공용 내구도](#210-공통-시스템) 참조. | 생존 제작에서는 반복 사용 도구의 파손을 수집·제작 판단과 연결한다. | 채집 도구가 파손되어 대체 도구를 제작해야 한다. | 일회성 소비 아이템과 달리 사용을 누적한다. | [80] |

<a id="gd-1-26-1"></a>
#### 1.26.1 생존제작·오픈월드 생존제작

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 생존제작(Survival crafting) | 생존에 필요한 도구·물자를 자원 수집과 제작으로 확보하는 결합 유형. | 제작이 곁들여진 모든 생존 경험보다 자원·도구 순환을 강조한다. | 돌 도구로 금속을 얻은 뒤 상위 도구를 제작한다. | 제작의 공용 정의는 공용 사전 참조. | [80] |
| 오픈월드 생존제작(Open-world survival crafting) | 열린 탐색 세계에서 수집·제작·생존을 결합한 유형. | 선형 임무 공간의 생존제작과 공간 구조가 다르다. | 자유롭게 지역을 탐색하며 생존 거점을 마련한다. | 오픈월드 자체는 공간 속성이다. | [80] |
| 피난처(Shelter) | 환경·적의 위협을 피하도록 확보하는 보호 공간. | 단순 장식 건축보다 보호 기능이 중심이다. | 밤이 되기 전에 피난처를 만들어 위험을 피한다. | — | [80] |

<a id="gd-1-27"></a>
### 1.27 공포

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 공포(Horror game) | 두려움·불안·긴장을 의도하는 소재와 표현을 중심으로 하는 유형군. | 전투 방식만으로 분류되는 장르와 다른 경험·서사 축이다. | 익숙한 공간의 이상 변화로 공포를 유발한다. | 공포 소재와 규칙 장르는 중첩될 수 있다. | [81] |

<a id="gd-1-27-1"></a>
#### 1.27.1 생존공포

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 생존공포(Survival horror) | 공포 환경에서 제한된 자원과 취약성을 관리하며 생존·탈출하는 유형. | 강력한 전투 능력으로 적을 제거하는 액션공포와 강조점이 다르다. | 한정된 탄약을 아끼며 위험 구간에서 탈출한다. | 제작·허기 중심 일반 생존과 필수 규칙을 공유하지 않는다. | [81] |
| 자원 희소성(Resource scarcity, 공포) | 방어·회복 등에 필요한 자원을 부족하게 배치해 대응 선택을 제한하는 구성. | 수량 제한 자체보다 안전하게 대응할 여지의 부족을 강조한다. | 회복 자원이 적어 피해를 피하는 경로 선택이 중요하다. | — | [81] |

<a id="gd-1-27-2"></a>
#### 1.27.2 심리공포

전문 용어 조회: [2.8 공용 단서·불확실성](#28-정보확률), [어드벤처의 환경 서사](#163-워킹-시뮬레이터). 기록과 공간의 흔적을 해석하거나 현실 판단의 불확실성을 설명할 때 조회하며, 이러한 정보·연출 구성이 모든 심리공포의 필수 조건은 아니다.

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 심리공포(Psychological horror) | 정신·정체성·현실 판단의 불안 등을 통해 두려움을 만드는 유형. | 눈앞의 괴물이나 즉각 놀람만을 중심으로 하지 않는다. | 모순되는 기록과 장소 변화를 제시해 기억의 신뢰성을 의심하게 한다. | 생존공포·액션과 함께 성립할 수 있다. | [81] |

<a id="gd-1-27-3"></a>
#### 1.27.3 액션공포·점프스케어

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 액션공포(Action horror) | 공포 소재에 빠르고 직접적인 전투 행동을 강조하는 유형. | 제한 자원·퍼즐 중심 생존공포와 전투 비중이 다르다. | 공포 환경에서 적극적으로 무기를 사용해 적을 돌파한다. | 장르 간 경계는 작품마다 겹친다. | [81] |
| 점프 스케어(Jump scare) | 예상하지 못한 순간의 자극으로 즉각 놀람을 유발하는 연출. | 서서히 조성하는 불안과 구별한다. | 조용한 탐색 뒤 갑작스러운 등장으로 점프 스케어를 만든다. | 특정 장르의 필수 기능은 아니다. | [81] |
| 역공포(Reverse horror) | 플레이어가 위협 주체가 되어 다른 대상을 겁주거나 사냥하는 공포 유형. | 플레이어의 취약한 생존을 중심으로 하는 공포와 역할이 반대다. | 플레이어가 괴물 역할로 상대의 도주 경로를 차단한다. | — | [81] |

<a id="gd-1-28"></a>
### 1.28 배틀로얄

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 배틀로얄(Battle royale) | 다수 참가자가 제한된 생존 자원을 확보하며 최후의 플레이어·팀을 가리는 형식. | 추출 성공이나 누적 점수가 최종 목표인 경기와 구별한다. | 줄어드는 활동 구역 안에서 최후의 팀이 될 때까지 경쟁한다. | 슈팅 이외 장르에도 결합되는 경기 형식이다. | [82] |
| 안전 구역(Safe zone, 배틀로얄) | 밖에 있으면 피해·제거 위험이 발생하는 유효 생존 영역. | 공포의 위협 없는 안전 공간과 의미가 다르다. | 다음 안전 구역 안으로 이동해 구역 피해를 피한다. | 안에 있어도 다른 참가자의 공격에는 안전하지 않다. | [82] |
| 구역 축소(Shrinking zone) | 진행에 따라 유효 활동 영역을 줄여 참가자 간 접촉을 유도하는 규칙. | 일반 지형 변화와 달리 남은 생존 공간을 줄인다. | 구역 축소가 원거리 은신을 제한한다. | — | [82] |
| 최후 생존(Last player/team standing) | 다른 참가자가 제거된 뒤 마지막으로 남는 승리 조건. | 제한 시간 동안 생존하는 목표와 다르다. | 마지막 생존 팀에 승리를 부여한다. | — | [82] |
| 현장 파밍(Looting, 배틀로얄) | 경기 중 지도나 제거된 참가자에게서 장비를 확보하는 행동. | 지속 장비 성장 중심 루터 슈터와 유지 범위가 다르다. | 착지 뒤 가까운 건물에서 무기와 방어 장비를 찾는다. | 파밍의 공용 넓은 의미는 반복 자원 획득이다. | [82] |

<a id="gd-1-29"></a>
### 1.29 익스트랙션·추출형

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 추출형 슈터(Extraction shooter) | 임무 공간에서 물자를 얻고 추출에 성공해 이를 보유하는 슈팅 유형. | 최후 생존자만 승리하는 배틀로얄과 목표가 다르다. | 위험 지역에서 물자를 수집한 뒤 추출을 선택한다. | PvPvE는 흔한 구성이지 모든 추출형의 필수 조건은 아니다. | [83] |
| 추출 지점(Extraction point) | 임무 공간에서 성공적으로 이탈하는 절차를 수행하는 위치. | 맵의 아무 출구나 단순 이동 지점과 다르다. | 지정 추출 지점에 도달해 반출을 완료한다. | — | [83] |
| 반출(Extraction of loot) | 임무 중 획득한 물자를 안전하게 임무 밖 보유 자산으로 옮기는 결과. | 물자를 줍는 순간의 임시 보유와 구별한다. | 추출에 성공한 물자는 다음 출격에 사용할 수 있다. | — | [83] |
| 장비 손실(Gear loss, 추출형) | 추출 실패로 가져간 장비나 획득 물자를 잃는 위험. | 단순 캐릭터 부활 비용과 구별한다. | 출격 장비가 좋을수록 실패 시 손실도 커진다. | 보험·보호 슬롯 등 예외는 작품별 규칙이다. | [83] |
| 추출 제한 시간(Extraction time limit) | 성공적인 이탈을 완료해야 하는 임무의 시간 제약. | 장르 일반의 제한 시간과 달리 반출 성공 여부를 제한한다. | 제한 시간 전에 추출을 완료해야 물자를 보유한다. | 모든 추출형에 같은 시간 제약이 있는 것은 아니다. | [83] |
| 부가 임무(추출형) | 단순 이탈 외에 보상·진행을 위해 출격 중 수행하는 목표. | 획득 물자의 양이나 적 제거만으로 정의되지 않는다. | 목표 문서를 확보한 뒤 추출하면 추가 진행 보상을 받는다. | — | [83] |

<a id="gd-1-30"></a>
### 1.30 MOBA

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| MOBA(Multiplayer Online Battle Arena) | 팀이 전장에서 캐릭터를 운용해 적 기지·팀을 제압하는 대전 전략 양식. | RTS의 다수 부대 경제와 달리 캐릭터 역할 운용을 중심에 둔다. | 팀이 경로를 확보해 적 기지를 파괴한다. | [38]의 시장 분류는 기지 파괴 외 팀 제압 양식도 포함한다. | [38], [31] |
| 레인(Lane, MOBA) | 기지를 연결하며 전투·진행이 이루어지는 주요 경로. | 생산 물류의 벨트 레인과 구별한다. | 레인의 방어 시설을 넘겨 기지로 진입한다. | — | [31] |
| 미니언(Minion) | 기지에서 발생해 전선으로 향하는 보조 유닛. | 플레이어가 주요 조작하는 챔피언과 구별한다. | 미니언을 앞세워 방어 시설을 공격한다. | — | [31] |
| 정글(Jungle) | 레인 사이에 중립 몬스터 등 별도 자원이 있는 영역. | 레인 경로와 구별한다. | 정글의 중립 몬스터를 처치한다. | — | [31] |
| 중립 몬스터(Neutral Monster) | 어느 팀에도 속하지 않으며 별도 처치 보상·효과를 제공하는 전장 대상. | 적 팀 미니언과 구별한다. | 중립 몬스터 처치로 팀 강화 효과를 얻는다. | — | [31] |
| 포탑(Turret, MOBA) | 경로·기지를 지키며 적 유닛과 캐릭터를 공격하는 방어 구조물. | 캐릭터 능력이나 장비와 구별한다. | 미니언 없이 포탑에 접근하면 직접 공격받는다. | — | [31] |
| 기지 핵(Nexus 계열) | 파괴하면 경기 승리 조건이 성립하는 기지 중심 목표물. | 다른 방어 시설과 구별한다. | 적 기지 핵을 먼저 파괴한 팀이 승리한다. | 명칭·승리 조건은 작품별. | [31] |
| 궁극기(Ultimate) | 캐릭터의 능력 구성에서 특별한 핵심 능력으로 구분하는 기술. | 기본 능력·패시브와 구별한다. | 캐릭터의 궁극기와 기본 능력을 조합한다. | — | [31] |
| 팀 버프(전장 목표) | 특정 전장 목표 달성으로 팀에게 제공하는 강화 효과. | 개인 아이템 구매 효과와 구별한다. | 중립 목표 처치로 팀 버프를 확보한다. | — | [31] |

<a id="gd-1-31"></a>
### 1.31 오토배틀러

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 오토배틀러(Auto Battler) | 유닛을 선택·구성·배치한 뒤 그 팀의 전투 해결을 중심으로 라운드를 진행하는 양식. | 자동전투 기능이 있는 모든 RPG와 구별한다. | 준비 단계에 팀을 구성하고 다음 전투 결과를 확인한다. | 자동 실행의 범위와 전투 중 입력은 작품별. | [84], [38] |
| 벤치(Bench, 오토배틀러) | 보유했지만 현재 전장에 투입하지 않은 유닛을 저장하는 공간. | 전장의 배치 칸과 구별한다. | 구매한 유닛을 벤치에 두고 다음 조합을 준비한다. | — | [84] |
| 상점(오토배틀러) | 비용을 지불해 얻을 유닛 후보를 제공하는 공간·절차. | 영구 유료 상점과 구별한다. | 상점 후보에서 팀에 맞는 유닛을 구매한다. | — | [84] |
| 공유 유닛 풀(Shared Pool) | 여러 참가자의 상점 후보가 함께 사용하는 유닛 공급 집합. | 플레이어마다 독립된 무한 공급과 구별한다. | 다른 참가자의 구매가 남은 유닛 풀에 영향을 준다. | 구체 공급량·회수 규칙은 작품별. | [84] |
| 리롤(Reroll, Refresh) | 비용을 지불해 상점 후보를 새로 뽑는 선택. | 기존 구매 유닛을 초기화하는 것과 구별한다. | 필요한 유닛을 찾기 위해 상점을 리롤한다. | — | [84] |
| 상점 잠금(Lock) | 다음 자동 갱신에서도 현재 상점 후보를 유지하는 설정. | 구매 확정이나 유닛 예약 소유와 구별한다. | 지금 살 수 없는 후보를 위해 상점을 잠근다. | — | [84] |
| 유닛 합성(오토배틀러) | 같은 유닛의 중복 보유를 결합해 더 강한 유닛으로 바꾸는 것. | 다른 종류 유닛의 특성 조합과 구별한다. | 중복 유닛을 모아 높은 단계로 합성한다. | 요구 개수는 작품별. | [84] |
| 특성 시너지(Trait Synergy) | 배치 유닛의 소속·클래스 조합이 조건을 충족해 주는 보너스. | 개별 유닛 합성과 구별한다. | 같은 특성 유닛을 함께 배치해 시너지를 활성화한다. | 활성 조건·중복 계산은 작품별. | [84] |
| 유닛 티어(Tier) | 유닛의 가격·출현 등급을 나누는 분류. | 중복 합성으로 올리는 개체 단계와 구별한다. | 상점에서 높은 티어의 유닛을 찾는다. | — | [84] |
| 이자(오토배틀러) | 보유 화폐량에 따라 다음 수입에 더해지는 추가 화폐. | 승리·연승 보상과 구별한다. | 화폐를 보유해 다음 준비 단계의 이자를 얻는다. | — | [84] |
| 전장 인원 한도(Unit Cap) | 동시에 배치할 수 있는 팀 유닛 수의 상한. | 벤치 보유 한도와 구별한다. | 레벨이 높아지면 전장에 더 많은 유닛을 배치한다. | — | [84] |

<a id="gd-1-32"></a>
### 1.32 몰입형 시뮬레이션

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 몰입형 시뮬레이션(Immersive Sim) | 상호작용하는 규칙·환경과 다양한 행동 수단으로 플레이어가 문제의 해결 방법을 선택하게 하는 설계 양식. | 현실 직업 재현이나 시각적 몰입만과 구별한다. | 같은 목표를 환경·도구·행동의 다른 조합으로 해결한다. | 원래 혼합 게임의 설계 설명이었고 현재는 경계가 논쟁적인 장르명으로도 쓰인다. | [85] |
| 다중 해법(Alternative Solutions) | 같은 목표·문제에 서로 다른 유효 해결 방법을 제공하는 구조. | 하나의 정답에 도달하는 장식적 경로 차이와 구별한다. | 잠금 해제와 우회 침입 중 방법을 선택한다. | — | [85] |
| 다중 경로(Multiple Paths) | 목표 공간에 접근하는 여러 공간적 통로를 제공하는 구조. | 다중 해법 전체와 동의어는 아니다. | 정문과 옥상에서 서로 다른 접근을 시도한다. | — | [85] |
| 시스템 상호작용(System Interaction) | 한 규칙의 결과가 다른 규칙의 입력·상태가 되어 결합 효과를 만드는 것. | 독립 기능들의 단순 병치와 구별한다. | 물체 이동이 감시 행동과 경로 선택에 영향을 준다. | — | [85] |
| 창발적 해결(Emergent Solution) | 제한된 규칙들의 조합으로 개별 장면에 고정 작성되지 않은 해결을 만들어내는 것. | 미리 정해진 분기 선택과 구별한다. | 물체와 이동 규칙을 조합해 예상 밖의 접근로를 만든다. | 창발은 무작위 결과와 동의어가 아니다. | [85] |
| 플레이어 행위 가능성(Agency) | 플레이어의 선택·행동이 세계와 결과에 의미 있는 차이를 만들 수 있는 성질. | 선택지 개수만과 구별한다. | 계획과 실행 방식에 따라 같은 문제의 결과가 달라진다. | 몰입형 시뮬레이션만의 전용 개념은 아니다. | [85] |

<a id="gd-2"></a>
## 2. 장르 공용 명칭 사전

<a id="gd-2-1"></a>
### 2.1 기본 개념

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 게임(game) | 규칙에 따라 플레이어가 행동하고 상태나 결과에 영향을 주는 놀이 체계. 정해진 최종 승패가 없는 형태도 포함한다. | 매체·소재보다 규칙과 참여 방식으로 식별한다. | 플레이어는 이동과 자원 배분으로 도시의 상태에 영향을 준다. | [86]: 고전 모델은 가변적·정량적 결과를 강조하며 이후 확장을 인정; [87]: 목표 지향 활동과 게임 안의 자유 놀이를 구별. | [86], [87] |
| 플레이(play) | 플레이어가 게임에 참여하여 조작·선택·탐색 등을 수행하는 활동. | 게임은 체계, 플레이는 그 체계를 이용하는 실제 활동이다. | 플레이는 탐색에서 전투로 이어진다. | [87]: 자유 놀이인 playing과 목표 지향 gaming을 구별; 여기서는 게임 참여를 뜻한다. | [87] |
| 게임플레이(gameplay) | 규칙과 시스템 안에서 이루어지는 플레이어의 행동·선택·상호작용 구조. | 영상·음악의 표현과 구별하되 그 표현이 행동 판단에 영향을 줄 수 있다. | 게임플레이는 채집한 자원을 제작과 거래에 배분하는 선택으로 구성된다. | — | [87], [88] |
| 규칙(rule) | 가능한 행동, 조건, 상태 변화와 결과를 정하는 기준. | 행동을 실행하는 메커니즘과 그 실행을 허용·제한하는 기준을 구별한다. | 체력이 0이 되면 현재 시도를 종료하는 규칙을 적용한다. | [86]: 명확히 집행할 수 있는 기준; [88]: 상호작용의 가능 공간과 상태 전이를 규율. | [86], [88] |
| 메커니즘·메커닉(mechanic) | 주체가 규칙 안에서 게임 상태와 상호작용하는 구체적인 작동 방식. | 무엇을 할 수 있고 어떻게 상태를 바꾸는지 설명한다. | 끌어당기기 메커니즘으로 상자를 발판 가까이 이동한다. | [88]: 주체가 호출하는 행동 방법; 같은 글의 MDA 소개: 데이터·알고리즘 구성요소까지 포함. | [88] |
| 시스템(system) | 관련 규칙·상태·메커니즘이 함께 작동하는 체계. | 단일 행동보다 여러 요소의 관계와 작동을 묶어 말한다. | 거래 시스템은 가격, 재고, 구매 조건을 함께 처리한다. | — | [88] |
| 콘텐츠(content) | 플레이하거나 감상하도록 제공되는 스테이지·임무·캐릭터·이야기 등의 내용. | 이를 처리하는 공통 규칙·기술 체계와 구별한다. | 신규 콘텐츠로 탐험 구역과 대화 이야기를 추가한다. | — | [6], [89] |
| 핵심 메커니즘(core mechanic) | 주요 목표나 보상 상태에 도달하기 위해 반복 사용하는 중심 작동 방식. | 단순히 자주 누르는 입력과 목표에 기여하는 중심 행동을 구별한다. | 핵심 메커니즘은 자원의 흐름을 연결하고 조절하는 것이다. | [88]: 반복 행동 일반보다 체계가 보상하는 상태 달성에 기여하는 행동을 강조. | [88] |

<a id="gd-2-2"></a>
<a id="22-주체대상행동"></a>
### 2.2 주체·대상·행동

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 플레이어(player) | 게임에 참여하여 행동과 선택을 수행하는 참가자. | 조작 대상인 캐릭터와 조작 주체를 구별한다. | 플레이어는 두 경로 중 하나를 선택한다. | [87]: 보통 인간 참가자지만 설계 모델에서는 AI·여러 인간이 맡는 추상 참여 역할도 포함. | [87] |
| 캐릭터(character) | 게임 안에서 인물이나 생물 등의 역할과 특성을 갖는 존재. | 모든 물체를 뜻하는 오브젝트보다 역할·정체성이 강조된다. | 캐릭터마다 이동 속도와 대화 반응이 다르다. | — | [88], [6] |
| 아바타(avatar) | 게임 공간에서 플레이어를 나타내는 표현 또는 대리 존재. | 캐릭터 모두가 플레이어를 대리하는 것은 아니다. | 플레이어는 자신의 아바타 외형을 변경한다. | — | [6] |
| NPC(non-player character) | 플레이어가 직접 조작하지 않는 캐릭터. | 적뿐 아니라 상인·동료·주민도 포함한다. | NPC는 시간대에 따라 상점을 열고 닫는다. | [6]: 컴퓨터 제어 및 직접 조작하지 않는 캐릭터; 비디지털 역할극에서는 진행자가 맡을 수 있다. | [6] |
| 오브젝트(object) | 게임 안에서 식별되고 속성이나 상태를 갖는 대상. | 반드시 캐릭터나 상호작용 가능한 물체일 필요는 없다. | 문 오브젝트는 잠김 상태와 열림 상태를 가진다. | — | [88] |
| 입력(input) | 조작 장치에서 게임으로 전달되는 버튼·방향·터치 등의 신호. | 입력 신호와 규칙상 수행되는 행동은 일대일 관계가 아닐 수 있다. | 같은 버튼 입력이 문 앞에서는 열기, 상자 앞에서는 들기로 해석된다. | — | [88] |
| 행동(action) | 주체가 게임 안에서 수행하는 이동·공격·대화 등의 행위. | 입력은 신호, 행동은 게임 안에서 실행되는 행위이다. | 공격 행동에는 스태미나가 필요하다. | — | [88] |
| 선택(choice) | 가능한 대안 중 하나를 결정하는 행위. | 자동으로 실행되는 행동과 대안을 고르는 결정을 구별한다. | 플레이어는 자원을 수리와 새 장비 구매 중 어디에 쓸지 선택한다. | — | [87], [88] |
| 상호작용(interaction) | 주체가 대상이나 다른 주체에 작용하고 이에 대한 반응을 받는 관계. | 단순히 바라보는 것과 상태·응답에 영향을 주는 참여를 구별한다. | 손잡이와 상호작용하면 문이 열린다. | — | [86], [88] |

<a id="gd-2-3"></a>
<a id="23-상태조건판정"></a>
### 2.3 상태·조건·판정

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 속성(property) | 대상의 성질을 나타내는 값이나 특징. | 속성 이름과 그 시점에 저장된 구체적 값을 구별한다. | 무게 속성은 운반 가능 여부를 결정한다. | — | [88] |
| 상태(state) | 특정 시점에 게임이나 대상이 갖는 값과 상황의 조합. | 한순간 발생하는 사건과 지속되는 현재 상황을 구별한다. | 문은 잠김 상태이며 열쇠를 쓰면 열림 상태가 된다. | — | [86], [88] |
| 사건·이벤트(game event) | 게임 진행 중 발생해 규칙 처리나 반응의 계기가 되는 일. | 기간 한정 운영 콘텐츠인 이벤트와 구별한다. | 사망 사건이 발생하면 보유 자원 일부를 바닥에 남긴다. | — | [86], [88] |
| 상태 변화(state change) | 이전 상태가 규칙과 행동의 결과로 다른 상태가 되는 것. | 현재 상태 자체가 아니라 전후의 차이를 뜻한다. | 수리 후 장비 상태가 파손에서 정상으로 바뀐다. | — | [88] |
| 조건(condition) | 행동이나 결과를 허용·발생시키기 위해 충족해야 하는 기준. | 조건은 참인지 확인할 기준, 비용은 지급하거나 소모할 부담이다. | 열쇠 보유 조건을 만족해야 문을 열 수 있다. | — | [88] |
| 제약(constraint) | 행동·선택·상태가 가질 수 있는 범위를 제한하는 규칙. | 목표는 달성할 상태, 제약은 허용 범위이다. | 휴대 중량 제약으로 모든 전리품을 가져갈 수 없다. | — | [88] |
| 비용(cost) | 행동을 수행하거나 대상을 얻기 위해 지급·소모하는 자원이나 부담. | 보유만 요구하는 조건과 실제 차감되는 값을 구별한다. | 제작 비용으로 광석을 소비한다. | — | [88], [6] |
| 판정(resolution) | 규칙에 따라 입력·행동·사건의 성립 여부나 결과를 결정하는 처리. | 결과를 보여 주는 피드백과 결과를 결정하는 처리를 구별한다. | 공격 범위와 대상 위치를 비교해 명중을 판정한다. | — | [86], [88] |
| 초기화(reset) | 지정된 범위의 상태를 시작값이나 정해진 기준값으로 되돌리는 처리. | 전부 삭제와 동일하지 않으며 초기화 범위를 따로 지정한다. | 라운드 시작 때 체력만 초기화하고 장비는 유지한다. | — | [6] |
| 트리거(trigger) | 정해진 조건이나 사건을 감지해 후속 처리를 시작하는 계기. | 조건 전체와 그 조건 성립으로 작동을 시작시키는 연결을 구별한다. | 구역 진입 트리거가 경보를 시작한다. | — | [88] |

<a id="gd-2-4"></a>
<a id="24-목표결과보상"></a>
### 2.4 목표·결과·보상

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 목표(goal) | 플레이어가 달성하려는 상태나 결과. | 시스템이 부여하거나 플레이어가 스스로 정할 수 있다. | 이번 임무의 목표는 제한 시간 안에 출구에 도착하는 것이다. | [86]: 고전 모델은 결과의 가치로 목표를 설명하며 자유형 시뮬레이션은 명시 목표가 없을 수 있음. | [86], [88] |
| 도전(challenge) | 원하는 결과를 얻기 위해 노력·판단·기술이 필요한 상황. | 어려움의 정도인 난도와 해결해야 하는 상황을 구별한다. | 움직이는 발판 구간은 이동 타이밍을 판단하는 도전이다. | — | [88] |
| 성공(success) | 정해진 목표나 수행 조건을 충족한 결과. | 행동·구간의 성공과 경기 전체의 승리를 구별한다. | 잠금 해제에 성공하면 다음 방으로 이동한다. | — | [86], [88] |
| 실패(failure) | 목표나 수행 조건을 충족하지 못한 결과. | 실패해도 재시도·계속 진행이 가능할 수 있다. | 제한 시간 내 탈출하지 못하면 임무 실패로 처리한다. | — | [86], [88] |
| 승리(victory) | 경쟁이나 게임의 승리 조건을 충족한 최종 또는 구간 결과. | 개별 행동의 성공보다 해당 경쟁 단위의 결과를 뜻한다. | 목표 점수를 먼저 달성한 팀이 승리한다. | — | [86] |
| 패배(defeat) | 경쟁이나 게임의 패배 조건에 해당한 결과. | 캐릭터 사망이 항상 팀의 패배는 아니다. | 모든 팀원이 탈락하면 패배한다. | — | [86] |
| 점수(score) | 수행 결과나 성과를 규칙에 따라 수치로 표현한 값. | 능력치를 올리는 경험치와 평가·순위 값을 구별한다. | 목표물을 연속 명중하면 추가 점수를 받는다. | — | [86], [6] |
| 보상(reward) | 행동·달성·참여의 대가로 제공되는 이익이나 긍정적 결과. | 비용과 반대 방향이며 반드시 아이템이나 화폐일 필요는 없다. | 구역 발견 보상으로 새 이동 경로를 해금한다. | — | [88], [6] |
| 업적(achievement) | 지정된 도전이나 수행 기록을 달성했다는 별도 기록. | 진행에 필요한 목표와 독립적으로 존재할 수 있다. | 피해 없이 임무를 완료하면 업적이 기록된다. | — | [6] |

<a id="gd-2-5"></a>
<a id="25-자원보유경제"></a>
### 2.5 자원·보유·경제

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 자원(resource) | 행동·생산·유지 등에 활용하며 획득·배분·소모할 수 있는 값이나 대상. | 화폐·재료·체력처럼 기능이 다르며 모든 수치가 자원인 것은 아니다. | 전투와 이동이 같은 스태미나 자원을 소비한다. | — | [90] |
| 아이템(item) | 획득·보유·사용 등 개별 단위로 다루는 게임 내 물품. | 항상 장착 가능하거나 소비되는 것은 아니다. | 열쇠 아이템은 문을 열어도 사라지지 않는다. | — | [6] |
| 장비(equipment) | 캐릭터나 유닛에 장착해 기능·능력·외형을 적용하는 물품. | 소모품처럼 즉시 소비하는 사용과 장착 상태를 구별한다. | 방어 장비를 장착하면 받는 피해가 줄어든다. | — | [6] |
| 로드아웃(loadout) | 경기·라운드·임무 전에 선택해 두는 장비·능력·물품의 조합. | 인벤토리 전체와 다르며, 빌드 중 경기·라운드·임무 전에 선택해 가져갈 구성을 가리킬 수 있다. 두 용어의 범위는 작품에 따라 겹친다. | 출격 전에 임무에 맞는 로드아웃을 선택한다. | — | [6] |
| 화폐(currency) | 가격 표시·구매·교환에 사용하는 게임 내 가치 단위. | 재료와 사용처가 겹치더라도 교환 기준 역할이 핵심이다. | 상점에서 화폐를 지불해 수리 재료를 구매한다. | — | [90] |
| 인벤토리(inventory) | 플레이어·캐릭터가 보유한 물품을 저장하고 관리하는 보유 공간 또는 목록. | 인벤토리를 보여 주는 화면과 실제 보유 데이터를 구별한다. | 인벤토리 용량이 가득 차면 새 물품을 줍지 못한다. | [6]: 물품을 선택·사용·장착하는 화면 영역도 뜻함. | [6] |
| 획득(acquisition) | 자원·물품·권한 등을 새로 보유하게 되는 변화. | 제작·구매·발견 등 획득 경로는 별도 메커니즘이다. | 적을 처치하면 재료를 획득한다. | — | [90] |
| 소비(consumption) | 사용 목적에 따라 보유 자원이나 물품을 차감·소진하는 처리. | 장비 장착과 보유만 요구하는 조건을 구별한다. | 회복약을 소비하면 체력이 증가한다. | — | [90] |
| 거래(trade) | 주체 사이에서 물품·자원·화폐를 교환하는 행동. | 단독 제작처럼 재료를 결과물로 바꾸는 변환과 구별한다. | 플레이어는 재료를 판매해 화폐를 얻는다. | — | [90] |
| 전리품(loot) | 적·상자·탐험 등의 결과로 얻는 물품이나 자원. | 획득물의 출처·맥락을 나타내며 모든 보상과 동일하지 않다. | 방을 탐색한 뒤 전리품 중 필요한 장비만 가져간다. | — | [6] |
| 희귀도(rarity) | 획득물의 희소성 등을 단계로 구분하여 표시한 등급. | 실제 획득 확률·품질·성능은 별도 규칙이며 희귀도 명칭만으로 같다고 단정하지 않는다. | 전리품은 희귀도 등급을 표시하며 획득 확률은 별도 표로 제공한다. | [2]: 루터 슈터에서 품질·속성·특성이 희귀도 단계와 함께 무작위 생성됨; 등급별 세부 관계는 작품마다 다름. | [2] |
| 체력(health·HP) | 생존이나 전투 지속 가능성을 나타내는 자원 값. | 방어력은 피해 계산 속성, 체력은 피해를 받아 줄어드는 값이다. | 체력이 0이 되면 캐릭터가 쓰러진다. | — | [6] |
| 스태미나(stamina) | 달리기·회피·공격 등 신체 행동의 수행량을 제한하는 자원. | 체력의 감소와 행동 가능량의 감소를 구별한다. | 회피와 강공격이 스태미나를 함께 소비한다. | [6]: stamina가 체력·방어 능력치 뜻으로도 사용; 여기서는 행동 자원에 한정. | [88], [6] |
| 쿨다운(cooldown) | 행동을 사용한 뒤 다시 사용할 때까지 기다려야 하는 시간. | 자원 비용과 시간 제약을 구별한다. | 스킬 사용 후 쿨다운이 끝나야 다시 사용할 수 있다. | — | [6] |

<a id="gd-2-6"></a>
<a id="26-시간진행성장"></a>
### 2.6 시간·진행·성장

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 플레이 세션(play session) | 플레이어가 한 번에 이어서 플레이하는 시간 구간. | 게임 전체 완료 단위나 서버 방과 동일하지 않다. | 짧은 플레이 세션 안에 한 임무를 완료할 수 있다. | [87]: 연속성은 플레이어 판단을 포함; game session은 한 게임 인스턴스에서의 모든 play session을 합친 뜻. | [87] |
| 경기(match) | 참가자와 시작·종료 조건을 갖는 하나의 경쟁 또는 협동 플레이 단위. | 한 경기는 여러 라운드로 구성될 수 있다. | 경기는 세 라운드의 합산 결과로 종료된다. | — | [6] |
| 라운드(round) | 경기나 반복 활동 안에서 규칙상 구분되는 한 회차. | 개별 주체의 행동 기회인 턴과 구별한다. | 라운드가 끝나면 배치를 변경할 수 있다. | — | [6] |
| 턴(turn) | 규칙에 따라 행동하거나 명령을 정하는 차례·처리 단위. | 반드시 한 플레이어만 순차 행동하는 것은 아니다. | 각 턴에 모든 플레이어가 명령을 제출한 뒤 함께 처리한다. | — | [6] |
| 런(run) | 시작부터 종료·실패까지 이어지는 한 번의 시도. | 세션이 끊겨도 저장해 이어지는 같은 런일 수 있다. | 현재 런이 끝나면 런 안에서 획득한 임시 효과를 제거한다. | — | [91] |
| 스테이지·레벨(공간)(stage·level) | 구역·과제·적 배치 등으로 구분한 플레이 공간 또는 진행 구간. | 캐릭터 성장 단계인 레벨과 구별한다. | 스테이지마다 다른 장애물 조합을 배치한다. | [6]: level은 공간뿐 아니라 단일 공간의 난도 회차도 지칭. | [6] |
| 진행(progression) | 과제·이야기·공간·콘텐츠를 거치며 플레이 상황이 다음 단계로 이어지는 과정. | 능력 증가인 성장 없이도 진행할 수 있다. | 열쇠를 찾으면 다음 구역으로 진행한다. | — | [6] |
| 성장(growth) | 플레이 결과로 캐릭터·계정·시설 등의 능력이나 가능 범위가 증가하는 변화. | 플레이어의 실제 기술 향상인 숙련과 구별한다. | 장비 강화는 캐릭터의 전투 성장을 제공한다. | — | [88], [6] |
| 숙련(mastery) | 경험·연습을 통해 플레이어가 규칙 이해와 수행 기술을 높이는 것. | 캐릭터 수치 상승 없이도 이루어진다. | 반복 연습으로 플레이어의 회피 타이밍 숙련이 높아진다. | — | [88] |
| 경험치(experience point·XP·EXP) | 활동 결과를 성장 단계에 반영하기 위해 누적하는 수치. | 경기 성과를 평가하는 점수와 구별한다. | 임무 경험치가 누적되면 캐릭터 레벨이 오른다. | — | [6] |
| 레벨(성장)(experience level) | 캐릭터·장비·계정 등의 성장 정도를 단계로 표시한 값. | 공간 레벨이나 플레이어의 실제 숙련과 구별한다. | 캐릭터 레벨이 오르면 기본 능력치가 증가한다. | — | [6] |
| 해금(unlock) | 조건 충족으로 이전에 접근·사용할 수 없던 콘텐츠나 기능을 이용 가능하게 하는 변화. | 기존 기능의 성능만 높이는 업그레이드와 구별한다. | 탐험 목표를 완료하면 새 이동 수단을 해금한다. | — | [6] |
| 업그레이드(upgrade) | 기존 캐릭터·물품·시설 등의 성능이나 기능을 개선하는 처리. | 새 대상을 사용할 권한을 얻는 해금과 구별한다. | 생산 시설 업그레이드로 처리량을 높인다. | — | [6] |
| 영구 사망(permadeath) | 사망한 캐릭터나 그 시도의 진행을 되살려 이어갈 수 없도록 하는 규칙. | 일시 탈락·리스폰과 구별하며 다른 캐릭터나 후속 런은 계속될 수 있다. | 캐릭터는 영구 사망하지만 다른 팀원으로 캠페인을 계속한다. | [6]: 전체 시도 재시작 또는 개별 캐릭터의 영구 제외라는 두 범위가 있음. | [6] |
| 리스폰(respawn) | 사망·소멸 뒤 캐릭터나 대상이 다시 나타나는 처리. | 같은 대상의 재등장과 새 시도 시작을 구별한다. | 탈락한 플레이어는 일정 시간 뒤 지정 구역에서 리스폰한다. | — | [6] |

<a id="gd-2-7"></a>
### 2.7 공간·시점·모드

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 맵(map) | 게임 공간의 배치 또는 그 배치를 나타내는 지도. | 실제 플레이 공간과 지도를 뜻할 때 문맥을 명시한다. | 맵 화면에 발견한 경로만 표시한다. | [6]: 플레이 공간·레벨 자체를 뜻하기도 함. | [6] |
| 구역(area·zone) | 경계·기능·규칙 등으로 구분한 게임 공간의 일부. | 하나의 맵에 여러 구역이 있을 수 있다. | 이 구역에서는 전투 행동을 금지한다. | — | [6] |
| 경로(path·route) | 출발지에서 목적지로 이동할 수 있는 연결과 이동 순서. | 방문할 공간인 구역과 공간을 잇는 방법을 구별한다. | 지하 경로는 짧지만 위험한 적을 통과해야 한다. | — | [88], [6] |
| 오픈월드(open world) | 넓은 게임 공간에서 방문 장소·순서를 비교적 자유롭게 선택하는 구조. | 자유로운 규칙 실험인 샌드박스와 동일하지 않다. | 오픈월드에서 임무 순서와 방문 지역을 선택한다. | — | [6] |
| 시점(perspective) | 플레이 공간과 대상을 바라보는 관찰 위치·방식. | 그래픽의 차원, 조작 방식, 장르와 별도 속성이다. | 고정 시점은 방 전체의 위험 요소를 한눈에 보여 준다. | — | [6] |
| 1인칭(first-person) | 조작하는 인물의 눈이나 그에 대응하는 위치에서 공간을 보는 시점. | 총 사용 여부와 관계없이 시점을 뜻한다. | 1인칭 시점에서는 손과 도구를 화면 앞에 표시한다. | — | [6] |
| 3인칭(third-person) | 조작 대상 바깥의 카메라 위치에서 그 대상과 주변을 보는 시점. | 인물의 눈 위치에서 보는 1인칭과 구별한다. | 3인칭 카메라로 캐릭터의 이동 방향을 확인한다. | — | [6] |
| 캠페인(campaign) | 이야기나 진행 상태로 연결된 여러 임무·경기·시나리오의 묶음. | 개별 경기보다 이어지는 전체 진행 단위를 뜻한다. | 캠페인의 자원과 선택 결과를 다음 임무에 이어 반영한다. | — | [6] |
| 보스러시(boss rush) | 보스와의 연속 대결을 중심으로 구성한 모드나 구간. | 일반 구간을 포함한 캠페인과 보스전 중심 구성을 구별한다. | 보스러시에서는 각 전투 사이에 장비를 변경한다. | — | [92] |
| 하드코어 모드(hardcore mode) | 기본 모드보다 실패 부담·정보 제한·생존 조건 등을 강화한 특별 규칙 모드. | 시장 분류와 플레이어 성향이 아니라 해당 작품의 규칙을 뜻한다. | 하드코어 모드는 사망 후 같은 캐릭터의 재개를 허용하지 않는다. | [93]: 한 생명과 사망 후 관전; [6]: 영구 사망의 별칭으로도 사용. 작품별 세부 규칙은 다름. | [93], [6] |

<a id="gd-2-8"></a>
<a id="28-정보확률"></a>
### 2.8 정보·확률

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 정보(information) | 상태·규칙·대상 등에 관해 판단에 사용할 수 있는 내용. | 실제 상태와 플레이어에게 알려진 내용을 구별한다. | 화면은 체력 정보를 수치와 막대로 함께 전달한다. | — | [86], [94] |
| 단서(clue) | 숨은 사실·해법·다음 행동을 추론하는 데 도움을 주는 정보. | 정답이나 해결법을 직접 알려 주는 힌트와 정도가 다를 수 있다. | 발자국 단서로 이동 방향을 추론한다. | — | [95] |
| 공개 정보(public information) | 정해진 참가자 모두가 확인할 수 있는 정보. | 특정 주체만 볼 수 있는 비공개 정보와 구별한다. | 버림 더미는 모든 참가자에게 공개 정보로 제공한다. | — | [86], [6] |
| 비공개 정보(hidden·private information) | 일부 참가자만 알거나 현재 누구에게도 드러나지 않은 정보. | 누가 알 수 있는지를 함께 지정한다. | 각 플레이어의 패는 본인에게만 보이는 비공개 정보이다. | — | [86], [6] |
| 무작위성(randomness) | 정해진 가능 범위에서 결과를 무작위로 선택하는 성질. | 모르는 결과 전부가 무작위인 것은 아니다. | 전리품의 종류는 무작위성에 따라 달라진다. | — | [96] |
| 확률(probability) | 특정 조건에서 결과가 발생할 가능성을 표현한 값. | 실제 발생 결과나 보장 횟수와 구별한다. | 표시된 확률은 각 추첨에 적용한다. | — | [96] |
| 불확실성(uncertainty) | 앞으로 일어날 일이나 현재 숨은 사실을 확정하기 어려운 상태. | 확률·정보 부족·상대의 선택 등 여러 원인으로 생긴다. | 비공개 명령 때문에 상대의 다음 이동에 불확실성이 생긴다. | — | [86] |
| 시드(seed) | 의사난수 생성의 초기 상태를 정하는 입력 값. | 같은 시드라도 생성 알고리즘·호출 순서 등이 같아야 같은 결과를 재현한다. | 같은 버전과 시드로 생성한 맵을 비교한다. | — | [96] |
| 절차 생성(procedural generation) | 정해진 알고리즘·규칙으로 맵·배치·콘텐츠 등을 생성하는 방식. | 모든 결과를 사람이 개별 제작하는 방식과 구별하며 무작위성은 선택 요소이다. | 절차 생성은 연결 조건을 만족하는 방 배치를 만든다. | [6]: 무작위성을 활용하는 레벨·월드 생성 설명에 집중. | [6] |

<a id="gd-2-9"></a>
### 2.9 인터페이스·피드백

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| UI(user interface) | 플레이어가 정보 확인·명령 입력·설정 등을 수행하는 접점과 표시 체계. | 플레이 중 표시인 HUD와 메뉴를 모두 포함한다. | UI는 현재 자원과 가능한 행동을 함께 표시한다. | — | [89], [94] |
| HUD(head-up display) | 플레이 화면 위에서 체력·점수·목표 등 필요한 정보를 표시하는 인터페이스. | 별도 설정 화면이나 메뉴 전체를 뜻하지 않는다. | HUD에 잔탄과 재장전 진행을 표시한다. | — | [89] |
| 메뉴(menu) | 명령·항목·설정 등의 선택지를 목록이나 계층으로 제시하는 인터페이스. | 플레이 공간에서의 직접 행동과 메뉴 항목 선택을 구별한다. | 메뉴에서 저장 슬롯을 선택한다. | — | [89], [94] |
| 피드백(game feedback) | 입력·행동·상태·결과를 플레이어가 알도록 전달하는 시각·소리·촉각 등의 반응. | 이용자가 개발자에게 주는 의견인 사용자 피드백과 구별한다. | 공격이 막히면 별도 소리와 효과로 피드백한다. | — | [88], [94] |
| 조작감(control feel) | 입력과 게임 반응의 연결에서 느끼는 반응성·일관성·움직임의 감각. | 난도나 조작키 수만으로 결정하지 않는다. | 입력 직후의 가속과 멈춤 반응을 조정해 조작감을 개선한다. | — | [88], [94] |
| 가독성(readability) | 글자·아이콘·상태 표시 등을 쉽게 구분하고 의미를 파악할 수 있는 성질. | 화면의 미적 선호와 필요한 정보의 식별 가능성을 구별한다. | 배경과 글자의 대비를 높여 자원 수치의 가독성을 개선한다. | — | [94] |
| 접근성(accessibility) | 장애나 감각·운동·인지 제약 등이 있는 사람도 게임에 참여할 수 있도록 장벽을 줄이는 성질. | 단순히 쉬운 난도나 넓은 시장 대중성과 동일하지 않다. | 자막과 입력 재설정으로 접근성을 높인다. | [94]: 감각·운동·인지 등 여러 배제 장벽을 다룸; 캐주얼 시장의 low barrier와 구별. | [94] |
| 난도(difficulty) | 과제 달성에 필요한 판단·기술·노력과 실패 부담의 정도. | 특정 플레이어의 숙련과 게임이 요구하는 부담을 함께 고려한다. | 적의 공격 빈도와 재시도 부담을 조절해 난도를 낮춘다. | — | [86], [94] |
| 튜토리얼(tutorial) | 조작·규칙·판단 방법을 학습하도록 안내하는 내용이나 구간. | 목표 수행 중 필요할 때 주는 힌트와 학습 구성을 구별한다. | 튜토리얼에서 안전하게 회피를 연습한다. | — | [94] |

<a id="gd-2-10"></a>
<a id="210-공통-시스템"></a>
### 2.10 공통 시스템

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 이동(movement) | 주체나 대상의 위치를 게임 공간 안에서 바꾸는 행동. | 속도·방향·충돌 규칙은 이동의 세부 조건이다. | 이동 중 장애물과 충돌하면 멈춘다. | — | [88] |
| 탐험(exploration) | 공간을 조사·이동하며 장소·대상·경로·정보를 발견하는 활동. | 정해진 목적지까지 단순 이동하는 것보다 발견이 중심이다. | 탐험으로 숨은 자원과 지하 경로를 발견한다. | — | [90], [97] |
| 전투(combat) | 상대에게 피해·제압 등을 가하고 이에 대응하는 규칙적 대결. | 경쟁 전체와 피해·방어 행동을 통한 대결을 구별한다. | 전투에서는 공격과 방어가 같은 자원을 사용한다. | — | [98] |
| 제작(crafting) | 재료·작업 등의 조건을 사용해 아이템을 만드는 행동. | 공간 구조물을 만드는 건설과 반복 산출 과정인 생산을 구별한다. | 채집한 재료로 회복약을 제작한다. | [99]: 게임 아이템을 만드는 활동; [6]: 다른 아이템의 조합을 특히 강조. | [99], [6] |
| 건설(construction·building) | 게임 공간에 구조물·시설 등을 만들거나 배치하는 행동. | 아이템 제작과 구조물의 공간 배치를 구별한다. | 자원을 지불하고 빈 부지에 창고를 건설한다. | [97]: 요소 재배치·코드·서사 구성까지 포괄하는 넓은 패턴; 여기서는 공간 구조물에 한정. | [97], [41] |
| 생산(production) | 자원·시설·작업 등을 통해 물품이나 유닛을 산출하는 과정. | 획득은 보유 변화, 생산은 산출을 만드는 과정이다. | 생산 시설은 원료를 투입받아 부품을 반복 생산한다. | — | [90], [41] |
| 대화(dialogue) | 캐릭터나 주체 사이에서 말·응답·선택지를 주고받는 상호작용. | 일방적으로 재생하는 대사와 응답에 따라 전개되는 상호작용을 구별한다. | 대화 선택에 따라 NPC의 협조 여부가 달라진다. | — | [6] |
| 관계(캐릭터)(relationship) | 캐릭터 사이의 친밀·신뢰·적대 등 연결 상태. | 플레이어 사이의 접속·사회적 기능과 게임 안 캐릭터 관계를 구별한다. | 선물을 주면 캐릭터 관계의 친밀도가 증가한다. | — | [46] |
| 저장(save) | 이후 재개를 위해 지정된 게임 상태를 보존하는 처리. | 자동 진행 기록과 저장 대상·시점을 명시해야 한다. | 임무 종료 때 장비와 진행 상태를 저장한다. | — | [6], [94] |
| 불러오기(load) | 보존된 상태를 복원해 그 상태에서 플레이를 재개하는 처리. | 새 게임 초기화와 이전 상태 복원을 구별한다. | 저장 슬롯을 불러오면 마지막 저장 상태에서 재개한다. | — | [6] |
| 체크포인트(checkpoint) | 실패·사망 뒤 재개 위치나 기준 상태로 사용하는 진행 지점. | 종료 후에도 보존하는 저장 파일과 별개일 수 있다. | 사망하면 마지막 체크포인트에서 재개한다. | — | [6] |
| 회피(dodge·evade) | 위치 이동이나 회피 상태를 이용해 공격의 영향을 피하는 행동. | 방어로 충격을 받아 막는 행동과 구별하며 무적 여부는 별도 규칙이다. | 회피 중에도 무적이 없으므로 공격 범위에서 벗어나야 한다. | — | [78] |
| 패링(parry) | 공격에 맞춘 방어 행동으로 공격을 쳐내거나 무효화하는 것. | 지속 가드와 타이밍·성공 판정을 갖는 방어를 구별한다. | 패링 성공 시 상대의 자세를 무너뜨린다. | — | [6] |
| 가드·블록(guard·block) | 방어 자세나 수단으로 공격 피해·영향을 막거나 줄이는 행동. | 공격 자체를 피하는 회피와 구별한다. | 가드 방향이 맞으면 피해를 줄인다. | — | [100] |
| 군중 제어(crowd control·CC) | 대상의 이동·행동을 제한해 위협이나 전투 참여를 통제하는 효과. | 직접 피해와 행동 제한 효과를 구별한다. | 둔화와 기절로 적의 접근을 제한한다. | [6]: MMO에서 적의 위협·수적 참여를 줄이는 전술을 강조; 개별 기술 효과로도 사용. | [6] |
| 콤보(공격)(attack combo) | 여러 공격을 규칙상 이어 수행하는 연속 공격. | 단순 동시 공격이나 여러 효과의 시너지와 구별한다. | 첫 공격이 명중하면 후속 공격으로 콤보를 이어 간다. | [6]: 상대가 피격 중 방어할 수 없는 연속 공격에 초점; 다른 액션 용례는 공격 연계 전체를 지칭할 수 있음. | [6] |
| 콤보(연속 성공)(success streak) | 실수 없이 이어진 판정 성공의 누적 횟수나 상태. | 공격 연계 콤보와 구별한다. | 판정에 실패하면 연속 성공 콤보를 초기화한다. | — | [101] |
| 피해(damage) | 공격·위험 등의 결과로 체력·내구도 등에서 줄어드는 값이나 손상. | 공격력은 계산에 쓰는 성능, 피해는 실제 손실이다. | 화상은 시간이 지날 때마다 피해를 준다. | — | [6], [90] |
| 내구도(durability) | 물품·구조물이 사용이나 손상을 견딜 수 있는 정도를 나타내는 값. | 캐릭터 생존 자원인 체력과 대상·사용 맥락을 구별한다. | 사용으로 내구도가 감소하며 수리로 복구한다. | — | [80] |
| 무적 프레임(invincibility frame·i-frame) | 공격이나 피해 적용을 받지 않는 동작 중의 시간 구간. | 모든 회피에 존재하는 것은 아니며 적용되는 공격 종류를 명시한다. | 회피의 일부 구간에만 무적 프레임을 적용한다. | [6]: 피격 직후의 보호 시간을 flashing invulnerability로 별도 설명. | [102], [6] |

<a id="gd-2-11"></a>
### 2.11 참여·접속·사회적 기능

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 싱글플레이(single-player) | 하나의 플레이어가 참여하는 플레이 형태. | 인터넷 접속 여부나 NPC 수와 별개이다. | 싱글플레이에서도 계정 저장을 위해 접속이 필요하다. | — | [6] |
| 멀티플레이(multiplayer) | 둘 이상의 플레이어가 같은 규칙 관계 안에서 참여하는 플레이 형태. | 같은 장소·같은 시각에 참여할 필요는 없다. | 멀티플레이는 협동과 경쟁 모드를 제공한다. | — | [6] |
| 협동(cooperative play·co-op) | 참가자들이 공동 목표 달성을 위해 함께 행동하는 형태. | 경쟁 관계가 없다는 뜻이 아니라 해당 과제의 공동 목표가 기준이다. | 협동 임무에서 한 명은 장치를 조작하고 다른 한 명은 길을 확보한다. | — | [6] |
| 경쟁(competitive play) | 참가자가 상대보다 유리한 결과를 얻거나 서로 충돌하는 목표를 달성하려는 형태. | 같은 팀 안에서는 협동하면서 팀 사이에서는 경쟁할 수 있다. | 두 팀은 거점 점유 시간을 두고 경쟁한다. | — | [86], [6] |
| 동기 플레이(synchronous play) | 참가자들의 행동과 대응이 같은 진행 시간 안에서 이루어지는 형태. | 접속만 동시라고 해서 모든 상호작용이 동기인 것은 아니다. | 동기 플레이에서는 팀원이 같은 전투에 실시간으로 대응한다. | — | [6] |
| 비동기 플레이(asynchronous play) | 참가자가 같은 시각에 참여하지 않아도 서로의 행동·결과가 연결되는 형태. | 단순 싱글플레이와 다른 참가자의 상태를 활용하는 구조를 구별한다. | 다른 시각에 제출한 명령을 턴 종료 때 함께 처리한다. | — | [6] |
| 매칭(matchmaking) | 조건에 맞는 참가자를 경기·팀·방에 배정하는 처리. | 친구 초대나 임의 방 선택과 자동 조건 배정을 구별한다. | 실력과 연결 조건을 고려해 매칭한다. | — | [6] |
| MMO(massively multiplayer online) | 많은 플레이어가 온라인으로 공유 공간이나 지속적인 게임 구조에 참여하는 형태. | RPG에 한정되지 않으며 모든 참가자가 한 장면에 모일 필요는 없다. | MMO 월드는 여러 지역에 나뉜 참가자의 거래를 연결한다. | — | [6] |
| 소셜게임(social game) | 플레이어 사이의 관계·교류·공동체 경험을 주요 참여 요소로 삼는 온라인 게임 명칭. | SNS 플랫폼 기반 여부보다 관계 형성과 함께하는 경험을 뜻할 때의 용례이며 SNS 게임군을 가리키는 좁은 뜻도 있다. | 소셜게임은 친구 방문과 공동 과제로 참여자 사이의 관계를 이어 간다. | [103]: Facebook·모바일의 캐주얼 소셜게임과 MMO를 아우르는 관계·공동체 중심 분석; [104]: Facebook SNS 통합 게임군에 social games를 사용. | [103], [104] |
| SNS 게임(social network game·SNG) | SNS 플랫폼이나 그 친구 연결망과 통합해 플레이·교류하는 게임. | 독립 앱의 소셜 기능과 SNS 통합을 기준으로 구별한다. | SNS 게임은 연결된 친구 목록을 방문 대상에 사용한다. | [104]: Facebook 이용 경험 연구 범위이며 단독 플레이에 사회적 요소가 결합된 경험도 확인. | [104] |
| 소셜 기능(social feature) | 친구 연결·채팅·선물·길드·공동 과제 등 플레이어 사이의 관계와 상호작용을 지원하는 기능. | 게임 전체의 명칭이나 SNS 통합 여부와 별도로 개별 기능을 식별한다. | 소셜 기능으로 친구에게 선물을 보내고 길드의 공동 과제를 수행한다. | [105]: Social Interaction과 Competition & PvP를 기능군으로 분류; [103]: 관계 형성·유지와 동기·비동기 상호작용으로 설명. | [105], [103] |

<a id="gd-2-12"></a>
### 2.12 시장·플레이어·경험 명칭

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 캐주얼(시장·설계)(casual) | 낮은 학습·참여 부담으로 폭넓은 이용자가 쉽게 시작할 수 있도록 한 게임군·설계 성격. | 특정 난도·과금 방식·플레이어 성향 하나로 판정하지 않는다. | 단순 조작과 짧게 끊을 수 있는 과제로 캐주얼 참여를 지원한다. | [106]: 모바일 집계의 상위 범주; [107]: 캐주얼·미드코어·하드코어 스펙트럼; 플레이어 명칭과 구별. | [106], [107] |
| 캐주얼(플레이어)(casual player) | 비교적 낮은 몰입 부담이나 일상 중 편한 참여를 선호하는 플레이어 성향 명칭. | 캐주얼 게임을 한다는 사실만으로 플레이어를 분류하지 않는다. | 캐주얼 플레이어의 중단·재개 편의를 별도로 검토한다. | [108]: 낮은 헌신·강도, 자기분류, 참여 동기 등 여러 연구 기준이 다름. | [108] |
| 하이퍼캐주얼(hyper-casual) | 매우 단순한 핵심 조작과 즉시 시작하는 짧은 플레이 루프를 중심으로 한 모바일 시장 명칭. | 깊은 메타 성장·경제를 결합한 하이브리드캐주얼과 구별한다. | 한 동작으로 시작하는 하이퍼캐주얼 루프를 구성한다. | [109]: 빠른 플레이와 광고 중심 수익화에 초점; 광고만으로 장르를 판정하지 않음. | [109] |
| 하이브리드캐주얼(hybrid-casual) | 단순한 핵심 플레이에 메타 성장·경제·전략 등 지속 참여 층을 결합한 모바일 시장 명칭. | 여러 장르 혼합 전부를 뜻하는 것이 아니다. | 단순 퍼즐에 장기 업그레이드를 더해 하이브리드캐주얼 구조를 만든다. | [109]: 깊은 메타·루프·경제와 IAP·보상형 광고; [110]: 플레이 깊이·콘텐츠와 광고·IAP 결합. 수치 임계값은 공통 정의가 아님. | [109], [110] |
| 미드코어(midcore) | 캐주얼의 진입 편의와 코어 게임의 전략·성장·지속 참여 요소를 결합한 시장 명칭. | 하이브리드캐주얼과 일부 겹치지만 제공자의 시장 분류 기준을 확인한다. | 미드코어 구조는 간단한 전투 조작과 장기 파티 성장을 결합한다. | [106]: RPG·전략 등 장르를 묶는 모바일 범주; [107]: 캐주얼과 하드코어 성분의 중간형. | [106], [107] |
| 코어·하드코어(시장)(core·hardcore) | 깊이·복잡성·숙련 등을 중시하는 코어·하드코어 이용층을 겨냥한 게임군의 시장 명칭. | 플레이어의 성향과 게임 모드 규칙을 구별하며 두 명칭 사이에 별도 보편 경계를 두지 않는다. | 코어·하드코어 이용층을 겨냥해 정교한 전략 선택을 제공한다. | [111]: hardcore를 core의 별칭으로 쓰고 대상층에 맞춘 제작을 논함; [107]: 시장 스펙트럼 상단을 hardcore로 표기; [106]: 공식 상위 범주는 midcore이며 일대일 대응하지 않음. | [111], [107], [106] |
| 코어·하드코어(플레이어)(core·hardcore player) | 게임을 취미로 지속하며 참여·숙련·관련 정보에 높은 관심이나 헌신을 보이는 이용자 명칭. | 한 번의 어려운 모드 선택이나 시간·지출 한 값만으로 판정하지 않는다. | 코어·하드코어 플레이어의 숙련 추구와 참여 동기를 분리해 분석한다. | [111]: hardcore·core·traditional을 별칭으로 사용; [108]: 강도·헌신·자기분류·취미인·게임 문해력 등 여러 기준이 공존. | [111], [108] |
| 코지(cozy) | 안전감·충족감·부드러운 분위기를 중심으로 편안한 참여를 유도하는 경험 명칭. | 낮은 난도·캐주얼·무전투와 항상 같은 뜻은 아니다. | 위협을 완화하고 자원 부족 압박을 줄여 코지 경험을 구성한다. | [112]: 안전·풍요·부드러움의 경험 모델이며 개인에 따라 체감이 다름. | [112] |
| 릴랙싱(relaxing) | 긴장과 부담을 낮추고 이완을 유도하는 경험 성격. | 특정 미학과 안전·충족 모델인 코지보다 넓은 정서 표현이다. | 시간 압박을 제거해 릴랙싱한 정리 경험을 제공한다. | — | [108], [112] |

<a id="gd-2-13"></a>
<a id="213-제작유통운영매체"></a>
### 2.13 제작·유통·운영·매체

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 인디(indie) | 독립적인 제작 활동과 관련 문화·산업 맥락에 놓인 게임이나 제작자를 지칭하는 명칭. | 작은 팀·낮은 예산·픽셀 그래픽·자체 유통만으로 확정하지 않는다. | 인디 제작 배경은 자금 조달과 창작·유통 결정권을 구분해 서술한다. | [113]: independent는 자금·창작·유통 독립의 여러 관계; indie는 2000년대 중반 형성된 문화표지의 좁은 역사적 뜻도 있음. | [113] |
| 자금 독립성(financial independence) | 개발팀이 외부 투자자의 자금·제작 수단에 의존하지 않고 제작비를 조달하는 관계. | 회사 전체의 규모와 실제 개발팀의 조달 관계를 구별한다. | 개발팀은 제작 자금을 직접 조달한다. | [113]: 정부 지원·시설 제공 등 현금 외 제작 수단도 투자 관계에 포함. | [113] |
| 창작 독립성(creative independence) | 개발자가 자신을 의도된 청중으로 삼아 자신이 원하는 게임을 만드는 의미의 독립성. | 개발팀이 결정권을 가졌다는 사실만이 아니라 누구의 취향·요구를 목표로 만드는지 구별한다. | 개발팀은 시장 수요에 맞추기보다 자신이 즐기고 싶은 경험을 목표로 게임을 만든다. | [113]: 개발자와 의도된 청중의 관계를 기준으로 하며 자율적으로 시장 수요에 맞춰도 이 의미의 독립성을 잃을 수 있음. | [113] |
| 유통 독립성(publishing independence) | 개발자가 외부 퍼블리셔를 통하지 않고 직접 출판·출시하는 관계. | 상점 플랫폼 이용은 외부 퍼블리셔 계약과 동일하지 않다. | 개발팀은 최초 버전을 직접 출시한다. | [113]: 최초 출시에서 개발자와 퍼블리셔가 같은 주체인지 기준. | [113] |
| AAA(triple-A) | 큰 제작·마케팅 투자와 대규모 상업 출시를 전제로 한 산업 규모 명칭. | 특정 장르·완성도·매출 성공을 보장하는 등급이 아니다. | AAA 제작 규모와 플레이 규칙을 별도로 설명한다. | [6]: 고예산·대규모 개발팀을 강조; [113]: independent AAA처럼 독립성과 규모가 함께 표현될 수 있음. | [6], [113] |
| 퍼블리셔(publisher) | 게임의 출판·출시·유통·마케팅 등을 맡는 주체. | 게임을 직접 만드는 개발자와 역할을 구별하되 같은 주체일 수 있다. | 퍼블리셔는 출시 지역과 홍보를 담당한다. | — | [113] |
| 아케이드(매체)(arcade game) | 오락시설 등의 상업용 전용 기기에서 제공하는 게임 매체·운영 형식. | 가정용 게임의 아케이드 스타일과 구별한다. | 아케이드 기기는 전용 조작 장치와 회차 과금을 사용한다. | [114]: 동전 또는 다른 결제 수단을 받는 cabinet 매체; 전자 비디오 이전의 오락기 역사도 존재. | [114] |
| 아케이드(스타일)(arcade-style) | 직관적 조작과 즉시 도전·반복·성과 추구를 강조하는 플레이 스타일 명칭. | 전용 기기에서 출시됐는지와 별개이다. | 짧은 구간을 반복하며 점수를 겨루는 아케이드 스타일을 제공한다. | [114]: 짧은 레벨·직관적 조작·빠른 난도 상승; 레이싱의 arcade는 현실 재현보다 관대한 조작을 강조하기도 함. | [114] |
| 무료플레이(free-to-play·F2P) | 기본 플레이에 선구매 비용을 요구하지 않는 제공·수익 모델. | 과금이 전혀 없는 무료 게임이나 무료 체험판과 구별한다. | 기본 플레이는 무료이며 외형 물품을 선택 구매할 수 있다. | — | [6], [104] |
| 가챠(gacha) | 정해진 후보와 추첨 규칙에 따라 물품·캐릭터 등을 무작위로 얻는 획득 방식. | 모든 무작위 전리품이나 캐릭터 수집 장르를 뜻하지 않는다. | 가챠는 추첨 후보와 각 결과의 확률을 표시한다. | — | [6] |
| 시즌(운영)(season) | 콘텐츠·규칙·보상·순위 등을 일정 기간 단위로 운영하는 주기. | DLC 구매 묶음을 뜻하는 season pass와 구별한다. | 시즌 종료 때 순위만 초기화하고 보유 장비는 유지한다. | [6]: 운영 기간 외에 예정된 DLC 묶음도 season으로 부름. | [6] |
| 이벤트(운영)(live event) | 특정 기간이나 조건에 맞춰 제공하는 특별 과제·보상·플레이 내용. | 게임 내부의 단일 사건 event와 구별한다. | 이벤트 기간에는 별도 목표와 보상을 제공한다. | — | [6] |
| 라이브 서비스(live service) | 출시 후 장기적인 콘텐츠 업데이트와 계속되는 수익 구조로 참여를 이어 가는 서비스 모델. | 온라인 접속 여부만으로 판정하지 않는다. | 라이브 서비스 운영으로 새 임무와 조정된 규칙을 제공한다. | — | [6] |
| VR(virtual reality) | 가상 공간을 주변 환경처럼 경험하도록 제공하는 몰입형 매체 방식. | 화면 시점인 1인칭 및 현실 위 합성인 AR과 구별한다. | VR 입력은 손의 위치와 머리 방향을 반영한다. | — | [6], [94] |
| AR(augmented reality) | 현실 환경 위에 가상 정보·대상·상호작용을 결합하는 방식. | 현실을 가상 환경으로 대체하는 VR과 구별한다. | AR은 실제 공간의 표면에 가상 대상을 표시한다. | — | [108] |
| FMV(full-motion video) | 미리 촬영·제작된 동영상을 화면 표현이나 선택·상호작용의 주요 매체로 쓰는 방식. | 실시간 렌더링과 제작된 영상 재생을 구별하며 영상만으로 장르가 결정되지 않는다. | FMV 장면에서 선택지에 따라 다음 영상이 달라진다. | — | [115] |
| 사용자 제작 콘텐츠(user-generated content·UGC) | 이용자가 만들어 게임에 활용하는 맵·외형·규칙 등의 콘텐츠. 공유는 선택적 기능이다. | 개발사가 제공한 콘텐츠와 제작 주체를 구별한다. | 편집기로 제작한 맵을 사용자 제작 콘텐츠로 공유한다. | — | [6], [97] |

<a id="gd-2-14"></a>
### 2.14 목적·소재·대상·지역 표현

| key | value | 구별 기준 | 보고서 예문 | 의미 차이 | ref |
|---|---|---|---|---|---|
| 교육게임(educational game) | 지식·기술·이해의 학습을 주요 목적으로 설계한 게임. | 학습 목적과 퍼즐·시뮬레이션 등의 플레이 구조를 별도로 서술한다. | 교육게임은 계산 과제의 수행 뒤 학습 피드백을 제공한다. | — | [116] |
| 기능성게임·시리어스게임(serious game) | 교육·훈련·건강·사회 문제 등 오락 외의 목적을 주요하게 수행하도록 설계한 게임. | 특정 장르가 아니라 사용 목적의 분류이며 교육게임을 포함할 수 있다. | 기능성게임은 의사결정 훈련을 반복 가능한 상황으로 제공한다. | — | [116] |
| 애드버게임(advergame) | 브랜드·상품·조직 등의 홍보를 목적으로 제작하거나 활용하는 게임. | 게임 안에 광고만 삽입한 경우와 게임 자체의 홍보 목적을 구별한다. | 애드버게임은 브랜드의 특성을 플레이 과제에 연결한다. | — | [116] |
| 판타지(fantasy) | 마법·초자연적 존재·가상 세계 등의 상상 요소를 중심으로 한 소재·세계관 표현. | RPG나 전략 같은 플레이 장르와 별개이다. | 판타지 소재의 도시 경영에서 마법 자원을 관리한다. | — | [117] |
| SF(science fiction) | 과학·기술·우주 여행 등을 통해 상상한 미래나 세계·사건을 다루는 소재 표현. | 우주 배경 하나나 특정 플레이 장르와 동일하지 않다. | SF 소재의 퍼즐에서 가상 중력 기술을 사용한다. | — | [118] |
| 가족 대상(family-friendly) | 어린이와 가족 이용자가 접하기 적합하도록 고려한 대상·적합성 명칭. | 협동 기능·연령등급·어린이 전용과 각각 구별한다. | 가족 대상 설계에서는 규칙 설명과 입력 부담을 낮춘다. | — | [119] |
| 서브컬처(한국 시장)(subculture game) | 한국 게임 시장에서 애니메이션 계열 표현과 캐릭터·서사·팬덤 중심 참여를 묶어 부르는 문화·시장 명칭. | 수집 RPG·가챠·일본 제작과 일대일 대응하지 않는다. | 서브컬처 시장 관점에서 캐릭터 서사와 팬 교류 콘텐츠를 분석한다. | [120]: 캐릭터 개성·스토리·최애 팬덤과 애니메이션 문화의 연결; 일반 subculture의 하위문화 전체보다 좁은 한국 시장 용례. | [120] |

<a id="gd-3"></a>
## 3. 레퍼런스

[1] [Beat em up — 정의와 역사](https://en.wikipedia.org/wiki/Beat_%27em_up)
[2] [Shooter game — 하위 장르](https://en.wikipedia.org/wiki/Shooter_game)
[3] [Platformer](https://en.wikipedia.org/wiki/Platformer)
[4] [Berlin Interpretation](https://www.roguebasin.com/index.php/Berlin_Interpretation)
[5] [Infil Fighting Game Glossary](https://glossary.infil.net/?g=COM)
[6] [게임 용어집 — 판정·플랫폼·로그](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms)
[7] [VALORANT Patch Notes 6.11](https://playvalorant.com/en-gb/news/game-updates/valorant-patch-notes-6-11/)
[8] [Bullet hell](https://en.wikipedia.org/wiki/Bullet_hell)
[9] [Infil — Frame](https://glossary.infil.net/?t=Frame)
[10] [Infil — Frame Advantage](https://glossary.infil.net/?t=Frame%20Advantage)
[11] [Infil — 3D Game·Sidestep](https://glossary.infil.net/?t=3D%20Game)
[12] [How to Smash — Gameplay Basics](https://www.smashbros.com/en_US/howtoplay/basic.html)
[13] [The best fighting games on PS4 and PS5](https://www.playstation.com/en-us/editorial/best-fighting-games-on-ps4-ps5)
[14] [GameMaker Platformer Jumping Tips](https://www.gamedeveloper.com/design/gamemaker-platformer-jumping-tips)
[15] [Infil — Buffer Window](https://glossary.infil.net/?t=Buffer%20Window)
[16] [Stealth game](https://en.wikipedia.org/wiki/Stealth_game)
[17] [The best stealth games on PS4 and PS5](https://www.playstation.com/en-us/editorial/great-stealth-games-on-PS4-essential-buyers-guide)
[18] [Adventure game](https://en.wikipedia.org/wiki/Adventure_game)
[19] [Puzzle video game](https://en.wikipedia.org/wiki/Puzzle_video_game)
[20] [Writing with ink](https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md)
[21] [Otome game](https://en.wikipedia.org/wiki/Otome_game)
[22] [RenPy Quickstart](https://www.renpy.org/doc/html/quickstart.html)
[23] [매칭 타일 게임의 역사 — Jesper Juul](https://jesperjuul.net/text/swapadjacent/)
[24] [Word game](https://en.wikipedia.org/wiki/Word_game)
[25] [Trivia Murder Party](https://www.jackbox.studio/games/trivia-murder-party)
[26] [Epistory - Typing Chronicles](https://www.epistorygame.com)
[27] [RPG — GameRefinery](https://docs.gamerefinery.com/en/articles/2278771-rpg)
[28] [Introduction — D&D Basic Rules 2014](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/introduction)
[29] [Step-by-Step Characters — D&D Basic Rules 2014](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/step-by-step-characters)
[30] [Job Guide — Final Fantasy XIV](https://na.finalfantasyxiv.com/jobguide/battle/)
[31] [League of Legends How to Play](https://www.leagueoflegends.com/en-us/how-to-play/)
[32] [Combat — D&D Basic Rules 2014](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat)
[33] [Blade Prince Academy Press Kit](https://firesquid.games/press-kits/blade-prince-academy)
[34] [Baldur’s Gate 3](https://baldursgate3.game)
[35] [Parts of the HUD — Final Fantasy XIV](https://na.finalfantasyxiv.com/uiguide/know/know-hud/hud-name.html)
[36] [Hades](https://www.supergiantgames.com/games/hades)
[37] [JRPG history — Mollie Patterson](https://mollielpatterson.com/jrpg-may-be-an-outdated-term-but-it-was-originally-born-out-of-love/)
[38] [Strategy — GameRefinery](https://docs.gamerefinery.com/en/articles/2278772-strategy)
[39] [Terminology — 0 A.D.](https://trac.wildfiregames.com/wiki/Manual_Terminology)
[40] [MSC: A Dataset for Macro-Management in StarCraft II](https://arxiv.org/html/1710.03131v3)
[41] [Basic Gameplay — 0 A.D.](https://trac.wildfiregames.com/wiki/Manual_BasicGameplay)
[42] [Simulation — GameRefinery](https://docs.gamerefinery.com/en/articles/2278750-simulation)
[43] [Reus](https://abbeygames.com/game/reus)
[44] [그로잉 투게더 확장팩 — The Sims 4](https://www.ea.com/ko/games/the-sims/the-sims-4/news/the-sims-4-grow-together-guided-tour)
[45] [Farming — Stardew Valley Wiki](https://stardewvalleywiki.com/Farming)
[46] [Crops — Stardew Valley Wiki](https://stardewvalleywiki.com/Crops)
[47] [Factorio Content](https://www.factorio.com/game/content)
[48] [Belt transport system — Official Factorio Wiki](https://wiki.factorio.com/Belt_transport_system)
[49] [Football Manager 2024 Console – New Features Unveiled](https://www.footballmanager.com/features/football-manager-2024-console-new-features-unveiled)
[50] [Sports — GameRefinery](https://docs.gamerefinery.com/en/articles/2278764-sports)
[51] [Rule 4 Definitions — NBA Official](https://official.nba.com/rule-no-4-definitions/)
[52] [Driving — GameRefinery](https://docs.gamerefinery.com/en/articles/2278766-driving)
[53] [How to Create a Room 2 — GT7 Manual](https://www.gran-turismo.com/gb/gt7/manual/multiplayer/04)
[54] [The Pit Menu — GT7 Manual](https://www.gran-turismo.com/au/gt7/manual/race/07)
[55] [Spin Rhythm XD](https://store.steampowered.com/app/1058830/Spin_Rhythm_XD)
[56] [Audiosurf](https://store.steampowered.com/app/12900/AudioSurf)
[57] [Judgement — osu!mania Wiki](https://osu.ppy.sh/wiki/en/Gameplay/Judgement/osu%21mania)
[58] [Card Games — GameRefinery](https://docs.gamerefinery.com/en/articles/2278770-card-games)
[59] [How to Play — Magic](https://magic.wizards.com/en/how-to-play)
[60] [Solitaire — Bicycle](https://bicyclecards.com/how-to-play/solitaire)
[61] [MTG Arena Formats and Events](https://magic.wizards.com/en/news/mtg-arena/mtg-arena-formats)
[62] [Dominion®](https://www.riograndegames.com/games/dominion)
[63] [Genre Taxonomy Update January 2020 — GameRefinery](https://www.gamerefinery.com/genre-taxonomy-update-january-2020/)
[64] [Tabletop Simulator](https://store.steampowered.com/app/286160/Tabletop_Simulator)
[65] [Laws of Chess 2023 — FIDE](https://handbook.fide.com/chapter/E012023)
[66] [Among Us](https://www.innersloth.com/games/among-us)
[67] [Drawful](https://www.jackboxgames.com/games/drawful)
[68] [The Math of Idle Games Part I — Kongregate](https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i)
[69] [Cookie Clicker](https://store.steampowered.com/app/1454400/Cookie_Clicker)
[70] [Casino — GameRefinery](https://docs.gamerefinery.com/en/articles/2278761-casino)
[71] [Free Casino Slots - Slotomania Free Slots](https://www.slotomania.com/free-casino-slots)
[72] [Casino Slots Glossary — GammaStack](https://www.gammastack.com/blog/online-slot-game-glossary/)
[73] [Basics of Poker — Bicycle](https://bicyclecards.com/how-to-play/basics-of-poker)
[74] [Blackjack — Bicycle](https://bicyclecards.com/how-to-play/blackjack)
[75] [Dead Cells](https://www.dead-cells.com)
[76] [Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire)
[77] [Rogue Legacy 2 — 공식 PlayStation 소개](https://www.playstation.com/en-gr/games/rogue-legacy-2/)
[78] [Soulslike](https://en.wikipedia.org/wiki/Soulslike)
[79] [Metroidvania](https://en.wikipedia.org/wiki/Metroidvania)
[80] [Survival game](https://en.wikipedia.org/wiki/Survival_game)
[81] [Horror game](https://en.wikipedia.org/wiki/Horror_game)
[82] [Battle royale game](https://en.wikipedia.org/wiki/Battle_royale_game)
[83] [Extraction shooter](https://en.wikipedia.org/wiki/Extraction_shooter)
[84] [Arena — TFT Wiki](https://wiki.leagueoflegends.com/en-us/TFT:Arena)
[85] [Introduction: The Genre Buster — Paidia](https://paidia.de/introduction-the-genre-buster-on-terminology-history-worldbuilding-and-gameplay-of-the-immersive-sim/)
[86] [Juul — The Game, the Player, the World](https://jesperjuul.net/text/gameplayerworld/)
[87] [Björk·Holopainen — Underlying Assumptions and Concepts](https://gdp.cse.chalmers.se/index.php?title=Underlying_Assumptions_and_Concepts)
[88] [Sicart — Defining Game Mechanics](https://gamestudies.org/0802/articles/sicart)
[89] [Epic — UMG UI Designer Quick Start Guide](https://dev.epicgames.com/documentation/unreal-engine/umg-ui-designer-quick-start-guide-in-unreal-engine)
[90] [Björk·Holopainen — Resources](https://gdp.cse.chalmers.se/index.php?title=Resources)
[91] [Supergiant — Hades Steam 소개](https://store.steampowered.com/app/1145360/Hades/)
[92] [Boss (video games)](https://en.wikipedia.org/wiki/Boss_(video_games))
[93] [All Game Modes in Minecraft](https://help.minecraft.net/hc/en-us/articles/360058743992-Minecraft-Differences-Between-Creative-Survival)
[94] [Game Accessibility Guidelines — Full list](https://gameaccessibilityguidelines.com/full-list/)
[95] [Björk·Holopainen — Clues](https://gdp.cse.chalmers.se/index.php?title=Clues)
[96] [Python — random](https://docs.python.org/3/library/random.html)
[97] [Björk·Holopainen — Construction](https://gdp.cse.chalmers.se/index.php?title=Construction)
[98] [Björk·Holopainen — Combat](https://gdp.cse.chalmers.se/index.php?title=Combat)
[99] [Björk·Holopainen — Crafting](https://gdp.cse.chalmers.se/index.php?title=Crafting)
[100] [Infil — Block](https://glossary.infil.net/?t=Block)
[101] [osu! Wiki — Combo (score multiplier)](https://osu.ppy.sh/wiki/en/Gameplay/Combo_(score_multiplier))
[102] [Infil — Invincible](https://glossary.infil.net/?t=Invincible)
[103] [Kabam 개발자 — What Makes Social Games Social?](https://www.gamedeveloper.com/game-platforms/what-makes-social-games-social-)
[104] [Paavilainen 외 — Social Network Games: Players’ Perspectives](https://journals.sagepub.com/doi/abs/10.1177/1046878113514808)
[105] [GameRefinery — Social Features Market Trend Analysis](https://www.gamerefinery.com/social-features-that-the-top-performing-mobile-games-have-incorporated-market-trend-analysis/)
[106] [What are Categories, Genres and Subgenres?](https://docs.gamerefinery.com/en/articles/2278730-what-are-categories-genres-and-subgenres)
[107] [The Mobile Games Playbook](https://resources.smaato.com/hubfs/Smaato/Resources/Whitepapers/Mobile_Games_Playbook.pdf)
[108] [Dunham 외 — Casual and Hardcore Player Traits and Gratifications](https://arxiv.org/html/2103.00037v2)
[109] [Unity — What are Hybrid-Casual Games](https://unity.com/kr/glossary/hybrid-gaming)
[110] [Mobile Gaming’s Shift from Hyper to Hybrid-Casual Games](https://unity.com/blog/mobile-gaming-shift-hyper-hybrid-casual)
[111] [Barry Ip — From Casual to Core: Gamer Dedication](https://www.gamedeveloper.com/business/from-casual-to-core-a-statistical-mechanism-for-studying-gamer-dedication)
[112] [Coziness in Games: An Exploration of Safety, Softness, and Satisfied Needs](https://www.projecthorseshoe.com/reports/featured/ph17r3.htm)
[113] [Garda·Grabarczyk — Is Every Indie Game Independent?](https://gamestudies.org/1601/articles/gardagrabarczyk)
[114] [Arcade video game](https://en.wikipedia.org/wiki/Arcade_video_game)
[115] [Full-motion video](https://en.wikipedia.org/wiki/Full-motion_video)
[116] [Chaos Theory — The Ultimate Guide to Serious Games](https://www.chaostheorygames.com/what-are-serious-games-2021)
[117] [Cambridge Dictionary — Fantasy](https://dictionary.cambridge.org/dictionary/english/fantasy)
[118] [Cambridge Dictionary — Science fiction](https://dictionary.cambridge.org/dictionary/english/science-fiction)
[119] [Cambridge Dictionary — Child-friendly](https://dictionary.cambridge.org/dictionary/english/child-friendly)
[120] [한국콘텐츠진흥원 — 서브컬처 국가별 현안](https://www.kocca.kr/global/2023_3+4/sub01_02.html)
