from typing import List
from typing import Dict

from collections import defaultdict

import json
import requests


def get_timetable(items_res) -> Dict[str, List[List[str]]]:
    info = defaultdict(list)

    for item in items_res:
        name = item["MovieNameKR"]
        start_time = item["StartTime"]
        end_time = item["EndTime"]
        info[name].append([start_time, end_time])

    for key in info:
        info[key].sort()

    return info


def get_konkuk_movie_info(date: str) -> Dict[str, List[List[str]]]:
    url = "https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
    param_list = {
        "MethodName": "GetPlaySequence",
        "channelType": "HO",
        "osType": "W",
        "osVersion": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                     "AppleWebKit/537.36 (KHTML, like Gecko)"
                     "Chrome/84.0.4147.105 Safari/537.36",
        "playDate": date,
        "cinemaID": "1|1|1004",
        "representationMovieCode": ""}

    parameter = {"paramList": json.dumps(param_list)}
    res = requests.post(url, data=parameter).json()
    items_res = res['PlaySeqs']['Items']

    return get_timetable(items_res)


if __name__ == '__main__':
    print(get_konkuk_movie_info("2020-08-08"))
