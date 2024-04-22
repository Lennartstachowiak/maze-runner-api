from flask import request
from app.controller.user.login_controller import login_user_controller
from app.controller.user.logout_controller import logout_user_controller
from app.controller.user.register_user_controller import register_user_controller
from app.controller.user.get_me_user_controller import get_me_user_controller
from app.controller.user.follow_user_controller import follow_user_controller
from app.controller.user.search_user_controller import search_user_controller
from app.controller.user.get_user_controller import get_user_controller
from db import models

User = models.Users
Algorithms = models.Algorithms
SessionAuth = models.SessionAuth


def register_user_routes(api):

    @api.route("/", methods=["GET"])
    def connect():
        return "connected"

    @ api.route("/v1/@me", methods=["GET"])
    def get_me_user_request():
        response = get_me_user_controller(request)
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

    @ api.route("/v1/follow_user", methods=["POST"])
    def follow_user_request():
        response = follow_user_controller(request)
        return response

    @ api.route("/v1/search_user", methods=["POST"])
    def search_user():
        response = search_user_controller(request)
        return response

    @ api.route("/v1/get_user", methods=["GET"])
    def get_user():
        response = get_user_controller(request)
        return response
