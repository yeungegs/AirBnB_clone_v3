#!/usr/bin/python3
"""
View for States that handles all RESTful API actions
"""

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False)
def states_all():
    """ returns list of all State objects """
    states_all = []
    states = storage.all("State").values()
    for state in states:
        states_all.append(state.to_json())
    return jsonify(states_all)
