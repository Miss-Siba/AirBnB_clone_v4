#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register blueprint for API views
app.register_blueprint(app_views)

# Method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the storage session after each request."""
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)

if __name__ == '__main__':
    # Set host and port based on environment variables or defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
