from typing import List

import requests
from bs4 import BeautifulSoup

def get_notice() -> List[List[str]]:
    req = requests.get("https://www.bible.ac.kr/ko/life/notice/list/1")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    li_s = soup.select('.tbody')
    notice = []

    for li in li_s:
        num = li.select_one('.loopnum')
        title = li.select_one('.title')
        name = li.select_one('.name')
        reg_date = li.select_one('.reg_date')

        li_list = [num.text, title.text, name.text, reg_date.text]
        li_list[1] = li_list[1].replace("\n", "")

        notice.append(li_list)
    return notice

if __name__ == '__main__':
    for i in get_notice():
        print(i)
