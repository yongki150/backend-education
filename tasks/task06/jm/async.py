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

async def get_notice_articles_async(page_num: int = 1) -> List[List[str]]:
    page = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"
    request = requests.get(page).text
    soup = BeautifulSoup(request, 'html.parser')
    lists = soup.select('ul li.tbody')

    target_page = "https://www.bible.ac.kr"

    for sel in lists:
        target_page = target_page + sel.select_one('div ul.black a')['href']
        result = [asyncio.create_task(get_article_notice(target_page))]

    return await asyncio.gather(*result)

if __name__ == '__main__':
    start = time.time()

    item = asyncio.run(get_notice_articles_async())
    for i in item:
        print(i)

    end = time.time()
    print(f'걸린 시간: {end - start}')