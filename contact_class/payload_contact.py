from general_functions.functions import get_nodes, get_code_entity
from connection_endpoint import send_payload


def to_check(value, resolve, field):
    payload = '{"query": "{' + resolve + ' (' + field + ':\\"' + value + '\\"){' + field + '}}"}'
    json = send_payload(payload)
    if json:
        if json['data'][resolve] is not None and not False:
            value = (json['data'][resolve][field])
            return True, value
    else:
        return json, False


def check_node3(entity, area_name):
    payload = '{"query": "{ checkNameArea (fkIdEntity:\\"' + entity + '\\" areaName:\\"' + area_name + '\\"  ){id}}"}'
    json = send_payload(payload)
    if json:
        if json['data']['checkNameArea'] is not None and not False:
            value = (json['data']['checkNameArea']['id'])
            return True, value
    else:
        return json, False


def check_node4(id_name, id_area):
    if id_area is not None:
        payload = '{"query":{"checkMemberInArea(fkIdArea: ' \
                  '\\"' + id_area + '\\" idNameAccountMember: ''\\"' + id_name + '\\"){edges{node{id}}}}"}'
        json = send_payload(payload)
        if json:
            if json['data']['checkMemberInArea'] is not None and not False:
                value = (json['data']['checkMemberInArea']['id'])
                return True, value
        else:
            return json, False
    else:
        payload = '{"query":{"checkMemberInEntity(idNameEntity: ' \
                  '\\"' + id_name_entity + '\\" idNameAccountMember: ''\\"' + id_name + '\\"){edges{node{id}}}}"}'
        json = send_payload(payload)
        if json:
            if json['data']['checkMemberInEntity'] is not None and not False:
                value = (json['data']['checkMemberInEntity']['id'])
                return True, value


def check_account(entity):
    pass


def check_if_exist(data):
    nodes = get_nodes(data)
    dict_result = {}
    for i in nodes:
        if i == 'node2' and nodes.get(i) is not '':
            result = to_check(nodes.get(i), 'checkEntityIdName', 'idName')
            if result is False or None:
                dict_result['node2'] = result
                return nodes, dict_result
            else:
                dict_result['node2'] = result

        if i == 'node3' and nodes.get(i) is not '':
            result = check_node3(nodes.get('node2'), nodes.get(i))
            if result is False:
                dict_result['node3'] = result
                return nodes, dict_result
            else:
                dict_result['node3'] = result

        if i == 'node4' and nodes.get(i) is not '':
            result = check_node4(nodes.get(i), dict_result['node3'])
            dict_result['node4'] = result
    return dict_result
