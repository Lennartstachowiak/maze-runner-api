from flask import jsonify
from app.models.maze.check_if_test import check_if_test
from app.models.maze.get_maze_algorithm_solution import (
    get_maze_algorithm_solution,
)
from app.models.maze.handle_adding_highscore import (
    handle_adding_maze_highscore,
)
from app.models.user.get_user import get_user_id


def get_maze_algorithm_solution_controller(request):
    algorithm_id = request.json["algorithmId"]
    maze_id = request.json["mazeId"]
    user_id = get_user_id(request)
    is_test = check_if_test(maze_id)
    solution = get_maze_algorithm_solution(maze_id, algorithm_id, is_test)

    is_no_test_and_no_error = not is_test and "solution" in solution and "visited" in solution and "score" in solution
    if is_no_test_and_no_error:
        handle_adding_maze_highscore(user_id, maze_id, algorithm_id, solution)
    return jsonify(solution)
