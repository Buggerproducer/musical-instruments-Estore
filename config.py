import os
basedir = os.path.abspath(os.path.dirname(__file__))

import leancloud
leancloud.init("gyg9pml06JYzbcyfiW9f0tUp-gzGzoHsz", "OiLNbwn0ivp1toeAJiHRAvhN")


class Config(object):
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask1'
    USERNAME = 'root'
    PASSWORD = '123456'
    SECRET_KEY = 'secret!'

    DB_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'MusiCrash.db')

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TERADOWN = True
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.db')
    # the path for the sqlite database


class ProductConfig(Config):
    """Generate the setting for production"""
    DEBUG = False


class TestConfig(Config):
    """generate the setting for test"""
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    "production": ProductConfig,
    'default': DevelopmentConfig,
    "testing": TestConfig,
}


