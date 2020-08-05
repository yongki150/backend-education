from typing import List

import requests
from bs4 import BeautifulSoup

def target_page(page):
    request = requests.get(page).text
    soup = BeautifulSoup(request, 'html.parser')

    return soup

def get_notice_articles(page_num: int = 1) -> List[List[str]]:
    page = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"
    table_list = target_page(page).select('ul li.tbody')
    outline = []

    for element in table_list:
        url = element.select_one('div ul.black a')['href']
        url = "https://www.bible.ac.kr" + url

        title = element.select_one('.title').get_text()
        title = title.strip()

        name = element.select_one('.name').get_text()
        date = element.select_one('.reg_date').get_text()

        article = target_page(url).select_one('.content').get_text()
        article = article.strip().replace("\xa0", "")

        outline.append([url, title, name, date, article])

    return outline

if __name__ == '__main__':
    for item in get_notice_articles(3):
        print(item)