from typing import List
import unicodedata
import time
import asyncio

import aiohttp
import requests
from bs4 import BeautifulSoup


async def get_article_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            html = await res.text()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('.header > h5').text
    content = soup.select_one('.content').text
    name = soup.select_one('span[data-type="nickname"]').text
    date = soup.select_one('time').text

    title = title.replace("\n", "")
    content = content.replace("\n", "")
    content = unicodedata.normalize("NFKD", content)

    return [title, name, content, date]


async def get_notice_articles_async(page_num: int = 1) -> List[List[str]]:
    url = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    li_s = soup.select('.tbody')

    async_base_url = "https://www.bible.ac.kr"
    
    tasks = []
    for li in li_s:
        async_url = async_base_url + li.select_one('.title > a')['href']
        tasks.append(get_article_from_url(async_url))

    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    st = time.time()
    articles = asyncio.run(get_notice_articles_async(1))
    for i in articles:
        print(i)
    print(time.time() - st)
