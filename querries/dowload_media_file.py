import requests
from general_functions.functions import get_extension


def get_media_file(payload):
    msg_id = payload['id']
    extension = get_extension(payload['type'])
    try:
        response = requests.get(payload['url'])
        dir_file = "./assets/media_file/" + msg_id + extension
        file = open(dir_file, "wb")
        file.write(response.content)
        file.close()
    except:
        print("somethings is wrong (get_media_file)")
