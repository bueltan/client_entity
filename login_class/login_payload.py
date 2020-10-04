from connection_endpoint import send_payload
import threading
import requests
import connection_endpoint


def check_login(user, password):
    payload = '{"query": "{validateAccount  (idName:\\"' + user + '\\", password:\\"' + password + '\\"){id}}"}'
    json = send_payload(payload)
    if json is not None and json is not False:
        if json['data']['validateAccount'] is not None:
            id = (json['data']['validateAccount']['id'])
            return id
    if json is None:
        return None
    if json is False:
        return False


def upload_image(file_name, path):
    base_url = connection_endpoint.server_http + 'upload_p_image'
    headers = {'filename': file_name}
    with open(path, 'rb') as f:
        json = None  # requests.post(base_url, data=f, headers=headers)
    return json


def get_data_account(id):
    payload = '{"query": "{account  (id:\\"' + id + '\\"){idName,name,email,password}}"}'
    json = send_payload(payload)
    if json is not None:
        if json['data'] is not None:
            return json['data']['account']
        else:
            result = None
            return result
