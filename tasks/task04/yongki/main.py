from typing import List

import requests
from bs4 import BeautifulSoup

def parse_url(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_notice_articles(page_num: int = 1) -> List[List[str]]:
    url = f"https://www.bible.ac.kr/ko/life/notice/list/{page_num}"
    articles = []
    li_s = parse_url(url).select('.tbody')

    for li in li_s:
        link = li.select_one('.title > a')['href']
        title = li.select_one('.title').text
        name = li.select_one('.name').text
        reg_date = li.select_one('.reg_date').text

        link = "https://www.bible.ac.kr" + link
        article = parse_url(link).select_one('.content').text

        title = title.replace("\n", "")
        article = article.replace("\n", "").replace("\xa0", "")

        li_list = [link, title, name, reg_date, article]
        articles.append(li_list)
    return articles

if __name__ == '__main__':
    for i in get_notice_articles(2):
        print(i)