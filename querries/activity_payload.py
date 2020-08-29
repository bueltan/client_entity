from Connection_endpoint import send_payload
from querries import activity_database

def get_activity(session ,id):
    payload = '{"query": "{activityList (ticketsId:\\"'+id+'\\"){edges{node {id,ticketsId,messageId,timestamp,type}}}}"}'
    json = send_payload(payload)
    if json is not None:
        if json['data']['activityList']['edges'] != []:
            source = (json['data']['activityList']['edges'])
            print(source)
            activity_database.load_act_in_database(session, source)