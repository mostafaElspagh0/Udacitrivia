import os
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


def rollback_db():
    db.session.roll_back()


def close_db_session():
    db.session.close()
