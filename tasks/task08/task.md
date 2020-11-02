# Task8

- 2020\-08\-18 (WED)
- 주제: AIOHTTP 서버 맛보기

## 배우는 내용

- aiohttp quict start

## 사전 요구사항

- `aiohttp`

## 태스크

https://docs.aiohttp.org/en/stable/client_quickstart.html

위 문서를 읽고, 쭉 따라해보세요.

그 이후에 다음 태스크를 수행하세요.

덧셈을 수행하는 API 를 생성합니다.
경로는 `sum` 이고, 입력은 쿼리스트링으로 받습니다.

- `/sum?a=1&b=2` : 3 이라는 적힌 문서를 반환
- `/sum?a=1&b=2&c=3` : 6 이라는 적힌 문서를 반환
- `/sum` : 입력이 필요하다는 텍스트 반환

로컬호스트에서 동작시키면 됩니다.
