from flask import jsonify
from app.models.maze.get_maze_algorithm_solution import get_maze_algorithm_solution


def get_maze_algorithm_solution_controller(request):
    algorithm_id = request.json["algorithmId"]
    maze_id = request.json["mazeId"]

    solution = get_maze_algorithm_solution(maze_id, algorithm_id)
    return jsonify(solution)
