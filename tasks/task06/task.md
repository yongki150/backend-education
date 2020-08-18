# Task6
- 2020\-08\-11 (TUE)
- 주제: 동시성 크롤링


## 배우는 내용
1. Concurrency

## 사전 요구사항
1. `aiohttp`


## 태스크
TASK04 에서 수행한 크롤러를 발전시킵니다.

TASK04에서는 공지사항의 특정 페이지에 존재하는 모든 공지사항의 정보를 수집했습니다.  
하지만 이 과정에서 HTTP 통신이 21회 정도 순차적으로 발생하기 때문에 수행속도가 꽤 느립니다.  
앞서 요청한 통신이 끝나야만 다음 통신을 진행할 수 있기 때문입니다.  

이번 태스크에서는 HTTP 요청을, 동시성 프로그래밍을 활용하여 한꺼번에 요청하고자 합니다.  
동시성(Conccurency)은 IO-bound tasks(파일의 입출력과 소켓을 이용한 통신 등)에서 뛰어난 효율을 발휘합니다.  
파이썬에서 사용할 수 있는 대표적인 방법은 다음과 같습니다.

1. asynchronous
2. multi-thread
3. multi-process

1번은 `aiohttp` 라는 써드파티 라이브러리를 이용하고, 2번과 3번은 파이썬 표준 라이브러리를 이용합니다.  

각각의 코드를 작성한 뒤 속도를 비교해보고, 각각의 개념에 대해서 간단히 조사해보세요.  
OS를 배우지 않았다면 개념이 생소할 수 있으나, 거시적인 관점에서 파악하려고 노력해야합니다.

> **NOTE1:** 동시성(Concurrency)과 병렬성(Parallelism)은 다른 주제입니다. 이번 태스크에서는 동시성만 학습하세요. 

> **NOTE2:** 시간이 남는다면, 세 주제의 공통점과 차이점에 대해서도 조사해보세요.


### 코드 작성
주제 당 하나씩, 총 세 개의 파이썬 파일을 만들어서 코드를 작성하세요.

```python
# async.py
from typing import List

# asynchronous
async def get_notice_articles_async(page_num: int = 1) -> List[List[str]]:
    """코드 작성"""
```

```python
# thread.py
from typing import List


def get_notice_articles_thread(page_num: int = 1) -> List[List[str]]:
    """코드 작성"""
```

```python
# process.py
from typing import List


def get_notice_articles_process(page_num: int = 1) -> List[List[str]]:
    """코드 작성"""

```