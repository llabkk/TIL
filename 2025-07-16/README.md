## 2025-07-16

### git bash 기본 명령어

---
현재 디렉토리 : .

현재의 상위 디렉토리 : ..

파일생성 : touch 파일이름.확장자

새 디랙토리 생성 : mkdir 디렉토리이름

현재 작업중인 디렉토리 내부의 폴더/파일 출력 : ls
  (숨김파일 포함 모든 파일 출력 : ls -a)

터미널 청소 : clear

현재 작업중인 디렉토리 변경(위치이동) : cd 이동위치

상위 폴더로 이동 : cd ..

폴더/파일을 열기 : start(mac은 open)

파일 삭제 : rm(디렉토리 삭제는 -r 옵션 추가사용 : rm -r 디렉토리)

현재 작업중인 폴더의 절대경로를 출력 : pwd

루트 디렉토리 (/) : 모든 주소의 시작점

홈 디렉토리 (~) : 터미널 시작시 기본공간(예 : /c/Users/SSAFY)

절대경로 : /(루트 디렉토리에서부터 목적지까지의 전체 주소)

상대경로 : 현재 내위치를 기준으로 한 주소

---
### markdown
작성된 markdown 문서는 다른 프로그램에 의해 변환되어 출력

문법 및 활용

.md :  파일확장자

제목 : # 개수에 따라 (1개에서 6개까지 1개가 제일 큼)

리스트 : tab 들여쓰기

code block

라인 코드블럭 : ``` 내용 ``` (백틱 : ~ shift없이)(내용 좌우로 `3개)

인라인 코드블럭 : `내용` (내용 좌우로 `1개)

링크 : [보여주고싶은 텍스트](링크) -> [텍스트] + (링크)

이미지 : ![이미지](링크) -> ![이미지] + (링크)

()안에 넣을 링크 : 다운로드 후 pwd(절대주소), 온라인 검색 이미지 주소 복사

굵게 : **내용**, (내용 좌우로 *2개)

기울임 : *내용*, (내용 좌우로 *1개)

취소선 : ~~내용~~, (내용 좌우로 ~3개)

수평선(단락구분) : ---

표 세로선 : | (shift \\)

이모지 : :키워드: (git bash는 안됨 : 확장프로그램 설치 필요)

git : 분산 버전 관리 시스템(중 하나), 각 버전은 이전 버전으로 부터의 변경사항을 기록하고 있음->전체내용 모두 포함x

---
### git의 영역
working directory : 실제 작업 중인 파일들이 위치하는 영역

staging area : working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

repository : 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨

commit : 변경된 파일을 저장하는 행위, snapshot 이라고도 함

---
### git의 동작 커맨드
git init : 로컬 저장소 설정(초기화) -> git의 버전 관리를 시작할 디렉토리에서 진행, 설정시 주소 옆에 파란색 (master) 표시

**주의사항 : 저장소 안에 또 다른 저장소를 만들지 말것**

git add : 변경사항이 있는 파일을 staging area에 추가(현재 폴더 넣기 : git add .)

git rm --cached 지울파일 : staging area에 추가된 파일을 다시 staging area에서 제거

git commit -m "commit 메세지" : staging area에 있는 파일들을 저장소에 기록 -> 해당 시점의 버전을 생성하고 변경이력을 남기는것 -> -m "commit 메세지" 버전 설명을 위해

git status : 저장소 상태 확인

git config (--global) user.email "you@example.com"

git config (--global) user.name "Your Name"

git config --global --unset (user.email/name)

git log : 작성한 변경내역 전체 확인

git log --oneline : 변경매역 한줄로 간단하게 표시

git config --global -l : git global 설정 정보 보기

code . : 현재 폴더에서 vscode 열기

**바로 직전 생성한 commit 수정하기**

git commit --amend : vim 에디터가 열리면서 수정가능

:wq : 저장(write) 후 vim 에디터 종료(quit)