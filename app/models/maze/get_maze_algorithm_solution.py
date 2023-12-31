import json
from app.models.maze.maze import Maze, MazeSolver
from db import models
from db.db import db

Mazes = models.Mazes
Algorithms = models.Algorithms


def get_maze_algorithm_solution(maze_id, algorithm_id, is_test):
    # Get Maze
    maze_object = Mazes.query.filter_by(id=maze_id).first()

    maze = Maze(maze_object.height, maze_object.width,
                json.loads(maze_object.structure))

    solver = MazeSolver(maze=maze)

    # Get Algorithm
    algorithm_object = Algorithms.query.filter_by(id=algorithm_id).first()
    algorithm_code = algorithm_object.code

    # Solve maze with algorithm
    solver.solve(algorithm_code)
    if solver.error:
        error_message = {"error": solver.error}
        # Update is working
        algorithm_object.isWorking = False
        db.session.commit()
        return error_message
    elif is_test:
        # Update is working
        algorithm_object.isWorking = True
        db.session.commit()
    check = solver.check_solution()
    if not check[0]:
        return check
    solver.calculateScore()

    solver_result = {"solution": solver.solution,
                     "visited": solver.visited,
                     "score": solver.score}
    return solver_result
