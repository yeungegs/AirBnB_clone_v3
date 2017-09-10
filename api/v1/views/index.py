#!/usr/bin/python3
"""
App views for AirBnB_clone_v3
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ returns status """
    status = {"status": "OK"}
    return jsonify(status)
