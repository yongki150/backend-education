import requests
from typing import List
from bs4 import BeautifulSoup


def get_notice(page) -> List[List[str]]:
    req = requests.get('https://www.bible.ac.kr/ko/life/notice' + '/list/' + str(page))
    soup = BeautifulSoup(req.text, 'html.parser')
    text_list = []
    for parent in soup.findAll("li", {'class' : 'tbody'}):
        text = parent.text
        text_list.append(text.replace("\n", " "))
    if len(text_list) == 0:
        return "잘못된 링크입니다."
    return text_list


def print_textlist(text_list):
    for text in text_list:
        print(text)


page = int(input('input page: '))
text_list = get_notice(page)
print_textlist(text_list)
