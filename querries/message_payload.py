from connection_endpoint import send_payload
from querries.message_database import load_msg_in_database
from querries.dowload_media_file import get_media_file
from rx import Observable
import multiprocessing
from rx.concurrency import ThreadPoolScheduler

optimal_thread_count = multiprocessing.cpu_count()
poo_scheduler = ThreadPoolScheduler(optimal_thread_count)

from connection_endpoint import send_payload
from querries import message_database


def get_message(session, id, timestamp):
    payload = '{"query": "{listMessage (ticketsId:\\"' + id + '\\", timestamp:\\"'+timestamp+'\\" )' \
              '{edges{node {ticketsId,id,type,text,fromMe,mime,url,caption,filename,payload,vcardList,timestamp}}}}"}'
    json = send_payload(payload)

    if json is not None:
        if json['data']['listMessage']['edges'] != []:
            source = (json['data']['listMessage']['edges'])
            message_database.load_msg_in_database(session, source)

