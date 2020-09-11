import requests

server_http = 'http://localhost:5000/'
base_url_http = server_http + 'graphql'
base_url_ws = 'ws://localhost:5000/subscriptions'
headers = {'content-type': 'application/json'}


def send_payload(payload):
    response = requests.post(base_url_http, headers=headers, data=payload)
    json = response.json()
    if response.status_code == 200:
        return json
