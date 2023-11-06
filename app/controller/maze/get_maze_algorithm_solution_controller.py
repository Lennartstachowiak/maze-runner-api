from flask import jsonify
from app.controller.maze.add_maze_highscore import add_maze_highscore
from app.models.maze.get_maze_algorithm_solution import get_maze_algorithm_solution
from app.models.user.get_user import get_user_id


def get_maze_algorithm_solution_controller(request):
    algorithm_id = request.json["algorithmId"]
    maze_id = request.json["mazeId"]
    user_id = get_user_id(request)

    solution = get_maze_algorithm_solution(maze_id, algorithm_id)
    add_maze_highscore(user_id, maze_id, algorithm_id, solution)
    return jsonify(solution)
