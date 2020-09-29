import base64

from database.model_messages import ModelMessages
from database.base import Session

sessionQ = Session()


def load_msg_in_database(session, data):
    for msg in data:
        msg = msg['node']
        id = msg['id']
        msg['id'] = (base64.standard_b64decode(id)).decode("utf-8").split(":")[1]
        message = ModelMessages(**msg)
        session.merge(message)


def get_msg_local_db(ticketsId):
    msg = sessionQ.query(ModelMessages).filter_by(ticketsId=ticketsId)
    sessionQ.close()
    return msg


def get_oneMsg_local_db(idMessage):
    msg = sessionQ.query(ModelMessages).filter_by(id=idMessage).first()
    sessionQ.close()
    return msg
