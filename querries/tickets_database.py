from database import base
from database.model_tickets import ModelTickets
import base64
from querries.message_payload import get_message
session = base.Session()

def load_tk_in_database(data, last_sync):
    print("data tk for load in data base local : ", data)
    for tk in data:
        tk = tk['node']
        id = tk['id']
        tk['id'] = (base64.standard_b64decode(id)).decode("utf-8").split(":")[1]
        get_message(session, tk['id'], last_sync)
        tickets = ModelTickets(**tk)
        session.merge(tickets)
    session.commit()
    session.close()
