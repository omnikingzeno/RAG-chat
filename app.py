from flask import Flask
from routes.api import api_routes


def create_app():
    """
    Create and configure Flask application
    """
    app = Flask(__name__)

    # Registering blueprints
    app.register_blueprint(api_routes, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
