from typing import List
from typing import Dict
import time
import json
import requests

def get_movies_no_overlap(items_res) -> List[str]:
    movies = []

    for item in items_res:
        movie_name = item.get("MovieNameKR")
        if movie_name not in movies:
            movies.append(movie_name)
    return movies

def get_timetable(items_res) -> Dict[str, List[List[str]]]:
    info = {}
    for movie in get_movies_no_overlap(items_res):
        tables = []
        for item in items_res:
            if item.get("MovieNameKR") == movie:
                start_time = item["StartTime"]
                end_time = item["EndTime"]
                table = [start_time, end_time]
                tables.append(table)
        tables.sort()
        info[movie] = tables
    return info

def get_konkuk_movie_info(date: str) -> Dict[str, List[List[str]]]:
    # 날짜를 바꿔도 url이 같다? post방식
    # post는 Request URL과 parameter로 요청하여 접근한다.
    url = "https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
    param_list = {"MethodName": "GetPlaySequence", "channelType": "HO", "osType": "W",
                "osVersion": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
                "playDate": date, "cinemaID": "1|1|1004", "representationMovieCode": ""}

    parameter = {"paramList": json.dumps(param_list)}
    res = requests.post(url, data= parameter).json()
    items_res = res['PlaySeqs']['Items']

    # start = time.time()
    return get_timetable(items_res)

if __name__ == '__main__':
    print(get_konkuk_movie_info("2020-08-08"))
