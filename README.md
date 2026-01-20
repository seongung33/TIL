# GIT이란?
분산 버전 관리 도구

## Repository
원격 저장소

```git
# 로컬 저장소에 원격 저장소 추가
git remote add origin remote_repo_url
remote_repo_url = # 원격 저장소 주소
# origin = 추가하는 원격 저장소 별칭
```

-----------------------
## push / pull or clone
### push
local Repository ---> Github Repository  
**git push** origin master << commit 목록을 업로드  
- commit 된 것을 원격 저장소로 저장
- 즉, add > commit -m > push 를 해야함

### pull

git pull origin master  
- 원격 저장소의 변경사항만을 받아옴 (업데이트)
- 원격 저장소와 개인 컴퓨터와 다른 정보를 끌고옴.
- 원격저장소 > 개인 컴퓨터

### clone
git clone remote_repo_url
- 원격저장소 전체를 복제(다운로드)
- 원격 저장소 파일 복제 > 개인 컴퓨터 저장

 - git remote -v
 - git remote rm <remote_name>
 - git push --set-upsteram origin master( git push -u origin master)

## gitignore
git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 텍스트 파일  
**.gitignore**  
올리면 안되는 파일 ex) .venv
- Git의 관리를 받은 파일이나 디렉토리는 이후에 .gitignore에 추가해도 적용되지 않는다.
    - git rm --cached를 통해 git 캐시에서 삭제필요

## Revert & Reset
### Git revert
- 특정 commit을 없었던 일로 만드는 작업
- 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함

1. commit 확인
    - git log--oneline
2. 출력된 값 바탕으로 원하는 위치에서 revert 하기
    - git revert ~~  

revert 동시에 하기
   - git revert 34kh 34jb 3j44

### GIt reset
특정 commit으로 되돌아가기
- git reset [옵션] <commit id>
  - --soft
    - 삭제된 commit들의 기록을 staging area에 남김
    - add 된 상태 commit 시 commit 됨
  - --mixed
    - 삭제된 commit들의 기록을 working directory에 남김(기본값)
    - add 해야하는 상태
    - untracked 상태
  - --hard
    - 삭제된 commit들의 기록을 남기지 않음
    - 완전 삭제  

### **주의사항**  
- reset은 만들어진 commit을 되돌리는 행위
- remote에 기록된 commit을 reset 하게되면?
  - 기존 기록과 다른 기록의 comiit 이력을 작업하게 됨
  - 다른 동료간 코드가 충돌할 수 있음


#### **remote에 올라간 commit은 절대 reset 해서는 안됨**

## Github은 어디에 활용할까
TIL을 통해 내가 학습하는 것을 기록
- 내가 배운 것을 마크다운으로 정리하여 문서화

## 직전 생성한 commit 수정하기

### git commit --amend
1. commit 메시지 수정
2. commit 전체 수정

### git restore
Modified 상태의 파일 되돌리기
1. git restore --staged
   - add 했던 내역이 없어집니다.
2. git rm --cached
  - Git이 파악하고 있는 파일을 GIt에서만 제거


## config
git config --global user.name 
변경시 git config --global user.name seongung
git config --global user.email

