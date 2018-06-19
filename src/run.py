import flask
from api.models import Client, Dataset
from flask_restless import APIManager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


app = flask.Flask(__name__)
engine = create_engine('sqlite:////tmp/testdb.sqlite', convert_unicode=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mysession = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine


Base.metadata.create_all()

manager = APIManager(app, session=mysession)


manager.create_api(Client, methods=['GET', 'UPDATE', 'POST', 'PUT', 'DELETE'])
manager.create_api(Dataset, methods=['GET', 'UPDATE', 'POST', 'PUT', 'DELETE'])


app.run(debug=True, host='0.0.0.0', port=5000)