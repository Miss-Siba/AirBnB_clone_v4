#!/usr/bin/python3
import os
from flask import Flask
import storage from models
import app_views from api.v1.views

app = Flask(__name__)

# Register blueprint for API views
app.register_blueprint(app_views)

# Method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the storage session after each request."""
    storage.close()

if __name__ == '__main__':
    # Set host and port based on environment variables or defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
