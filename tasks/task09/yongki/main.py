import asyncio

from biblebot import LmsAPI

INFO = {
    "ID": "",
    "passWD": "",
    "semester": "20202",
}


async def use_login_api():
    # Login
    resp = await LmsAPI.Login.fetch(INFO["ID"], INFO["passWD"])
    result = LmsAPI.Login.parse(resp)
    cookie = result.data["cookies"]
    print(result)

    # Get Profile
    resp = await LmsAPI.Profile.fetch(cookies=cookie)
    profile = LmsAPI.Profile.parse(resp)
    print(profile)

    # Get CourseList
    resp = await LmsAPI.CourseList.fetch(cookies=cookie, semester=INFO["semester"])
    result = LmsAPI.CourseList.parse(resp)
    print(result)

    # Get Attendance
    resp = await LmsAPI.Attendance.fetch(cookies=cookie, course_code="1697")
    result = LmsAPI.Attendance.parse(resp)
    print(result)


async def main():
    await use_login_api()

asyncio.run(main())
