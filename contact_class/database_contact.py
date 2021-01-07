from database import base
from database.model_contact import ModelContact
session = base.Session()

def load_contact_in_database(data, last_sync):
    print("data contacts for load in data base local : ", data)
    tickets = ModelTickets(**tk)
    session.merge(tickets)
    session.commit()
    session.close()
