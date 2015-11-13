# -*- coding:utf-8 -*-
from os.path import dirname, abspath


class Config(object):
    """配置基类"""
    # Flask app config
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\xb5\xb3}#\xb7A\xcac\x9d0\xb6\xb8+\xe9)\xf0}'

    # Root path of project
    PROJECT_PATH = abspath(dirname(dirname(__file__)))

    # Db config
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/lottery'

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 6
