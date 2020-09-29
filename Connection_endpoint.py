import os

import requests
dir_settings_file = f"{os.environ['ENTITY_CLIENT_ROOT']}/assets/resource_files/settings/GLOBAL_VAR.json"
dir_language = f"{os.environ['ENTITY_CLIENT_ROOT']}/assets/resource_files/language/spanish_after_login.json"
server_http = 'http://192.168.0.13:5000/' #'http://192.168.0.22:5000/'
base_url_http = server_http + 'graphql'#
base_url_ws = 'ws://192.168.0.13:5000/subscriptions'#'ws://192.168.0.22:5000/subscriptions'
headers = {'content-type': 'application/json'}


def send_payload(payload):
    response = requests.post(base_url_http, headers=headers, data=payload)
    json = response.json()
    if response.status_code == 200:
        return json
