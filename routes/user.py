from flask import request
from controller.user.login import login_user
from controller.user.logout import logout_user
from controller.user.register import register_user
from controller.user.me import me
from db import models

User = models.User
Algorithms = models.Algorithms
SessionAuth = models.SessionAuth


def register_user_routes(api):

    @api.route("/", methods=["GET"])
    def connect():
        return "connected"

    @ api.route("/v1/@me", methods=["GET"])
    def get_current_user():
        response = me(request)
        return response

    @ api.route("/v1/register", methods=["POST"])
    def register():
        response = register_user(request, api)
        return response

    @ api.route("/v1/login", methods=["POST"])
    def login():
        response = login_user(request, api)
        return response

    @ api.route("/v1/logout", methods=["POST"])
    def logout():
        response = logout_user(request)
        return response
