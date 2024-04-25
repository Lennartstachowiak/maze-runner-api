from flask import jsonify
from app.models.algorithm.get_single_algorithm import get_single_algorithm
from app.models.maze.check_if_test import check_if_test
from app.models.maze.get_maze_algorithm_solution import (
    get_maze_algorithm_solution,
)
from app.models.maze.get_single_maze import get_single_maze
from app.models.maze.handle_adding_highscore import (
    handle_adding_maze_highscore,
)
from app.models.user.get_user import get_user_id
from db.db import db


def get_maze_algorithm_solution_controller(request):
    algorithm_id = request.json["algorithmId"]
    maze_id = request.json["mazeId"]
    user_id = get_user_id(request)
    is_test = check_if_test(maze_id)
    maze = get_single_maze(maze_id)
    algorithm = get_single_algorithm(algorithm_id)
    solution = get_maze_algorithm_solution(maze, algorithm)
    if solution.error:
        # Update "is working"
        algorithm.is_working = False
        db.session.commit()
    elif is_test:
        # Update "is working"
        algorithm.is_working = True
        db.session.commit()

    is_no_test_and_no_error = not is_test and "solution" in solution and "visited" in solution and "score" in solution
    if is_no_test_and_no_error:
        handle_adding_maze_highscore(user_id, maze_id, algorithm_id, solution)
    return jsonify(solution)
