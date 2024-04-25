import json
from app.models.maze.maze import Maze, MazeSolver


def get_maze_algorithm_solution(maze_object, algorithm_object):
    maze = Maze(
        maze_object.height,
        maze_object.width,
        json.loads(maze_object.structure),
    )
    solver = MazeSolver(maze=maze)
    algorithm_code = algorithm_object.code

    solver.solve(algorithm_code)
    solver_result = {"solution": None, "visited": None, "score": None, "check": None, "error": None}

    if solver.error:
        solver_result["error"] = solver.error
        return solver_result

    check = solver.check_solution()
    if not check[0]:
        solver_result["check"] = check
        return solver_result

    solver.calculateScore()

    solver_result.update(
        {
            "solution": solver.solution,
            "visited": solver.visited,
            "score": solver.score,
        }
    )

    return solver_result
