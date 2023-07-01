from flask import Blueprint, render_template

bp_main = Blueprint("main", __name__, url_prefix="/")

@bp_main.route("/")
def root():
    return "root"

@bp_main.route("/hello")
def hello():
    return render_template('hello.html')
