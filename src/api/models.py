"""
Models for application (including simple validation and database initialization.
"""

import re
from flask_restless.views import ValidationError
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship, validates
from sqlalchemy import create_engine

from api.data_types import MutableDict, MetadataType

Base = declarative_base()
IP_PATTERN = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')


class Client(Base):
    """Model for client."""

    @declared_attr
    def __tablename__(cls):

        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ip_address = Column(String(15), nullable=False)

    @validates('ip_address')
    def validate_ip_address(self, key, ip_address):
        """
        Validator for IP address.

        For now only IPv4 was supported.

        :return: address
        :raises: ValidationError
        """
        if not IP_PATTERN.match(ip_address):
            raise ValidationError
        return ip_address


class Dataset(Base):
    """Model for dataset."""
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    filename = Column(String(255))
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    meta_data = Column(MutableDict.as_mutable(MetadataType))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
