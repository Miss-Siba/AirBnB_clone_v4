#!/usr/bin/python3
"""
index
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return a JSON response indicating status OK."""
    data = {
            "status":"OK"
            }
    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    stats of all objects route
    :return: json of all objects
    """
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    resp = jsonify(data)
    resp.status_code = 200

    return resp
