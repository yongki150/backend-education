from typing import Dict, List
import json

import requests

def get_konkuk_movie_info(date: str) -> Dict[str, List[List[str]]]:
    item_list = []
    url = "https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
    form_data = {
        "MethodName":"GetPlaySequence",
        "channelType":"HO",
        "osType":"W",
        "osVersion":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                    "AppleWebKit/537.36 (KHTML, like Gecko)"
                    "Chrome/84.0.4147.105"
                    "Safari/537.36",
        "playDate":date,
        "cinemaID":"1|1|1004",
        "representationMovieCode":""
    }

    parameters = {"paramList": json.dumps(form_data)}
    response = requests.post(url, data = parameters).json()
    movies_response = response['PlaySeqs']['Items']

    for item in movies_response:
        title = item["MovieNameKR"]
        start = item["StartTime"]
        end = item["EndTime"]

        if [title] not in item_list:
            item_list.append([title])
        item_list.append([start, end])

    return item_list

if __name__ == '__main__':
    print(get_konkuk_movie_info("2020-08-17"))