from typing import Dict, List, Optional
from dataclasses import dataclass
import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup


@dataclass
class SemesterData:
    year: int
    semester: int


LOGIN_INFO = {
    'username': '',
    'password': ''
}


async def get_courses(semester: Optional[SemesterData] = None) -> Dict[str, List[str]]:
    try:
        login_url = "https://lms.bible.ac.kr/login.php"

        async with aiohttp.ClientSession() as session:
            login_req = await session.post(login_url, data=LOGIN_INFO)

            if semester is None:
                course_url = f"{str(login_req.url)}local/ubion/user/"
            else:
                course_url = f"{str(login_req.url)}/local/ubion/user/?year={semester.year}&semester={semester.semester}"

            course_req = await session.get(course_url)
            if course_req.status == 404:
                raise ValueError
            html = await course_req.text()

        soup = BeautifulSoup(html, 'html.parser')
        course_lists = soup.select('.my-course-lists > tr')

        tasks = {}
        for course in course_lists:
            title = course.select_one('.coursefullname').text
            tutor = course.select('td')[2].text
            tutee = course.select('td')[3].text
            tasks[title] = [tutor, tutee]

        return tasks

    except ValueError:
        print("로그인에 실패하였습니다. 정보를 재입력해주세요.")


async def main():
    st = time.time()

    print("default")
    print(await get_courses())
    print("-" * 30)
    print(await get_courses(SemesterData(2020, 10)))

    print(time.time() - st)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
