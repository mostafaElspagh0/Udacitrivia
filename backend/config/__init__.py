from .database_uri import DatabaseUri

SQLALCHEMY_DATABASE_URI = str(DatabaseUri())

SQLALCHEMY_TRACK_MODIFICATIONS = False
