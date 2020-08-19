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
    login_url = "https://lms.bible.ac.kr/login.php"

    if semester is None:
        course_url = "https://lms.bible.ac.kr/local/ubion/user/"
    else:
        course_url = f"https://lms.bible.ac.kr/local/ubion/user/?year={semester.year}&semester={semester.semester}"


    session = requests.Session()
    login_req = session.post(login_url, data=LOGIN_INFO)
    login_req.raise_for_status()  # 200이 아니면 error 발생

    # print(session.cookies.get_dict())

    course_req = session.get(course_url)
    course_req.raise_for_status()

    soup = BeautifulSoup(course_req.text, 'html.parser')
    course_lists = soup.select('.my-course-lists > tr')
    tasks = {}
    for course in course_lists:
        title = course.select_one('.coursefullname').text
        tutor = course.select('td')[2].text
        tutee = course.select('td')[3].text
        tasks[title] = [tutor, tutee]

    return tasks


async def main():
    st = time.time()
    print("default")
    print(await get_courses())
    print("-" * 30)
    print(await get_courses(SemesterData(2020, 10)))
    print(time.time() - st)

asyncio.run(main())
