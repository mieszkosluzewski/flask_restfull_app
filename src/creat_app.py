"""
create_app factory.
"""
from api.models import Client, Dataset, engine
from flask import Flask
from flask_restless import APIManager
from flask_restless.views import ValidationError
from sqlalchemy.orm import scoped_session, sessionmaker

_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mysession = scoped_session(_session)


def create_app(name_handler, session=mysession):
    """
    Application factory

    :param name_handler: name of the application.
    :param db_uri:
    """
    app = Flask(name_handler)
    manager = APIManager(app, session=session)

    manager.create_api(
        Client, methods=['GET', 'UPDATE', 'POST', 'PUT', 'DELETE'], validation_exceptions=[ValidationError]
    )
    manager.create_api(Dataset, methods=['GET', 'UPDATE', 'POST', 'PUT', 'DELETE'])

    return app
