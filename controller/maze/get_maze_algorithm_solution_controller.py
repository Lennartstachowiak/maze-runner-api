from flask import jsonify
from db import models
from services.maze.get_maze_algorithm_solution import get_maze_algorithm_solution

Mazes = models.Mazes
Algorithms = models.Algorithms


def get_maze_algorithm_solution_controller(request):
    algorithm_id = request.json["algorithmId"]
    maze_id = request.json["mazeId"]

    solution = get_maze_algorithm_solution(maze_id, algorithm_id)
    return jsonify(solution)
