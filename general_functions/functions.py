import re
import shutil

def detect_nodes(subscription):
    nodes_contains = {'id_code': False, 'node2': False, 'node3': False, 'node4': False}
    if subscription.find(".") != -1:
        nodes_contains['node4'] = True
        subscription.splitlines()
    if subscription.find("#") != -1:
        nodes_contains['node3'] = True
    if subscription.find("@") != -1:
        nodes_contains['node2'] = True
    if subscription.find("@") != -1 and subscription.find("@") != 0:
        nodes_contains['id_code'] = True
    return nodes_contains


def get_nodes(subscriptions):
    nodes = {'id_code': 0, 'node2': '', 'node3': '', 'node4': ''}
    nodes_contains = detect_nodes(subscriptions)
    if nodes_contains['node4'] == True and nodes_contains['node3'] == False:
        nodes['node4'] = subscriptions
    if nodes_contains['node3'] == True and nodes_contains['node4'] == False:
        nodes['node3'] = "#"+subscriptions.split("#")[1]
    if nodes_contains['node3'] == True and nodes_contains['node4'] == True:
       sub = subscriptions.split("#")[1]
       nodes['node3'] = "#" + sub.split(".")[0]
    if nodes_contains['node2'] == True and nodes_contains['node3'] == False and nodes_contains['id_code'] == False:
        nodes['node2'] = subscriptions
    if nodes_contains['node2'] == True and nodes_contains['node3'] == True and nodes_contains['id_code'] == False:
        nodes['node2'] = subscriptions.split("#")[0]
    if nodes_contains['node2'] == True and nodes_contains['node3'] == True and nodes_contains['id_code'] == True:
        sub = subscriptions.split("#")[0]
        nodes['node2'] = "@" + sub.split("@")[1]
    if nodes_contains['node4'] == True and nodes_contains['node3'] == True:
        nodes['node4'] = "." + subscriptions.split(".")[1]
    if nodes_contains['id_code'] == True:
        nodes['id_code'] = subscriptions.split("@")[0]
    if nodes_contains['id_code'] == True and nodes_contains['node3'] == False :
        nodes['node2'] = "@" + subscriptions.split("@")[1]



    return nodes

def show_last_msg(payload, word):
    if payload['type'] == "text":
        return payload['text']
    if payload['type'] == "ptt":
        return word['ticket_audio']
    if payload['type'] == "image":
        return word['ticket_image']
    if payload['type'] == "location":
        return word['ticket_location']
    if payload['type'] == "document":
        return word['ticket_document']


def format_text(text):
    text = re.sub(' +', ' ', text)
    return text


def count_lent_sentence(text):
    count = 0
    sentence = ""
    parcial = 0
    for character in text:
        if character != "\n":
            sentence += character
            parcial = len(sentence)
        else:
            if parcial > count:
                count = len(sentence)
                sentence = ""

    if parcial > count:
        count = len(sentence)

    return  count


def get_extension(type):

    if type == 'audio':
        extension = '.ogg'

    if type == 'image':
        extension = '.png'

    return extension


def get_resolution_img(url):
    size = url.split("size=")[1]
    width = int(size.split("x")[0])
    height = int(size.split("x")[1])
    return width, height


def get_height_img(width, height, width_end):
    percent = 100 * float(width_end) / float(width)
    height_end = round(height / 100 * percent)
    return width_end, height_end
#print(get_height_img(720, 1280, 300))


def save_dir_in_db(dir, table):
    pass

def copy(src_file, dest_file):
    shutil.copy2(src_file, dest_file, follow_symlinks=True)

