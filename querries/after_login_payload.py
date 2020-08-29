from Connection_endpoint import send_payload
from querries import tickets_database
import base64


def get_subscritions(accout_name_id):
    payload = '{"query": "{subscriptionList (idNameAccount:\\"'+accout_name_id+'\\")\
               {edges {node {source,id}}}}"}'
    json = send_payload(payload)
    if json is not None:
        if json['data']['subscriptionList'] is not None:
            source = (json['data']['subscriptionList']['edges'])
            return source
        else:
            source = []
            return source


def get_tickets(nodes):
    payload = '{"query": "{ticketList(idCode:\\"' + str(nodes['id_code'])\
              + '\\", node2:\\"' + nodes['node2']\
              + '\\", node3:\\"' + nodes['node3']\
              + '\\", node4:\\"' + nodes['node4']\
              + '\\"){edges{node {id, idTk, idCode, node2, node3, node4,name, timestamp, image, phone,lastIdMsg, count}}}}"}'

    json = send_payload(payload)
    if json is not None:
        if json['data']['ticketList']['edges'] != []:
            source = (json['data']['ticketList']['edges'])
            for tk in source:
                tk = tk['node']
                tk['id_code'] = tk.pop('idCode')
                tk['last_id_msg'] = tk.pop('lastIdMsg')
                tk['id_tk'] = tk.pop('idTk')
                id = tk['id']
                tk['id'] = (base64.standard_b64decode(id)).decode("utf-8").split(":")[1]
            tickets_database.load_tk_in_database(source)


def getLastMsg(id_msg):
    payload = '{"query": "{getMessage (id:\\"'+id_msg+'\\"){type,text,filename,caption}}"}'
    json = send_payload(payload)
    if json is not None:
        if json['data']['getMessage'] is not None:
            source = (json['data']['getMessage'])
            return source
        else:
            source = []
            return source





#payload = {'phone_id':3663,'node2':"@Cyberlink",'node3':"",'node4':""}
#print(get_tickets(payload))