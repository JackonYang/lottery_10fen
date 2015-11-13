# -*- coding:utf-8 -*-
from .default import Config


class DevelopmentConfig(Config):
    # App config
    DEBUG = True

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/db.sqlite3'.format(Config.PROJECT_PATH)
