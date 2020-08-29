from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .model_messages import ModelMessages


class ModelActivity(Base):
    """Activity model."""

    __tablename__ = 'Activity'

    id = Column('id', String(30), primary_key=True, doc="Id of the activity.")
    ticketsId = Column('tickets_id', ForeignKey('Tickets.id'), doc="Id of the tickets")
    messageId = Column('message_id', ForeignKey('Messages.id'), doc="Id of the message")
    type = Column('type', String(30), doc="type of activity")
    timestamp = Column('timestamp', Integer, doc="Record timestamp.")

    listMessage = relationship(ModelMessages, backref="Activity")
