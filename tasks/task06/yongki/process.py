from typing import List
import unicodedata
import time
from concurrent.futures import ProcessPoolExecutor

import requests
from bs4 import BeautifulSoup

def get_article_from_url(url):
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('.header > h5').text
    content = soup.select_one('.content').text
    name = soup.select_one('span[data-type="nickname"]').text
    date = soup.select_one('time').text

    title = title.replace("\n", "")
    content = content.replace("\n", "")
    content = unicodedata.normalize("NFKD", content)

    return [title, name, content, date]


def get_notice_articles_process(page_num: int = 1) -> List[List[str]]:
    url = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    li_s = soup.select('.tbody')

    async_base_url = "https://www.bible.ac.kr"

    with ProcessPoolExecutor(max_workers=len(li_s)) as executor:
        tasks = [executor.submit(get_article_from_url,
                                 async_base_url + li.select_one('.title > a')['href']) for li in li_s]

    return tasks

if __name__ == '__main__':
    st = time.time()
    articles = get_notice_articles_process(1)
    for i in articles:
        print(i.result())
    print(time.time() - st)
