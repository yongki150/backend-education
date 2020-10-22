import json
from typing import Dict, List
from collections import defaultdict

import requests

def input_date() -> str:
    date = input('YYYY-MM-DD의 형식으로 입력하시오: ')
    return date

def init_header(date) -> json:  
    custom_header = {
        "MethodName":"GetPlaySequence",
        "channelType":"HO",
        "osType":"W",
        "osVersion":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "playDate": date,
        "cinemaID":"1|0001|1004",
        "representationMovieCode":""
    }
    custom_header = json.dumps(custom_header)
    return custom_header

def init_json(custom_header) -> json:
    data = {"paramList" : custom_header}
    url = 'https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx'
    r = requests.post(url, data = data).json()
    return r

    
def make_json_movie_data(movie_json) -> Dict[str, List[List[str]]]:
    dic = defaultdict(list)
    for info_movies in movie_json['PlaySeqs']['Items']:
        key_ = info_movies['MovieNameKR']
        start_time = info_movies['StartTime']
        end_time = info_movies['EndTime']
        dic[key_].append([start_time,end_time])
    return dic
        
date = input_date()
movie_json = init_json(init_header(date))
movie_data = make_json_movie_data(movie_json)

print(movie_data)
