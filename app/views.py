# project/app/views.py

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import render_template, request, jsonify
from app import app
from .fetcher import get_data

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/data")
def data():
    return jsonify(get_data())


@app.route('/about')
def about():
    return render_template('about.html')
