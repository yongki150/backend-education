import asyncio

from biblebot import IntranetAPI, KbuAPI, exceptions

INFO = {
    "ID": "",
    "passWD": "",
    "semester": "20202",
    "sid": "201504009",
    "page": "1",
    "searchKeyword": None,
    "cookie": "",
}


async def use_intranet_api():
    try:
        try:
            # Login
            response = await IntranetAPI.Login.fetch(INFO["ID"], INFO["passWD"])

            if response.reason != "Found":
                raise ValueError("맞는 ID와 비밀번호를 입력하세요.")
            
            result = IntranetAPI.Login.parse(response)
            INFO['cookie'] = result.data["cookies"]
            print(result)

        except ValueError as e:
            print("오류 원인:", str(e))

        # Get StudentPhoto
        resp = await IntranetAPI.StudentPhoto.fetch(cookies=INFO['cookie'], sid=INFO["sid"])
        result = IntranetAPI.StudentPhoto.parse(resp)
        print(result)

        # Get Chapel
        resp = await IntranetAPI.Chapel.fetch(cookies=INFO['cookie'], semester=INFO["semester"])
        result = IntranetAPI.Chapel.parse(resp)
        print(result)

        # Get Timetable
        resp = await IntranetAPI.Timetable.fetch(cookies=INFO['cookie'], semester=INFO["semester"])
        result = IntranetAPI.Timetable.parse(resp)
        print(result)

        # Get Course
        resp = await IntranetAPI.Course.fetch(cookies=INFO['cookie'], semester=INFO["semester"])
        result = IntranetAPI.Course.parse(resp)
        print(result)

    except exceptions.ParsingError as e:
        print("오류 원인:", str(e))
    except Exception as e:
        print("오류 원인:", str(e))


async def use_kbu_api():
    resp = await KbuAPI.MainNotice.fetch(page=INFO["page"], search_keyword=INFO["searchKeyword"])
    result = KbuAPI.MainNotice.parse(resp)
    print(result)

    resp = await KbuAPI.ScholarshipNotice.fetch(page=INFO["page"], search_keyword=INFO["searchKeyword"])
    result = KbuAPI.ScholarshipNotice.parse(resp)
    print(result)

    resp = await KbuAPI.IllipNotice.fetch(page=INFO["page"], search_keyword=INFO["searchKeyword"])
    result = KbuAPI.IllipNotice.parse(resp)
    print(result)


async def main():
    print("인트라넷API사용 중입니다.")
    await use_intranet_api()
    print("kbuAPI사용 중입니다.")
    await use_kbu_api()

asyncio.run(main())
