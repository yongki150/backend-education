from typing import List

import requests
from bs4 import BeautifulSoup

def get_notice() -> List[List[str]]:
    request = requests.get('https://www.bible.ac.kr/ko/life/notice').text
    soup = BeautifulSoup(request, 'html.parser')
    table_list = soup.select('ul li.tbody')
    outline = []

    for element in table_list:
        num = element.select_one('.loopnum').get_text()
        title = element.select_one('.title').get_text()
        name = element.select_one('.name').get_text()
        date = element.select_one('.reg_date').get_text()

        outline.append([num, title, name, date])

    return outline

if __name__ == '__main__':
    for item in get_notice():
        print(item)