from connection_endpoint import send_payload
from querries import tickets_database
import base64


def get_subscritions(accout_name_id):
    payload = '{"query": "{subscriptionList (idNameAccount:\\"' + accout_name_id + '\\")\
               {edges {node {source,id}}}}"}'
    json = send_payload(payload)
    if json is not None:
        if json['data']['subscriptionList'] is not None:
            source = (json['data']['subscriptionList']['edges'])
            return source
        else:
            source = []
            return source




# payload = {'phone_id':3663,'node2':"@Cyberlink",'node3':"",'node4':""}
# print(get_tickets(payload))
