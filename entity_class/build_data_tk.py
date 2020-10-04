import os
import requests
from rx import Observable
from general_functions import functions
from querries.message_database import get_oneMsg_local_db
import multiprocessing
from rx.concurrency import ThreadPoolScheduler
from ast import literal_eval
from path import dir_language, assets

optimal_thread_count = multiprocessing.cpu_count()
poo_scheduler = ThreadPoolScheduler(optimal_thread_count)

with open(dir_language, 'r') as file:
    dict_l = literal_eval(file.read())

dictionary = dict_l['card_subs']


def build_data_tk(*arg):
    data_to_return = {}
    last_msg = get_oneMsg_local_db(arg[0]['lastIdMsg'])
    msg = functions.show_last_msg(last_msg, dictionary)
    image_url = arg[0]['image']
    dir_profile = assets + arg[0]['idTk'] + ".png"
    if os.path.isfile(dir_profile):
        data_to_return['source_img'] = dir_profile

    if not os.path.isfile(dir_profile):
        if image_url:
            save_profile = {'url': image_url, 'id_tk': arg[0]['id_tk']}
            data_to_return['source_img'] = image_url
            Observable.of(save_profile) \
                .map(lambda i: get_profile_img(i)) \
                .subscribe_on(poo_scheduler).subscribe(on_error = lambda e : print("Error al descargar",e))
        else:
            dir_default = assets + "/img_profile/default_profile.png"
            data_to_return['source_img'] = dir_default

    if arg[0]['phone']:
        data_to_return['tertiary_text'] = 'WhatsApp ' + arg[0]['phone']
    else:
        data_to_return['tertiary_text'] = 'Entity'

    data_to_return['viewclass'] = 'itemTickets'
    data_to_return['text'] = arg[0]['name']
    data_to_return['secondary_text'] = msg
    data_to_return['name_icon'] = 'bell'
    data_to_return['name'] = arg[0]['id']


    return data_to_return


def get_profile_img(payload):
    tk_id = payload['id_tk']
    print("get_profile_img")
    print(payload['url'])
    response = requests.get(payload['url'])
    dir_profile = assets + "/img_profile/" + tk_id + ".png"
    file = open(dir_profile, "wb")
    if response:
        file.write(response.content)
    file.close()
