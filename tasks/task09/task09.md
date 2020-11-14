#Task09 -> 학교 홈페이지 공지사항 데이터 가져오기
## STEP 1
### Step 1-1
<pre>
resp = await kbuAPI.MainNotice.fetch(page = 2)
</pre>
- MainNotice 클래스 안의 함수들은 동적함수로 작동한다.
- resp 에서 MainNotcie 속의 class MainNotice(NoticeList): 에서 cls 은 URL 을 정의한다.
- NoticeList 클래스에서 fetch 함수가 정의되어있고, "동적"으로 선언해주었기 때문에, 상속받는 함수의 cls 의 값을 사용 할 수 있다.
- fetch 에선, 인자값으로 페이지 번호를 받고, 홈페이지 세션을 요청하기 위해 비동기로 서버에 요청한다.
### Step 1-2
<pre>
async def fetch(~) -> Response: 
    ~~
    response.etc["notice"] = {"page": page, "keyword": search_keyword}
    return response
</pre>
- etc 는 dict 형태로 데이터를 저장 할 수 있다. 아마, 여러 데이터를 구분하기 위해 만든 클래스 인 것 같음.
- 위에서 get 을 요청 할 때, request|base.py에 저장되어있는 클래스를 참조하는데, 이유를 모르겠음..(아마 확장성과 오류 처리를 용이하게 해주기 위한 듯)
- 세션을 보내고, 해당 페이지의 세션을 담은 response 객체를 리턴함.

## STEP 2
- 가져온 반응 객체를 통해서 데이터를 받아오고, 출력하는 단계
<pre>
result = KbuAPI.MainNotice.parse(resp)
pprint(result.data)
</pre>
### Step 2-1
- 비교적 단순한 구조를 지님, parse에서 컨테이너를 찾을 수 업을 때, parseError을 일으킴.
- find 메소드를 사용해서 공지사항을 가져오고, APIResponseTyped에 넣어준다.
- APIResponseType에는 {data, meta, link} 키 값을 가지고 있는데, meta는 추가적인 공부가 필요 할 듯(메타 클래스).



#Task10 -> 로그인 한 사용자의 수강 데이터 가져오기
- 공지사항 데이터를 들고오는 방식이랑 비슷하다. 하지만, 로그인 양식을 post 해서, session을 받아오는 과정이 필요함.
- task09의 과정을 두 번 한다. (1. 로그인 세션 요청 -> resp 2. )
##Step 1
<pre>
resp = await IntranetAPI.Login.fetch(*account)
result = IntranetAPI.Login.parse(resp)
cookie = result.data["cookies"]
</pre>
- resp에서 계정 정보를 담아서, response 객체를 받아온다. *여기선 오류 처리를 하지 않는다.
  (왜 그런지를 생각해봤는데, 로그인 실패를 하면, 디버깅 오류가 아니라 세션에서 로그인 처리가 안되는 것 뿐이라 아마 오류를 잡아내기 까다롭기 때문이 아닌가 생각든다.)
  (하지만 status를 통해 오류를 잡아 줄 수 있을텐데, 오류를 resp에서 처리해주는 순간, parse의 기능이 섞여서 객체지향에 어긋나서 그런 것 인지도)
- Login의 parse함수도 비슷한 구조인데, status를 통해 오류가 아니라면, cookie와 link와 메타 클래스를 담아 return 해준다.
- 오류라면, alert에서 에러 메세지를 포함해 return 해주는데, 이 부분도 내부적으로 이해가 힘들다.

##Step 2
비동기로 서버에 계정 양식을 보내주고(post), cookie 변수에 cookie를 저장해둠.
따라서, 로그인이 필요한 path에도 접근이 가능함.
<pre>
# Get course information
resp = await IntranetAPI.Course.fetch(cookies=cookie, semester="20201")
result = IntranetAPI.Course.parse(resp)
pprint(result.data)
 </pre>
- DOMAIN_NAME + "/GradeMng/GD095.aspx" <- 수강 정보 데이터
- resp에서 cookie 데이터를 넘겨줌으로서 회원 정보를 알려줌, +학기 정보
- parse의 구조는 유사함.

#메모
- 확장성을 위해서인지, aio, asy를 그냥 사용해서 post를 하는 것이 아니라, 클래스를 통해서 일어 날 수 있는 에러를 처리하고, 
반환하는 데이터를 일관성있게 정리한 것 같음. (파고 파고 들어가도 어려움)
- 특히, func(func2)와 같은 유형인데, func, func2 전부 다 객체이고, 매개변수가 어떻게 들어가는지 파악하기 어려움.
- 디버깅을 하면, 함수가 어떤 순서로 진입하는지 확인 할 수 있느나, 너무 코드량이 많아서.. 하나하나 확인하기 힘듦.
- 다만, post, get 부분을 fetch, 그리고 값을 가져오는 역활을 parse가 하다보니 대략적인 느낌은 쉽게 파악 할 수 있었음.
- 파이썬 문법을 체계적으로 학습할 필요를 느낌... (기본적인 데코, 클래스, 함수 사용 방법 등등)
- 성서봇 api에서 비동기로 실행되는 코드는 요청인데, 속도의 차이점이 있는지 궁금함.







