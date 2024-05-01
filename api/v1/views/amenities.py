#!/usr/bin/python3
"""
route for handling Amenity objects and operations
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.amenity import Amenity

@app_views.route("/amenity", methods=["GET"], strict_slashes=False)
def all_amenity():
    """
    Retrieves all Amenities and return jsons
    """
    amenity_list = []
    amenity_obj = storage.all("Amenity")
    for obj in amenity_obj.values():
        amenity_list.append(obj.to_json())

    return jsonify(amenity_list)

@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def create_amenity():
    """
    create amenity route
    :return: newly created amenity obj
    """
    am_json = request.get_json(silent=True)
    if am_json is None:
        abort(400, 'Not a JSON')
    if "name" not in am_json:
        abort(400, "Missing name")

    new_amenity = Amenity(**amenity_json)
    new_amenity.save()
    resp = jsonify(new_am.to_json())
    resp.status_code = 201

    return resp

@app_views.route("/amenities/<amenity_id>",  methods=["GET"],
                 strict_slashes=False)
def amenity_by_id(amenity_id):
    """
    gets a specific Amenity object by ID 
    """
    fetched_obj = storage.get("Amenity", str(amenity_id))

    if fetched_obj is None:
        abort(404)

    return jsonify(fetched_obj.to_json())

