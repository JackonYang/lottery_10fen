# -*- Encoding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint('default', __name__, template_folder='templates')

@bp.route('/')
def default_home():
    return render_template('default/home.html')
