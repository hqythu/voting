"""
flask config file
"""

import os
from modulefinder import importlib

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Base config class
    """

    SECRET_KEY = \
        os.environ.get('SECRET_KEY', 'ngJ4FvdqjEm9cGLutoQMjsbEFbigcuVd')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    Development config class, same to Config
    """
    pass


class ProductionConfig(Config):
    """
    Production config class, rewrite attribute of basic config.
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root@database:3306'


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}

importlib.import_module('config_local')
