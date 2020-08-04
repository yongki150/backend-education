import requests
from bs4 import BeautifulSoup
from typing import List

def get_notice() -> List[List[str]]:
    req = requests.get('https://www.bible.ac.kr/ko/life/notice').text
    soup = BeautifulSoup(req, 'html.parser')
    lists = soup.select('ul li.tbody')
    temp_list = []
    item = 0

    for list in lists:
        num = list.select_one('.loopnum').get_text()
        title = list.select_one('.title').get_text()
        name = list.select_one('.name').get_text()
        date = list.select_one('.reg_date').get_text()

        temp_list.append([num, title, name, date])

    for item in temp_list:
        print(item)

    return item

if __name__ == '__main__':
    get_notice()