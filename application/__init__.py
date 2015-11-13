# -*- Encoding: utf-8 -*-
from flask import Flask
from models import db, rd  # sql and redis

# hooks
from flask import g, render_template
from flask_restful import Api

# add project path to sys path
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(abspath(__file__))))

from config import load_config


def make_app():
    app = Flask(__name__)
    config = load_config()
    app.config.from_object(config)

    rd.init_app(app)
    db.init_app(app)
    registe_routes(app)
    registe_api(app)
    registe_hooks(app)
    registe_error_handler(app)
    return app


def registe_api(app):
    """Register api."""
    import resources

    api = Api(app)
    api.add_resource(resources.LiveWin, '/api/live-win/<int:count>')


def registe_routes(app):
    """Register routes."""
    import views
    app.register_blueprint(views.bp, url_prefix='/')


def registe_hooks(app):
    """Register hooks."""

    @app.before_request
    def before_request():
        pass
        # from models import get_status_info
        # g.status_time = get_status_info()

    @app.after_request
    def after_request(response):
        return response


def registe_error_handler(app):
    """registe pages for http error"""

    @app.errorhandler(403)
    def page_403(error):
        return render_template('error/403.html'), 403

    @app.errorhandler(404)
    def page_404(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def page_500(error):
        return render_template('error/500.html'), 500
