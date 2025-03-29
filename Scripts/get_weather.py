"""
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-16 18:24:47
@LastEditTime : 2025-03-29 17:34:34
@LastEditors  : Niu zhixin
"""

"""
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-16 18:24:47
@LastEditTime : 2025-03-29 17:32:47
@LastEditors  : Niu zhixin
"""

"""
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-16 18:24:47
@LastEditTime : 2025-03-16 18:45:05
@LastEditors  : Niu zhixin
"""

import requests, gzip


def get_city(inputs: str, jwt: str):
    headers = {
        "Authorization": f"Bearer {jwt}",
    }
    params = {
        "location": inputs,
    }
    url = f"https://geoapi.qweather.com/v2/city/lookup?"
    locdata = requests.get(url=url, headers=headers, params=params).json()['location']
    locid, locname = [], []
    for i in locdata:
        locid.append(i["id"])
        locname.append(i["name"])

    return locid, locname


def get_weather(city: str, jwt: str):
    url = f"https://devapi.qweather.com/v7/weather/now"


