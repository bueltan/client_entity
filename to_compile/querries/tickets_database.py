from database import base
from database.model_tickets import ModelTickets
from querries.activity_payload import get_activity

session = base.Session()


def load_tk_in_database(data):
    for tk in data:
        tk = tk['node']
        id = str(tk['id'])
        id_last_msg = tk['last_id_msg']
        local_tk = session.query(ModelTickets).filter_by(id=id).first()
        if local_tk:
            if local_tk.last_id_msg != id_last_msg:
                merge_data(tk, local_tk)
                get_activity(session, id,str(local_tk.last_id_msg))
        else:
            put_tk_data(tk)
            get_activity(session, id,'0')

    session.commit()
    session.close()


def merge_data(tk, local_tk):
    last_id_msg = tk['last_id_msg']
    timestamp = tk['timestamp']
    local_tk.last_id_msg = last_id_msg
    local_tk.timestamp = timestamp
    session.merge(local_tk)


def put_tk_data(data):
    tickets = ModelTickets(**data)
    session.add(tickets)
