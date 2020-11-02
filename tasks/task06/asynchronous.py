import time
from typing import List

import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup



async def get_url_return_soup(url) -> BeautifulSoup:
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as text:
            html = await text.text('utf8')
            soup = BeautifulSoup(html, 'html.parser')
    return soup


async def get_main_list(each_tbody) -> List[List[str]]:
    link = each_tbody.select('span')[1].contents[1]['href']
    soup = await get_url_return_soup('https://www.bible.ac.kr/' + link)
    title = soup.select_one('div.header > h5').text
    name = soup.select('div.header > ul > li')[0].text
    date = soup.select('div.header > ul > li')[1].text
    main_text = soup.select('div.content')[0].text
    return [link, title, name, date, main_text.replace('\n', '').replace('\r\n', '').replace('\xa0', '')]


async def get_notice_articles(page_num) -> List[List[str]]:
    result_text = []
    soup = await get_url_return_soup('https://www.bible.ac.kr/ko/life/notice')
    tbodys = soup.select('li.tbody')
    for each_tbody in tbodys: #url
        result_text.append(asyncio.create_task(get_main_list(each_tbody)))
    await asyncio.gather(*result_text)
    return result_text
    

async def _main(page_num : int):
    result_texts = await get_notice_articles(page_num)
    for result_text in result_texts:
        print(result_text.result())


if __name__ == '__main__':
    page = int(input('input page: '))
    asyncio.run(_main(page))