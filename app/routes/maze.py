from flask import jsonify, request
from app.controller.maze.delete_maze_controller import delete_maze_controller
from app.controller.maze.generate_maze_controller import generate_maze_controller
from app.controller.maze.get_maze_algorithm_solution_controller import get_maze_algorithm_solution_controller
from app.controller.maze.get_mazes_controller import get_mazes_contoller
from app.controller.maze.get_my_mazes_controller import get_my_mazes_controller
from app.controller.maze.get_single_maze_controller import get_single_maze_controller
from db import models

User = models.Users
Mazes = models.Mazes
Highscores = models.Highscores
Algorithms = models.Algorithms


def register_maze_routes(api):

    @ api.route("/v1/get_mazes", methods=["GET"])
    def get_mazes_request():
        response = get_mazes_contoller()
        return response

    @ api.route("/v1/get_my_mazes", methods=["GET"])
    def get_my_maze_request():
        response = get_my_mazes_controller(request)
        return response

    @api.route("/v1/get_single_maze", methods=["GET"])
    def get_single_maze_request():
        response = get_single_maze_controller(request)
        return response

    @api.route("/v1/get_maze_algorithm_solution", methods=["POST"])
    def get_maze_algorithm_solution_request():
        response = get_maze_algorithm_solution_controller(request)
        return response

    @api.route("/v1/generate_maze", methods=["POST"])
    def generate_maze_request():
        response = generate_maze_controller(request)
        return response

    @api.route("/v1/delete_maze", methods=["DELETE"])
    def delete_maze_request():
        response = delete_maze_controller(request)
        return response
