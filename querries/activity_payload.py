from Connection_endpoint import send_payload
from querries import activity_database


def get_activity(session, id, timestamp):
    payload = '{"query": "{activityList (ticketsId:\\"' + id + '\\", timestamp:\\"'+timestamp+'\\" ){edges{node {id,ticketsId,messageId,timestamp,type}}}}"}'
    json = send_payload(payload)
    print(payload)
    if json is not None:
        if json['data']['activityList']['edges'] != []:
            source = (json['data']['activityList']['edges'])
            activity_database.load_act_in_database(session, source)
