from typing import Dict, List, Optional
from dataclasses import dataclass
import asyncio
import time

import requests
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

        if semester is None:
            course_url = "https://lms.bible.ac.kr/local/ubion/user/"
        else:
            course_url = f"https://lms.bible.ac.kr/local/ubion/user/?year={semester.year}&semester={semester.semester}"

        with requests.Session() as session:
            login_req = session.post(login_url, data=LOGIN_INFO)
            login_cookie = login_req.cookies.get_dict()
            # print(login_cookie)

            course_req = session.get(course_url)

        # 쿠키가 있는데 로그인정보가 실패??
        if login_cookie:
            raise ValueError

        soup = BeautifulSoup(course_req.text, 'html.parser')
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

asyncio.run(main())
