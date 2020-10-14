""""  sync data """
import json
import time

from connection_endpoint import send_payload
from querries import tickets_database
from ast import literal_eval
from path import dir_settings_file


def read_in_file_global_var():
    with open(dir_settings_file, 'r') as file:
        try: data = literal_eval(file.read())
        except: data = None
        finally:
            return data


def write_in_file_global_var(sub, **kwargs):
    data = read_in_file_global_var()
    if not data: data = {}
    if sub not in data: data[sub] = {}
    if not kwargs: return None
    for key in kwargs:
        data[sub][key] = kwargs.get(key)
    with open(dir_settings_file, 'w') as file:
        try:
            json.dump(data, file), file.close()
        except:
            data = None, file.close()
        finally:
            return data


def sync_tickets(nodes, my_id):
    sub = nodes['node2'] + nodes['node3'] + nodes['node4']
    file_var = read_in_file_global_var()
    last_sync_timestamp = 0

    if file_var:
        if sub in file_var:
            last_sync_timestamp = file_var[sub]['last_sync_timestamp']
    now_timestamp = round(time.time())
    write_in_file_global_var(sub, last_sync_timestamp=now_timestamp)
    payload = '{"query": "{ticketList(node2:\\"' + nodes['node2'] \
                  + '\\", node3:\\"' + nodes['node3'] \
                  + '\\", node4:\\"' + nodes['node4'] \
                  + '\\", timestamp:\\"' + str(last_sync_timestamp) \
                  + '\\"){edges{node {id, idTk, idCode, node2, node3, node4,name, timestamp, image, phone,lastIdMsg}}}}"}'

    json = send_payload(payload)
    if json is not None:
        if json['data']['ticketList']['edges'] != []:
            source = (json['data']['ticketList']['edges'])
            tickets_database.load_tk_in_database(source, str(last_sync_timestamp))

