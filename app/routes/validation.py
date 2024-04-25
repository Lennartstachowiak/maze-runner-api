from flask import jsonify, request
from os import environ
from dotenv import load_dotenv

load_dotenv()


def register_validation(api):
    """
    Register validation handlers for the Flask API to ensure that only requests
    from the expected origin are allowed and to provide standard JSON error responses.

    Args:
        api (Flask): The Flask application object or Blueprint to which the validation handlers will be registered.
    """
    expected_origin = environ.get("ALLOW_ORIGIN")

    @api.before_request
    def validate_origin():
        """
        Before request handler that validates the 'Origin' header of incoming requests.

        If the 'Origin' does not match the expected origin, a JSON error response is returned
        with a 403 Forbidden status code.

        Returns:
            A tuple of a JSON error response and the HTTP status code if the origin is invalid.
        """
        origin = request.headers.get("Origin")
        if request.endpoint != "connect" and origin != expected_origin:
            return {"error": "Invalid request origin"}, 403

    @api.errorhandler(409)
    def conflict(error):
        """
        Error handler for 409 Conflict HTTP status code.

        Args:
            error: The error object provided by Flask.

        Returns:
            A Flask response object containing the JSON error message and the HTTP status code 409.
        """
        return jsonify({"error": "Conflict"}), 409

    @api.errorhandler(401)
    def unauthorized(error):
        """
        Error handler for 401 Unauthorized HTTP status code.

        Args:
            error: The error object provided by Flask.

        Returns:
            A Flask response object containing the JSON error message and the HTTP status code 401.
        """
        return jsonify({"error": "Unauthorized"}), 401

    @api.errorhandler(400)
    def invalid_request(error):
        """
        Error handler for 400 Bad Request HTTP status code.

        Args:
            error: The error object provided by Flask.

        Returns:
            A Flask response object containing the JSON error message and the HTTP status code 400.
        """
        return jsonify({"error": "Invalid request"}), 400

    @api.errorhandler(500)
    def internal_server_error(error):
        """
        Error handler for 500 Internal Server Error HTTP status code.

        Args:
            error: The error object provided by Flask.

        Returns:
            A Flask response object containing the JSON error message and the HTTP status code 500.
        """
        return jsonify({"error": "Internal server error"}), 500
