"""
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-16 18:24:47
@LastEditTime : 2025-03-16 18:45:05
@LastEditors  : Niu zhixin
"""

import requests, os
#! from .createJWT import createJWT
import sys
import time
import jwt

def createJWT(private_key, project_id, key_id):
    payload = {
        'iat': int(time.time()) - 30,
        'exp': int(time.time()) + 900,
        'sub': project_id
    }
    headers = {
        'kid': key_id
    }

    encoded_jwt = jwt.encode(payload, private_key, algorithm='EdDSA', headers = headers)
    return encoded_jwt

def get_city_data(inputs: str):
    with open(
        f"{os.getcwd()}\\Scripts\\ed25519-private.pem", encoding="utf-8"
    ) as private_key_file:
        PRIVATE_KEY = private_key_file.read()
        PROJECT_ID = "29KVBFNRAX"
        KEY_ID = "CHPN48PMNJ"
        JWT = createJWT(PRIVATE_KEY, PROJECT_ID, KEY_ID)
    headers = {
        "Authorization": f"Bearer {JWT}",
    }
    params = {
        "location": inputs,
    }
    url = f"https://pn5pwbu9vu.re.qweatherapi.com/geo/v2/city/lookup?"
    try:
        locdata = requests.get(url=url, headers=headers, params=params).json()["location"]
        locid, locname = [], []
        for i in locdata:
            locid.append(i["id"])
            locname.append(i["name"])
    except:
        locid, locname = [], ["无城市"]

    return locid, locname


def get_weather(city: str, jwt: str):
    url = f"https://devapi.qweather.com/v7/weather/now"

