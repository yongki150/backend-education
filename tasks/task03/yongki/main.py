import requests
from bs4 import BeautifulSoup
from typing import List

requests = requests.get("https://www.bible.ac.kr/ko/life/notice/list/1")
html = requests.text
soup = BeautifulSoup(html, 'html.parser')

def get_notice() -> List[List[str]]:
    li_s = soup.select('.tbody')
    lists = []

    for li in li_s:
        num = li.select_one('.loopnum')
        title = li.select_one('.title')
        name = li.select_one('.name')
        reg_date = li.select_one('.reg_date')

        list = [num.text, title.text, name.text, reg_date.text]
        list[1] = list[1].replace("\n", "")

        lists.append(list)
    return lists

if __name__ == '__main__':
    for i in get_notice():
        print(i)
