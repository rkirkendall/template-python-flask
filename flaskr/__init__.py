"""Template app with a single /ping route, configured with MySQL."""

import os

from datetime import datetime

from flaskext.mysql import MySQL

from flask import (
    Flask, jsonify, request
)

from flask_cors import CORS

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    CORS(app)

    mysql = MySQL()
    mysql.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/ping')
    def ping():
        ping = request.args.get('ping')
        if ping == "":
            ping = 'To ping, or not to ping; that is the question.'
        return jsonify(
            ping=ping,
            received_at=datetime.utcnow(),
        )

    return app
