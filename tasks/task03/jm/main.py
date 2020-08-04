import requests
from bs4 import BeautifulSoup
from typing import List

req = requests.get('https://www.bible.ac.kr/ko/life/notice').text
soup = BeautifulSoup(req, 'html.parser')

def get_notice() -> List[List[str]]:
    hotkeys = soup.select('ul li.tbody')
    temp_list = []

    for list in hotkeys:
        num = list.select_one('.loopnum').get_text()
        title = list.select_one('title').get_text()
        name = list.select_one('.name').get_text()
        date = list.select_one('.reg_date').get_text()

        temp_list.append([num, title, name, date])

    return temp_list

if __name__ == '__main__':
    for item in get_notice():
        print(item)