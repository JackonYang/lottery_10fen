# -*- Encoding: utf-8 -*-
from flask.ext.script import Manager
from application import make_app
from application.models import db

PORT = 8000  # debug mode

app = make_app()
manager = Manager(app)


@manager.command
def run():
    """Run server."""
    app.run(host='0.0.0.0', port=PORT)


@manager.command
def create_db():
    """Create database."""
    print 'creating db...'
    print db.engine.url
    db.create_all()


if __name__ == "__main__":
    manager.run()
