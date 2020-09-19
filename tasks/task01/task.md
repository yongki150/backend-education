# Task1
- 2020\-07\-30 (Thu)
- 주제: 파이썬 기초



## 배우는 내용
1. 예외처리
2. 리스트, for 조작법




## 사전 요구사항
1. Python 설치
2. IDE: Pycharm 커뮤니티 버전 설치
    
    

## 태스크
1. 업다운 게임
    - 랜덤하게 1 - 1000 사이의 숫자를 정답으로 하고, 유저가 정답을 맞출 때 까지 게임을 진행해주세요.
    - 숫자가 아닌 문자를 입력하면, 잘못된 입력이라는 안내와 함께 다시 입력을 받아주세요.
    - 문법참고 [https://wikidocs.net/book/1https://docs.python.org/ko/3/tutorial/index.html]


2. [https://leetcode.com/problems/two-sum/] 해당문제 풀기
    - 알고리즘은 생각하지 않아도 됩니다.
    - 아래와 같은 구조를 사용해주세요.

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 여기에 코드 작성 """


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
```