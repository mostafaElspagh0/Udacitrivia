from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    setup_migration(app, db)


def setup_migration(app, db):
    migration = Migrate(app, db)


def rollback_db():
    db.session.roll_back()


def close_db_session():
    db.session.close()
