import time
from typing import List
from concurrent.futures import ProcessPoolExecutor

import requests
import asyncio
from bs4 import BeautifulSoup


async def get_url_return_soup(url) -> BeautifulSoup:
    #must get html
    req =  requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup


async def get_main_list(url) -> List[List[str]]:
    soup = await get_url_return_soup('https://www.bible.ac.kr/' + url)
    title = soup.select_one('div.header > h5').text
    name = soup.select('div.header > ul > li')[0].text
    date = soup.select('div.header > ul > li')[1].text
    main_text = soup.select('div.content')[0].text

    return [url, title, name, date, main_text.replace('\n', '').replace('\r\n', '').replace('\xa0', '')]


async def get_notice_articles(page_num) -> List[List[str]]:
    result_text = []
    soup = await get_url_return_soup('https://www.bible.ac.kr/ko/life/notice')
    tbodys = soup.select('li.tbody')
    for each_tbody in tbodys:
        link = each_tbody.select('span')[1].contents[1]['href'] #url
        result_text.append(await get_main_list(link))
    return result_text

async def _main(page_num : int):
    result_text = await get_notice_articles(page_num)
    print(result_text)

if __name__ == '__main__':
    page = int(input('input page: '))
    start = time.time()
    asyncio.run(_main(page))
    print('time: ', time.time() - start)