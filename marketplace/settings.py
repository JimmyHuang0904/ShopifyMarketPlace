import os


class BaseConfig():
    SECRET_KEY = 'REPLACE ME'
    DEBUG = True

# TODO: Add LDAP config. We assume we could use LDAP authentication because account look up for login and processing
# is used more than creation (LDAP will be able to handle more reads than write operation)

# Configuration for Production


class ProdConfig(BaseConfig):
    # Internal configuration
    FLASK_ENV = 'production'
    ENV = 'production'
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    # Internal configuration values
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
