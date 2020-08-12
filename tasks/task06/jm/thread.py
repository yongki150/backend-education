import time
import unicodedata
from typing import List
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

def get_notice_articles(page):
    request = requests.get(page).text
    soup = BeautifulSoup(request, 'html.parser')

    table_list = soup.select('ul li.tbody')
    outline = []

    for element in table_list:
        url = element.select_one('div ul.black a')['href']
        url = "https://www.bible.ac.kr" + url

        title = element.select_one('.title').get_text()
        title = title.strip()

        name = element.select_one('.name').get_text()
        date = element.select_one('.reg_date').get_text()

        article = element.select_one('.content').get_text()
        article = article.strip()
        article = unicodedata.normalize("NFKD", article)
        outline.append([url, title, name, date, article])

    return outline

def get_notice_articles_thread(page_num: int = 1) -> List[List[str]]:
    page = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"

    request = requests.get(page).text
    soup = BeautifulSoup(request, 'html.parser')
    lists = soup.select('ul li.tbody')

    result = []
    futures = []
    target_page = "https://www.bible.ac.kr"

    with ThreadPoolExecutor() as executor:
        for links in lists:
            target_page = target_page + links.select_one('div ul.black a')['href']
            result.append(executor.submit(get_notice_articles, target_page))

        for future in futures:
            result.append(future.result())
    return result

if __name__ == '__main__':
    start = time.time()

    item = get_notice_articles_thread()
    for i in item:
        print(i.result())

    end = time.time()
    print(f'걸린 시간: {end - start}초')