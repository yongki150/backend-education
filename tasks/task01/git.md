# git 활용

### 구조설명
현재 구조는
[https://github.com/rekyungmin/backend-education](rekyungmin/backend-education) 레포지토리를 포크한
[https://github.com/yongki150/backend-education](yongki150/backend-education)저의 레포지토리를 토대로 진행됩니다.

해당 레포지토리에서 제가 PR을 받아서 질문 및 피드백이 진행됩니다.

### 본인의 작업환경
1. [https://github.com/rekyungmin/backend-education](rekyungmin/backend-education) 레포지토리를 저처럼 포크해서 본인만의 레포지토리를 만들어서 진행하는 방법
  참고자료 [http://taewan.kim/post/updating_fork/]

2. 저의 레포지토리에 브랜치를 생성해서 진행하는 방법(간단히 이방법을 추천합니다.)

두 가지 방법에서 중요한 점은
**master로 PR을 보내면 안되는 점입니다.**
  ex.
  - yongki150/backend-education (master) ← yongki150/backend-education (master) (x)
  - yongki150/backend-education (master) ← yongki150/backend-education (본인이생성한브랜치) (O)
  - yongki150/backend-education (master) ← <본인레포지토리>/backend-education (master) (x)
  - yongki150/backend-education (master) ← <본인레포지토리>/backend-education (본인이생성한브랜치) (O)
**꼭 브랜치를 생성해서 보내주세요.**