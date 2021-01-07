from .payload_contact import check_if_exist, check_account_for_email, check_account
from general_functions.functions import get_nodes
from kivymd.uix.snackbar import Snackbar
data_contact = {}

def build_contact(data):
    global data_contact
    result = set_and_get(data)
    if result:
        for key in result:
            if result[key] is False:
                Snackbar(text="connection with the server was lost", padding="20dp").open()
                return None
            if key == 'node2':
                if result[key] is None:
                    Snackbar(text="Entity name not found", padding="20dp").open()
                    return None
                else:
                    data_contact['node2'] = get_nodes(data)['node2']
            if key == 'node3':
                if result[key] is None:
                    Snackbar(text="Area name not found", padding="20dp").open()
                    return None
                else:
                    data_contact['node3'] = get_nodes(data)['node3']
            if key == 'node4':
                if result[key] is None:
                    Snackbar(text="Member not found", padding="20dp").open()
                    return None
                else:
                    print("result", result['node4'], type(result))
                    data_contact['node4'] = result['node4']['idName']
                    data_contact['id_tk'] = result['node4']['id']
    else:
        Snackbar(text="No result, the input is incorrect", padding="20dp").open()
        return None
    return data_contact


def set_and_get(data):
    if data and len(data) >= 5:
        if data[0] == '@':
            """ the data is maybe entity name, check for nodes"""
            data_contact = check_if_exist(data)
            return data_contact

        if data[0] == '.':
            """ the data maybe is account name """
            data_contact = {'node4': check_account(data)}
            return data_contact

        if data.find("@") > 3 and data.find(".") > 4 and data.find("#") == -1:
            """ the data is maybe some email, try get account """
            data_contact = {'node4': check_account_for_email(data)}
            return data_contact

        if data.find("@") == -1 and data.find(".") == -1 and data.find("#") == -1 and len(data) < 16:
            """ the data maybe is account name, but without dot """
            data = '.' + data
            data_contact = {'node4': check_account(data)}
            print("data_contact: ", data_contact)
            return data_contact
    else:
        return None


