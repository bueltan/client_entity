from general_functions.functions import get_nodes
from connection_endpoint import send_payload
from login_class.login import Login

def get_profile(resolve, value):
    payload = '{"query": "{' + resolve + ' (idName:\\"' + value + '\\"){name profileImg}}"}'
    json = send_payload(payload)
    if json:
        if 'errors' in json:
            return None
        if json['data'][resolve] == None:
            value = None
        else:
            value = (json['data'][resolve])
    else:
        return False
    return value


def to_check(value, resolve, field0, field1):
    payload = '{"query": "{' + resolve + ' (' + field0 + ':\\"' + value + '\\"){' + field1 + ', id}}"}'
    json = send_payload(payload)
    if json:
        if 'errors' in json:
            return None
        if json['data'][resolve] == None:
            value = None
        else:
            value = (json['data'][resolve])
    else:
        return False
    return value


def check_node3(entity, area_name):
    payload = '{"query":"{checkNameArea(fkIdEntity:' \
              '\\"' + entity + '\\"nameArea:\\"' + area_name + '\\"){id}}"}'
    json = send_payload(payload)

    if json:
        if 'errors' in json:
            return None
        if json['data']['checkNameArea'] == None:
            value = None
        if json['data']['checkNameArea']:
            value = (json['data']['checkNameArea']['id'])
    else:
        return False
    return value

def check_node4(**kwargs):
    id_name = kwargs.get('node4')
    id_area = kwargs.get('node3')
    entity = kwargs.get('node2')
    if id_area:
        payload = '{"query":"{checkMemberInArea(fkIdArea:\\"' + id_area\
                  + '\\", idNameAccountMember: \\"' + id_name + '\\"){edges{node{id}}}}"}'
        resolve = 'checkMemberInArea'
    else:
        payload = '{"query": "{checkMemberInEntity (idNameEntity: \\"' + entity\
                  + '\\", idNameAccountMember:\\"' + id_name + '\\"){edges{node{id}}}}"}'
        resolve = 'checkMemberInEntity'

    json = send_payload(payload)

    if json:
        if 'errors' in json:
            return None
        if len(json['data'][resolve]['edges']) == 0:
            value = None
        else:
            result = (json['data'][resolve]['edges'])
            value = result[0]['node']['id']
    else:
        return False
    return value


def check_account(id_name):
    node4_and_id_tk = to_check(id_name, 'checkIdNameAccount', 'idName', 'idName')
    return node4_and_id_tk

def check_account_for_email(email):
    node4_and_id_tk = to_check(email, 'checkEmailAccount', 'email', 'idName')
    return node4_and_id_tk


def check_if_exist(data):
    nodes = get_nodes(data)
    dict_result = {}
    for i in nodes:
        if i == 'node2' and nodes.get(i) != '':
            result = to_check(nodes.get('node2'), 'checkEntityIdName', 'idName', 'idName')
            if result is False or None:
                dict_result['node2'] = result
                return dict_result
            else:
                dict_result['node2'] = result
        if i == 'node3' and nodes.get(i) != '':
            result = check_node3(nodes.get('node2'), nodes.get('node3'))
            if result is False:
                dict_result['node3'] = result
                return dict_result
            else:
                dict_result['node3'] = result

        if i == 'node4' and nodes.get(i) != '':
            dict_result['node4'] = nodes['node4']
            result = check_node4(**dict_result)
            dict_result['node4'] = result
    return dict_result


def save_contact(**kwargs):
    print("welcome to save_contact")
    data_contact = {'id_account': '', 'id_contact': '', \
                    'type_contact': '', 'name_contact': '', \
                    'node2': '', \
                    'node3': '', 'node4': '', 'phone': ''}

    data_contact['id_account'] = Login.data_login['my_id']

    for key in kwargs:
        if key == 'name' and kwargs.get(key) != None :
            data_contact['name_contact'] = kwargs.get(key)
        if key == 'profileImg' and kwargs.get(key) != None:
            data_contact['image_contact'] = kwargs.get(key)
        if key == 'id_tk':
            data_contact['id_contact'] = kwargs.get(key)
        if key in data_contact:
            data_contact[key] = kwargs.get(key)
        if 'phone' in kwargs:
            data_contact['type_contact'] = 'wapp'
        else:
            data_contact['type_contact'] = 'entity'
    print(data_contact)
