# coding: utf-8
from .default import Config


class ProductionConfig(Config):
    # App config
    SECRET_KEY = '\xb5\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}'

    # Site domain
    SITE_DOMAIN = '10fen.safebang.org'

    # Db config
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/lottery'
