from . import bp
from flask import render_template


@bp.route("/")
def index():
    return "This is Core-Index!"