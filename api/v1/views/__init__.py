#!/usr/bin/python3
from flask import Blueprint


# Create a Blueprint instance with the URL prefix /api/v1
app_views = Blueprint('/api/v1', __name__, url_prefix='/api/v1')

# Wildcard import of everything
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.users import *
from api.v1.views.places_amenities import *
