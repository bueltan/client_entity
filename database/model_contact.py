from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean


class ModelContact(Base):
    """Contact model."""
    __tablename__ = 'Contact'
    id = Column('id', Integer, primary_key=True, doc="Id of the Contact.")
    id_account = Column('id_account', ForeignKey('Account.id'), doc="Id of the account")
    type_contact = Column('type_contact', String(10))
    name_contact = Column('name_contact', String(30))
    image_contact = Column('image_contact', String(200))
    node2 = Column('node2', String(15), doc="")
    node3 = Column('node3', String(15), doc="")
    node4 = Column('node4', String(15), doc="")
    phone = Column('phone', String(15), nullable=False, doc="phone number.")
