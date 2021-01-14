import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'f3cfe9ed8fae309f02079dbf'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///healthcare'