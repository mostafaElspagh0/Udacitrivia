import os
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "trivia_dev"
database_username = os.getenv('DATABASE_USERNAME')
database_password = os.getenv('DATABASE_PASSWORD')
database_path = "postgres://{}:{}@{}/{}".format(database_username, database_password, 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def rollback_db():
    db.session.roll_back()


def close_db_session():
    db.session.close()
