from database.model_messages import ModelMessages
from database.base import Session

sessionQ = Session()


def load_msg_in_database(session, data):
    message = ModelMessages(**data)
    session.add(message)


def get_msg_local_db(ticketsId):
    msg = sessionQ.query(ModelMessages).filter_by(ticketsId=ticketsId)
    sessionQ.close()
    return msg


def get_oneMsg_local_db(idMessage):
    msg = sessionQ.query(ModelMessages).filter_by(id=idMessage).first()
    sessionQ.close()
    return msg
