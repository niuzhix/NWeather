'''
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-27 16:29:07
@LastEditTime : 2025-03-27 16:31:07
@LastEditors  : Niu zhixin
'''
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


