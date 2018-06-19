from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from api.data_types import MutableDict, MetadataType

Base = declarative_base()


class Client(Base):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ip_address = Column(String(15), nullable=False)


class Dataset(Base):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    meta_data = Column(MutableDict.as_mutable(MetadataType))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
