from flask import request
from app.controller.algorithm.add_new_algorithm_controller import (
    add_new_algorithm_controller,
)
from app.controller.algorithm.delete_algorithm_controller import (
    delete_algorithm_controller,
)
from app.controller.algorithm.get_algorithms_controller import (
    get_algorithms_controller,
)
from app.controller.algorithm.get_single_algorithm_controller import (
    get_single_algorithm_controller,
)
from app.controller.algorithm.rename_algorithm_controller import (
    rename_algorithm_controller,
)
from app.controller.algorithm.save_algorithm_controller import (
    save_algorithm_controller,
)
from db import models

Mazes = models.Mazes
Algorithms = models.Algorithms


def register_algorithm_routes(api):

    @api.route("/v1/get_algorithms", methods=["GET"])
    def get_algorithms_request():
        """
        Retrieve a all algorithms of a user from the database by user session and return the algorithm data as JSON.

        Returns:
            A Flask response object containing the JSON representation of all user algorithms,
            with an HTTP status code of 200 (OK) if the user is found, or 401, "Unauthorized"
            if the user or the session does not exist.
        """
        response = get_algorithms_controller(request)
        return response

    @api.route("/v1/get_single_algorithm", methods=["GET"])
    def get_single_algorithm_request():
        """
        Retrieve a single all algorithm from the database by its id and return the algorithm data as JSON.

        Args:
            id (string): Unique identifier for the algorithm

        Returns:
            A Flask response object containing the JSON representation of user algorithms,
            with an HTTP status code of 200 (OK).
        """
        response = get_single_algorithm_controller(request)
        return response

    @api.route("/v1/save_algorithm_changes", methods=["PATCH"])
    def save_algorithm_request():
        """
        Saves changes for a user algorithm in the database. User will be authenticated by the session cookie for access.

        Args:
            algorithmId (string): Unique identifier
            newCode (string): Text which represents the updated code

        Returns:
            A Flask response object containing the JSON representation of all user algorithms,
            with an HTTP status code of 200 (OK), or 401, "Unauthorized"
            if the user doesn't exist or is not authenticated or the session does not exist.
        """
        response = save_algorithm_controller(request)
        return response

    @api.route("/v1/add_new_algorithm", methods=["POST"])
    def add_new_algorithm_request():
        """
        Adds a new algorithm into the database. User will be authenticated by the session cookie for access.

        Returns:
            A Flask response object containing the JSON representation of all user algorithms,
            with an HTTP status code of 201, or 401, "Unauthorized"
            if the user doesn't exist or is not authenticated or the session does not exist.
        """
        response = add_new_algorithm_controller(request)
        return response

    @api.route("/v1/delete_algorithm", methods=["DELETE"])
    def delete_algorithm_request():
        """
        Deletes a user algorithm from the database. User will be authenticated by the session cookie for access.

        Args:
            algorithmId (string): Unique identifier

        Returns:
            A Flask response object containing the JSON representation of all user algorithms,
            with an HTTP status code of 204, or 401, "Unauthorized"
            if the user doesn't exist or is not authenticated or the session does not exist.
        """
        response = delete_algorithm_controller(request)
        return response

    @api.route("/v1/rename_algorithm", methods=["PATCH"])
    def rename_algorithm_request():
        """
        Renames a user algorithm in the database. User will be authenticated by the session cookie for access.

        Args:
            algorithmId (string): Unique identifier
            newName (string): Text which represents the name

        Returns:
            A Flask response object containing the JSON representation of all user algorithms,
            with an HTTP status code of 200 (OK), or 401, "Unauthorized"
            if the user doesn't exist or is not authenticated or the session does not exist.
        """
        response = rename_algorithm_controller(request)
        return response
