from flask import jsonify, request
from os import environ
from dotenv import load_dotenv

load_dotenv()


def register_validation(api):
    expected_origin = environ.get('ALLOW_ORIGIN')

    @api.before_request
    def validate_origin():
        origin = request.headers.get("Origin")
        if request.endpoint != "connect" and origin != expected_origin:
            return {"error": "Invalid request origin"}, 403

    @api.errorhandler(409)
    def conflict(error):
        return jsonify({"error": "Conflict"}), 409

    @api.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "Unauthorized"}), 401

    @api.errorhandler(400)
    def invalid_request(error):
        return jsonify({"error": "Invalid request"}), 400

    @api.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Internal server error"}), 500
