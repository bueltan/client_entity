from general_functions.functions import get_nodes, get_code_entity
from connection_endpoint import send_payload


def to_check(value, resolve, field):
    payload = '{"query": "{' + resolve + ' (' + field + ':\\"' + value + '\\"){'+field+'}}"}'
    json = send_payload(payload)
    print(payload)
    print(json)
    if json:
        if json['data'][resolve] is not None and not False:
            id = (json['data'][resolve][field])
            return id

    else:
        return json


def check_node3(entity, area_name):
    code = get_code_entity(entity)
    payload = '{"query": "{ checkNameArea (fkIdCode:\\"' + code + '\\" areaName:\\"' + area_name + '\\"  ){areaName}}"}'
    json = send_payload(payload)
    print(payload)
    print(json)
    if json:
        if json['data']['checkNameArea'] is not None and not False:
            id = (json['data']['checkNameArea']['areaName'])
            return id
    else:
        return json


def check_node4(entity, area_name, id_name):
    pass


def check_account(entity):
    pass


def check_if_exist(data):
    nodes = get_nodes(data)
    for i in nodes[0]:
        if i == 'node2':
            result = to_check(nodes[0].get(i), 'checkEntityIdName', 'idName')
            if result is False or None:
                return result, nodes[i]

        if i == 'node3':
            result = check_node3(nodes[0].get('node2'), nodes[0].get(i))
            if result is False or None:
                return result, nodes[i]

        if i == 'node4':
            result = check_node3(nodes[0].get('node2'), nodes[0].get('node3'), nodes[0].get(i))
            if result is False or None:
                return result, nodes[i]
