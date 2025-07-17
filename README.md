# 목차
1. [2025-07-16](#2025-07-16-학습내용)
    1. [git bash 기본 명령어](#git-bash-기본-명령어) 
    2. [markdown](#markdown)
    3. [git의 영역](#git의-영역)
    4. [git의 동작 커맨드](#git의-동작-커맨드)
2. [2025-07-17](#2025-07-17-학습내용)

# [2025-07-16 학습내용](#목차)
## [git bash 기본 명령어](#목차)

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
## [markdown](#목차)
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

표 세로선 : | (shift \)

이모지 : :키워드: (git bash는 안됨 : 확장프로그램 설치 필요)

git : 분산 버전 관리 시스템(중 하나), 각 버전은 이전 버전으로 부터의 변경사항을 기록하고 있음->전체내용 모두 포함x

---
## [git의 영역](#목차)
working directory : 실제 작업 중인 파일들이 위치하는 영역

staging area : working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

repository : 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨

commit : 변경된 파일을 저장하는 행위, snapshot 이라고도 함

---
## [git의 동작 커맨드](#목차)
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

## [2025-07-17 학습내용](#목차)

git remote add origin(저장소 이름) remote_repo_url(추가하는 원격 저장소 주소) : 로컬 저장소에 원격 저장소 추가

git remote -v : 원격저장소 확인

git push origin(원격 저장소 이름) master(라는 이름의 브랜치) : 업로드 로컬->원격

git pull origin master : 원격 저장소의 변경사항 만 다운로드 원격->로컬

git clone remote_repo_url : 원격 저장소 전체를 복제(다운로드)(clone으로 받은 프로젝트는 이미 git init 되어있음)

.gitignore : 추적되지 않도록 설정하는 것
(이미 git의 관리를 받은 파일이나 폴더는 적용되지 않음)

git rm -cached : 

git remote -v : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기

git remote rm 원격저장소이름 : 현재 로컬 저장소에 등록된 원격 저장소 삭제

git revert <commit id>: 특정(단일) commit을 없었던 일로 만드는 작업, 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함, 기록에서 commit이 사라지지는 않음

변경사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업

git revert 해쉬1 해쉬2 해쉬3 : 여러 commit 동시에 가능

git revert 해쉬1..해쉬3 : ..을 사용해 범위지정

git revert --no-edit 해쉬 : edit창 열지않고 바로 실행

git revert --no-commit 해쉬 : add만 하고 commit은 직접 실행해야함

git reset [옵션] commit id :되돌리기, 특정 commit값으로 돌아갔을때 되돌아간 이후의 commit은 모두 삭제

옵션)

--soft : 삭제된 commit의 기록을 staging area에 남김

--mixed : 삭제된 commit의 기록을 working directory에 남김

--hard : 삭제된 commit의 기록을 남기지 않음

git reflog : head가 가리켰던 모든 commit을 보여줌

git restore : modified 상태의 파일 되돌리기, 원래파일로 덮어쓴느 원리로 수정내용 전부 사라짐, 즉 되돌리기 이후 복구 불가능

staging area에서 working directory로 되돌리기)

git rm --cached : git저장소에 commit이 없는 경우

git restore --staged : git저장소에 commit이 있는 경우