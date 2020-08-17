import asyncio
import unicodedata
import time
from typing import List

import aiohttp
import requests
from bs4 import BeautifulSoup

async def get_article_notice(page):
    async with aiohttp.ClientSession() as session:
        async with session.get(page) as response:
            link = await response.text()

    soup = BeautifulSoup(link, 'html.parser')

    url = soup.select_one('link[rel="canonical"]')['href']

    title = soup.select_one('.header > h5').get_text()
    title = title.strip()

    name = soup.select_one('.name span[data-role="name"]').get_text()
    date = soup.select_one('time').get_text()

    article = soup.select_one('.content').get_text()
    article = article.strip()
    article = unicodedata.normalize("NFKD", article)

    return [url, title, name, date, article]

async def get_notice_articles_async(page_num: int = 1) -> List[List[str]]:
    page = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"
    request = requests.get(page).text
    soup = BeautifulSoup(request, 'html.parser')
    lists = soup.select('ul li.tbody')
    result = []

    base_page = "https://www.bible.ac.kr"

    for li in lists:
        target_page = base_page + li.select_one('span.title a')['href']
        result.append(get_article_notice(target_page))

    return await asyncio.gather(*result)

if __name__ == '__main__':
    start = time.time()

    item = asyncio.run(get_notice_articles_async())
    for i in item:
        print(i)

    end = time.time()
    print(f'걸린 시간: {end - start}')