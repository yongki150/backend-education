from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import time

import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup as bs

class SemesterData:
    year : int
    semester : int


def make_data_list(start_ind : int, text: str) -> [str, str, str]:
    resultname = ''
    professor = ''
    num = ''
    for i in range(start_ind, len(text)):
        resultname += text[i]
        if text[i] == ']':
            break
    for i in range(i + 1, len(text)):
        if(text[i].isdigit()):
            break
        professor += text[i]
    for i in range(i, len(text)):
        num += text[i]

    return [resultname, professor, num]

    
async def get_courses(semester: Optional[SemesterData] = None) -> Dict[str, List[str]]:
    ##세션 데이터 받아옴.
    return_data = dict() #type dict
    userinfo = setting_user_info()
    data = {
        'username' : userinfo['name'],
        'password' : userinfo['password'],
    }
    ##세션 요청함.
    async with aiohttp.ClientSession() as s:
        await s.post('https://lms.bible.ac.kr/login.php', data = data)
        url = 'https://lms.bible.ac.kr/local/ubion/user/'
        if semester:
            url += '?year=' + str(semester[0]) + '&semester=' + str(semester[1])
        #강의 페이지 접속
        async with s.get(url) as spost:
            text = await spost.text()
    soup = bs(text, 'html.parser')
    snames = soup.select('tbody > tr')
    for sname in snames:
        start_ind = sname.text.find(' ')
        data = make_data_list(start_ind + 1, sname.text)
        return_data[data[0]] = [data[1], data[2]]

    return return_data
    

def setting_user_info() -> Dict:
    userinfo = dict()
    userinfo['name'] = input('input_ID: ')
    userinfo['password'] = input('input_PW: ')
    return userinfo


async def main_():
    dic_data = await get_courses((2020, 1)) #비동기로 실행 (dict자료형 불러옴)
    to_json = json.dumps(dic_data) #json 형식으로 변경
    print(json.loads(to_json)) #json파일 인코딩

if __name__ == "__main__":
    asyncio.run(main_())