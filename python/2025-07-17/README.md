## 2025-07-17
### [git 원격저장소 커맨드](#목차)

git remote add origin(저장소 이름) remote_repo_url(추가하는 원격 저장소 주소) : 로컬 저장소에 원격 저장소 추가

git remote -v : 원격저장소 확인

git push origin(원격 저장소 이름) master(라는 이름의 브랜치) : 업로드 로컬->원격

git pull origin master : 원격 저장소의 변경사항 만 다운로드 원격->로컬

git clone remote_repo_url : 원격 저장소 전체를 복제(다운로드)(clone으로 받은 프로젝트는 이미 git init 되어있음)

.gitignore : 추적되지 않도록 설정하는 것
(이미 git의 관리를 받은 파일이나 폴더는 적용되지 않음)

git remote -v : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기

git remote rm 원격저장소이름 : 현재 로컬 저장소에 등록된 원격 저장소 삭제

git revert <commit_id>: 특정(단일) commit을 없었던 일로 만드는 작업, 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함, 기록에서 commit이 사라지지는 않음

변경사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업

git revert 해쉬1 해쉬2 해쉬3 : 여러 commit 동시에 가능

git revert 해쉬1..해쉬3 : ..을 사용해 범위지정

git revert --no-edit 해쉬 : edit창 열지않고 바로 실행

git revert --no-commit 해쉬 : add만 하고 commit은 직접 실행해야함

git reset [옵션] commit_id :되돌리기, 특정 commit값으로 돌아갔을때 되돌아간 이후의 commit은 모두 삭제

옵션>

--soft : 삭제된 commit의 기록을 staging area에 남김

--mixed : 삭제된 commit의 기록을 working directory에 남김

--hard : 삭제된 commit의 기록을 남기지 않음

git reflog : head가 가리켰던 모든 commit을 보여줌

git restore : modified 상태의 파일 되돌리기, 원래파일로 덮어쓴느 원리로 수정내용 전부 사라짐, 즉 되돌리기 이후 복구 불가능

staging area에서 working directory로 되돌리기

git rm --cached : git저장소에 commit이 없는 경우

git restore --staged : git저장소에 commit이 있는 경우
