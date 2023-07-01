from flask import Blueprint

bp_sample = Blueprint("sample", __name__, url_prefix="/sample")

@bp_sample.route("/get_sample")
def get_sample():
    return "get sample"