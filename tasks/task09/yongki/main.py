import asyncio

from biblebot import LmsAPI
from biblebot import IntranetAPI


async def use_login_class():
    # Login
    resp = await LmsAPI.Login.fetch("", "")
    result = LmsAPI.Login.parse(resp)
    cookie = result.data["cookies"]
    # print(result)

    # Get Profile
    resp = await LmsAPI.Profile.fetch(cookies=cookie)
    profile = LmsAPI.Profile.parse(resp)
    # print(profile)

    # Get CourseList
    resp = await LmsAPI.CourseList.fetch(cookies=cookie, semester="20202")
    result = LmsAPI.CourseList.parse(resp)
    # print(result)

    # Get Attendance
    resp = await LmsAPI.Attendance.fetch(cookies=cookie, course_code="1697")
    result = LmsAPI.Attendance.parse(resp)
    # print(result)


async def use_intranet_class():
    # Login
    response = await IntranetAPI.Login.fetch("", "")
    result = IntranetAPI.Login.parse(response)
    cookie = result.data["cookies"]
    print(result)

    # Get StudentPhoto
    resp = await IntranetAPI.StudentPhoto.fetch(cookies=cookie, sid="201504009")
    result = IntranetAPI.StudentPhoto.parse(resp)
    # print(result)

    # Get Chapel
    resp = await IntranetAPI.Chapel.fetch(cookies=cookie, semester="20202")
    result = IntranetAPI.Chapel.parse(resp)
    print(result)


async def main():
    await use_login_class()
    await use_intranet_class()

asyncio.run(main())
