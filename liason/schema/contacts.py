"""
liason.schema.contacts
~~~~~~~~~~~~~~~~~~~~~~
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contacts(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
