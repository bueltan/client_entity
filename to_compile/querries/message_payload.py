from Connection_endpoint import send_payload
from querries.message_database import load_msg_in_database
from querries.dowload_media_file import get_media_file
from rx import Observable
import multiprocessing
from rx.concurrency import ThreadPoolScheduler

optimal_thread_count = multiprocessing.cpu_count()
poo_scheduler = ThreadPoolScheduler(optimal_thread_count)


def get_msg(session, id_msg, ticketsId, timestamp):
    payload = '{"query": "{getMessage (id:\\"' + id_msg + '\\"){type,text,fromMe,mime,url,caption,filename,payload,vcardList}}"}'
    json = send_payload(payload)
    if json is not None:
        if json['data']['getMessage'] is not None:
            source = (json['data']['getMessage'])
            source['id'] = id_msg
            source['ticketsId'] = ticketsId
            source['timestamp'] = timestamp
            load_msg_in_database(session, source)
            if source['type'] == 'image':
                Observable.of(source) \
                    .map(lambda i: get_media_file(i)) \
                    .subscribe_on(poo_scheduler).subscribe(on_error = lambda e : print(e))
