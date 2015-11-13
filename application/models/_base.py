# -*- Encoding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask_redis import Redis

db = SQLAlchemy()
rd = Redis()
