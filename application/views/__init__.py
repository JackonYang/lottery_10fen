# -*- Encoding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint('default', __name__, template_folder='templates')


@bp.route('/')
def live_win():
    return render_template('live.html')
