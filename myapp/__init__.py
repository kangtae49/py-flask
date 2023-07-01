from flask import Flask
from . import main
from . import sample

app = Flask(__name__)



app.register_blueprint(main.bp_main)
app.register_blueprint(sample.bp_sample)