from flask import request
from app.controller.user.login_controller import login_user_controller
from app.controller.user.logout_controller import logout_user_controller
from app.controller.user.register_user_controller import register_user_controller
from app.controller.user.get_user_controller import get_user_controller
from db import models
from os import environ
from dotenv import load_dotenv

load_dotenv()

User = models.Users
Algorithms = models.Algorithms
SessionAuth = models.SessionAuth


def register_user_routes(api):
    expected_referer = environ.get('ALLOW_ORIGIN')

    @api.before_request
    def validate_referer():
        if request.endpoint != "connect" and request.headers.get("Referer")+'*' != expected_referer:
            return {"error": "Invalid request origin"}, 403

    @api.route("/", methods=["GET"])
    def connect():
        return "connected"

    @ api.route("/v1/@me", methods=["GET"])
    def get_user_request():
        response = get_user_controller(request)
        return response

    @ api.route("/v1/register", methods=["POST"])
    def register_user_request():
        response = register_user_controller(request, api)
        return response

    @ api.route("/v1/login", methods=["POST"])
    def login_user_request():
        response = login_user_controller(request, api)
        return response

    @ api.route("/v1/logout", methods=["POST"])
    def logout_user_request():
        response = logout_user_controller(request)
        return response
