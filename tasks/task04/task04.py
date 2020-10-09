from typing import List

import requests
from bs4 import BeautifulSoup


def get_url_return_soup(url) -> List[BeautifulSoup]:
    #must get html
    req =  requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup

    
def get_main_article(url) -> str:
    soup = get_url_return_soup('https://www.bible.ac.kr/' + url)
    main_text = soup.select('div.content')[0].text
    """
    #\xa0 -> UTF-8로 인코딩 되었음을 알리는 문자
    01~nn 같은 규칙이 있는 경우, 반복문으로 문자열을 만들어 처리.
    불특정한 문자를 제거해야 하는 경우, 제거해야 할 문자를 담은 문자열 배열을 만들고,
    반복시켜 제거.
    """
    return main_text.replace('\n', '').replace('\r\n', '').replace('\xa0', '')


def get_notice_articles(page_num) -> List[List[str]]:
    result_text = []
    soup = get_url_return_soup('https://www.bible.ac.kr/ko/life/notice')
    tbodys = soup.select('li.tbody')
    for each_tbody in tbodys:
        each_text = []
        link = each_tbody.select('span')[1].contents[1]['href']
        each_text.append(link)
        
        for j in range(1, 5):
            if j == 3: #none text type, passing
                continue
            each_text.append(each_tbody.select('span')[j].contents[1].text)
        
        each_text.append(get_main_article(link)) #put main_article
        result_text.append(each_text) #put each_text to result_text => making 2D list
    
    return result_text


page = int(input('input page: '))

for text in get_notice_articles(page):
    print(text)


