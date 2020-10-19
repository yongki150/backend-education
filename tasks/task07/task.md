# Task7

- 2020\-08\-17 (TUE)
- 주제: 크롤링 마지막

## 배우는 내용

- 쿠키 처리

## 사전 요구사항

- `aiohttp`

## 태스크

1. https://lms.bible.ac.kr/ 로그인한 뒤
2. https://lms.bible.ac.kr/local/ubion/user/ 수강 강좌 페이지의 (강좌, 교수명, 수강인원)을 가져오세요.

`get_courses` 함수를 구현하세요. 더 나은 방향으로 함수의 구조를 변경해도 괜찮습니다.

이번 태스크로 크롤링 학습은 마칩니다. 다음 태스크부터는 aiohttp를 활용해 서버를 개발합니다.

```python
from typing import Dict, List, Optional
from dataclasses import dataclass
import asyncio


@dataclass
class SemesterData:
    year: int
    semester: int


async def get_courses(semester: Optional[SemesterData] = None) -> Dict[str, List[str]]:
    """ 선택한 학기의 수강 강좌 데이터를 가져옵니다

    :param semester: 선택할 학기 정보, None 이면 수강 강좌 페이지에서 default로 선택된 학기
    :return: 수강 강좌 데이터
    """
    # 코드 작성


async def main():
    print("default")
    print(get_courses())
    print("-" * 30)
    print(get_courses(SemesterData(2020, 1)))  # 2020학년도 1학기 데이터 조회


asyncio.run(main())
```

**반환 예시**

```json
{
  "전도훈련Ⅷ": ["조혜경", "7"],
  "종합설계II": ["정해덕", "30"],
  "인턴쉽I": ["양혜경", "30"],
  "인턴쉽II": ["임지영", "30"],
  "인턴쉽III": ["김원빈", "30"],
  "인턴쉽IV": ["현우석", "30"]
}
```
