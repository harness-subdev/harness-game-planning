#!/bin/sh
set -eu
cd "$(dirname "$0")"
printf '게임 기획 워크플로우: http://127.0.0.1:4174\n종료: Ctrl+C\n'
exec python3 -m http.server 4174 --bind 127.0.0.1
