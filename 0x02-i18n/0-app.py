#!/usr/bin/python3
"""  basic Flask app  with single route """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display 0-index.html """
    return render_template('0-index.html')
