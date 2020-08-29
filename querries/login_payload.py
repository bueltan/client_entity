from Connection_endpoint import send_payload
import threading
import requests
import Connection_endpoint

def check_login(user, password):
    payload = '{"query": "{findAccount  (name:\\"' + user + '\\", password:\\"' + password + '\\"){id}}"}'
    json = send_payload(payload)
    print(payload)
    if json is not None:
        if json['data']['findAccount'] is not None:
            id = (json['data']['findAccount']['id'])
            return id
        else:
            id = None
            return id

def upload_image(file_name,path):
    base_url = Connection_endpoint.server_url + 'upload_p_image'
    headers = {'filename': file_name}
    with open(path, 'rb') as f:
        json =requests.post(base_url, data=f, headers=headers)
    return json

def get_data_account(id):
    payload = '{"query": "{account  (id:\\"' + id + '\\"){idName,name,email,password}}"}'
    json = send_payload(payload)
    print(payload)
    if json is not None:
        if json['data'] is not None:
            return json['data']['account']
        else:
            result = None
            return result