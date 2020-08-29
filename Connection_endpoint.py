import requests

server_url =  'http://192.168.0.11:5000/'
base_url = server_url+'graphql'
base_url_ws = 'ws://192.168.0.11:5000/subscriptions'
headers = {'content-type': 'application/json'}

def send_payload(payload):
    response = requests.post(base_url, headers=headers, data=payload)
    json = response.json()
    if response.status_code == 200:
        return json




