from flask import request
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
