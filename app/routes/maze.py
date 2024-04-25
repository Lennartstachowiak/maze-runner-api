from flask import request
from app.controller.maze.delete_maze_controller import delete_maze_controller
from app.controller.maze.generate_maze_controller import (
    generate_maze_controller,
)
from app.controller.maze.get_maze_algorithm_solution_controller import (
    get_maze_algorithm_solution_controller,
)
from app.controller.maze.get_mazes_controller import get_mazes_contoller
from app.controller.maze.get_my_mazes_controller import get_my_mazes_controller
from app.controller.maze.get_user_mazes_controller import (
    get_user_mazes_controller,
)
from app.controller.maze.get_single_maze_controller import (
    get_single_maze_controller,
)
from app.controller.maze.follow_maze_controller import follow_maze_controller
from app.controller.maze.get_followed_mazes_controller import (
    get_followed_mazes_controller,
)
from db import models

User = models.Users
Mazes = models.Mazes
Highscores = models.Highscores
Algorithms = models.Algorithms


def register_maze_routes(api):

    @api.route("/v1/get_mazes", methods=["GET"])
    def get_mazes_request():
        """
        Retrieve a all official mazes from the database and returns the maze data as JSON.

        Returns:
            A Flask response object containing the JSON representation of all mazes,
            with an HTTP status code of 200 (OK).
        """
        response = get_mazes_contoller()
        return response

    @api.route("/v1/get_my_mazes", methods=["GET"])
    def get_my_maze_request():
        """
        Retrieve a all mazes of a user from the database by user session and return the maze data as JSON.

        Returns:
            A Flask response object containing the JSON representation of all user mazes,
            with an HTTP status code of 200 (OK), or 401, "Unauthorized"
            if the user or the session does not exist.
        """
        response = get_my_mazes_controller(request)
        return response

    @api.route("/v1/get_user_mazes", methods=["GET"])
    def get_user_maze_request():
        """
        Retrieve a all mazes of a specific other user from the database by user id and return the maze data as JSON.

        Args:
            id (string): Unique identifier for the user

        Returns:
            A Flask response object containing the JSON representation of all user mazes,
            with an HTTP status code of 200 (OK), or 401, "Unauthorized"
            if the user.
        """
        response = get_user_mazes_controller(request)
        return response

    @api.route("/v1/get_single_maze", methods=["GET"])
    def get_single_maze_request():
        """
        Retrieve a specific maze from the database by user id and return the maze data as JSON.

        Args:
            id (string): Unique identifier for the maze

        Returns:
            A Flask response object containing the JSON representation of the maze,
            with an HTTP status code of 200 (OK).
        """
        response = get_single_maze_controller(request)
        return response

    @api.route("/v1/get_maze_algorithm_solution", methods=["POST"])
    def get_maze_algorithm_solution_request():
        """
        Retrieve the solution of a maze by maze id and algorithm if and return the solution data as JSON.

        Args:
            algorithmId (string): Unique identifier for the algorithm
            mazeId (string): Unique identifier for the maze

        Returns:
            A Flask response object containing the JSON representation of the solution,
            with an HTTP status code of 200 (OK).

        Response JSON Object:
            - solution (dict): The solution path.
            - visited (dict): The visited cell path.
            - score (int): The score.
            - check (string): Reason chech failed.
            - error (str): An error message.
        """
        response = get_maze_algorithm_solution_controller(request)
        return response

    @api.route("/v1/generate_maze", methods=["POST"])
    def generate_maze_request():
        """
        Retrieve the solution of a maze by maze id and algorithm if and return the solution data as JSON.

        Args:
            mazeName (string): The name of the generated maze
            mazeSize (int): The size of the generated maze
            generateType (enum): The generation type how to generate the maze

        Returns:
            A Flask response object containing the JSON representation of the solution,
            with an HTTP status code of 200 (OK), or with 409, "Conflict" if maze generation failed.
        """
        response = generate_maze_controller(request)
        return response

    @api.route("/v1/delete_maze", methods=["DELETE"])
    def delete_maze_request():
        """
        Deletes a specific maze from a user from the database by maze id and user session for authentication.

        Args:
            mazeId (string): Unique identifier for the maze

        Returns:
            A Flask response object containing an HTTP status code of 204 (OK) if the user is found,
            or 401, "Unauthorized" if the user or the session does not exist.
        """
        response = delete_maze_controller(request)
        return response

    @api.route("/v1/follow_maze", methods=["POST"])
    def follow_maze_request():
        """
        A user follows a specific maze and connection will be added to database. User authenticates by session.

        Args:
            mazeId (string): Unique identifier of the maze

        Returns:
            A Flask response object containing the JSON list representation of the solution,
            with an HTTP status code of 200 (OK), or with 409, "Conflict" if maze generation failed.
        """
        response = follow_maze_controller(request)
        return response

    @api.route("/v1/get_followed_maze", methods=["GET"])
    def get_followed_maze_request():
        """
        Retrieve a all followed mazes of a user from the database by user session and return the maze data as JSON.

        Returns:
            A Flask response object containing the JSON list representation of all user mazes,
            with an HTTP status code of 200 (OK), or 401, "Unauthorized"
            if the user or the session does not exist.
        """
        response = get_followed_mazes_controller(request)
        return response
