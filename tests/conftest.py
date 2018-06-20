from creat_app import create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from api.models import Client, Dataset
import pytest


DB_URI = 'sqlite:////tmp/testdb.sqlite'


@pytest.fixture(scope='session')
def engine():
    return create_engine(DB_URI)


@pytest.yield_fixture(scope='session')
def tables(engine):
    Client.metadata.create_all(engine)
    Dataset.metadata.create_all(engine)
    yield
    Client.metadata.drop_all(engine)
    Dataset.metadata.drop_all(engine)


@pytest.yield_fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture
def app(dbsession):
    _app = create_app('test', session=dbsession)
    _app.debug = True
    testing_client = _app.test_client()

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
