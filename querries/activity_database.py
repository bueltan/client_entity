from database.model_activity import ModelActivity
from querries.message_payload import get_msg


def load_act_in_database(session, data):
    for act in data:
        act = act['node']
        id = act['id']
        local_act = session.query(ModelActivity).filter_by(id=id).first()
        if not local_act:
            put_act_data(session, act)
            ticketsId = act['ticketsId']
            timestamp = act['timestamp']
            get_msg(session, act['messageId'], ticketsId, timestamp)


def put_act_data(session, data):
    activity = ModelActivity(**data)
    session.add(activity)