import time
import unicodedata
from typing import List
from concurrent.futures import ProcessPoolExecutor

import requests
from bs4 import BeautifulSoup

url = 0

def target_page(page):
    request = requests.get(page).text
    soup = BeautifulSoup(request, 'html.parser')

    return soup

def get_notice_articles(page_num: int = 1) -> List[List[str]]:
    page = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"
    table_list = target_page(page).select('ul li.tbody')
    outline = []

    for element in table_list:
        global url
        url = element.select_one('div ul.black a')['href']
        url = "https://www.bible.ac.kr" + url

        title = element.select_one('.title').get_text()
        title = title.strip()

        name = element.select_one('.name').get_text()
        date = element.select_one('.reg_date').get_text()

        article = target_page(url).select_one('.content').get_text()
        article = article.strip()
        article = unicodedata.normalize("NFKD", article)

        outline.append([url, title, name, date, article])

    return outline

def get_notice_articles_process(page_num: int = 1) -> List[List[str]]:
    page = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"

    with ProcessPoolExecutor(max_workers=len(target_page(page).select('ul li.tbody'))) as executor:
        tasks = [executor.submit(get_notice_articles, url)]

    return tasks

if __name__ == '__main__':
    start = time.time()

    item = get_notice_articles_process()
    for i in item:
        print(i.result())

    end = time.time()
    print(f'걸린 시간: {end - start}초')