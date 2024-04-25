from flask import request
from app.controller.user.login_controller import login_user_controller
from app.controller.user.logout_controller import logout_user_controller
from app.controller.user.register_user_controller import (
    register_user_controller,
)
from app.controller.user.get_me_user_controller import get_me_user_controller
from app.controller.user.follow_user_controller import follow_user_controller
from app.controller.user.user_following_controller import (
    user_following_controller,
)
from app.controller.user.user_followers_controller import (
    user_followers_controller,
)
from app.controller.user.search_user_controller import search_user_controller
from app.controller.user.get_user_controller import get_user_controller
from db import models

User = models.Users
Algorithms = models.Algorithms
SessionAuth = models.SessionAuth


def register_user_routes(api):

    @api.route("/", methods=["GET"])
    def connect():
        """
        An endpoint to test the connectivity to the API.

        Returns:
            A simple string message indicating the connection status.
        """
        return "connected"

    @api.route("/v1/@me", methods=["GET"])
    def get_me_user_request():
        """
        Retrieve the profile information of the currently authenticated user.

        Requires an active session.

        Returns:
            A Flask response object containing the JSON representation of the current user's profile information,
            with an HTTP status code of 200 (OK) if the request is authorized, or 401 (Unauthorized) if not.
        """
        response = get_me_user_controller(request)
        return response

    @api.route("/v1/register", methods=["POST"])
    def register_user_request():
        """
        Register a new user with the provided credentials in the request payload.

        The request payload must contain `username`, `email`, `password` and `repeatedPassword` fields.

        Returns:
            A Flask response object containing the JSON representation of the newly created user profile,
            with an HTTP status code of 201 (Created). If the user cannot be created,
            returns a 400 (Bad Request) status code.
        """
        response = register_user_controller(request, api)
        return response

    @api.route("/v1/login", methods=["POST"])
    def login_user_request():
        """
        Authenticate a user with the provided credentials in the request payload.

        The request payload must contain `email` and `password` fields.

        Returns:
            A Flask response object containing the JSON representation of the authenticated user's session information,
            with an HTTP status code of 200 (OK) if the login is successful, or 401 (Unauthorized) if not.
        """
        response = login_user_controller(request, api)
        return response

    @api.route("/v1/logout", methods=["POST"])
    def logout_user_request():
        """
        Log out the currently authenticated user.

        Requires an active session.

        Returns:
            A Flask response object with an HTTP status code of 200 (OK) if the logout is successful,
            or 401 (Unauthorized) if there is no active session to terminate.
        """
        response = logout_user_controller(request)
        return response

    @api.route("/v1/follow_user", methods=["POST"])
    def follow_user_request():
        """
        Follow another user's profile as the currently authenticated user.

        The request payload must contain the `userIdFollowed` of the user to follow and an active user session.

        Returns:
            A Flask response object with an HTTP status code of 200 (OK) if the follow request is successful,
            or 401 (Unauthorized) if the current user is not authenticated,
            or 404 (Not Found) if the target user does not exist.
        """
        response = follow_user_controller(request)
        return response

    @api.route("/v1/user_following", methods=["GET"])
    def user_following_request():
        """
        Retrieve the list of users that the currently authenticated user is following.

        Requires an active user session.

        Returns:
            A Flask response object containing the JSON list of followed users,
            with an HTTP status code of 200 (OK) if the request is authorized, or 401 (Unauthorized) if not.
        """
        response = user_following_controller(request)
        return response

    @api.route("/v1/user_followers", methods=["GET"])
    def user_followers_request():
        """
        Retrieve the list of users that are following the currently authenticated user.

        Requires an active user session.

        Returns:
            A Flask response object containing the JSON list of followers,
            with an HTTP status code of 200 (OK) if the request is authorized, or 401 (Unauthorized) if not.
        """
        response = user_followers_controller(request)
        return response

    @api.route("/v1/search_user", methods=["POST"])
    def search_user():
        """
        Search for users by a given query contained in the request payload.

        The request payload must contain a `email` field.

        Returns:
            A Flask response object containing the JSON list of users matching the search query,
            with an HTTP status code of 200 (OK), or 400 (Bad Request) if the search query is invalid.
        """
        response = search_user_controller(request)
        return response

    @api.route("/v1/get_user", methods=["GET"])
    def get_user():
        """
        Retrieve a specific user's profile information by user ID provided as a URL parameter.

        Args:
            id (str): Unique identifier for the user.

        Returns:
            A Flask response object containing the JSON representation of the user's profile,
            with an HTTP status code of 200 (OK) if the user is found, or 404 (Not Found) if the user does not exist.
        """
        response = get_user_controller(request)
        return response
