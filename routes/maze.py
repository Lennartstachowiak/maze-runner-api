from flask import jsonify, request
import json
from scripts.maze_generator import Maze, MazeSolver
from db import models

User = models.User
Mazes = models.Mazes
Highscores = models.Highscores
Algorithms = models.Algorithms


def register_maze_routes(api):
    @ api.route("/v1/get_mazes", methods=["GET"])
    def get_mazes():
        mazes = []
        for maze in Mazes.query.all():
            highscoreList = get_highscores(maze.id)
            mazes.append({"id": maze.id, "name": maze.name,
                          "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList})
        return jsonify(mazes)

    @api.route("/v1/get_single_maze", methods=["GET"])
    def get_single_maze():
        maze_id = request.args.get("id")
        maze = Mazes.query.filter_by(id=maze_id).first()
        highscoreList = get_highscores(maze_id)
        single_maze = {"id": maze.id, "name": maze.name,
                       "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "structure": maze.structure}
        return jsonify(single_maze)

    @api.route("/v1/get_maze_algorithm_solution", methods=["POST"])
    def get_maze_algorithm_solution():
        algorithm_id = request.json["algorithmId"]
        maze_id = request.json["mazeId"]

        # Get Maze
        maze_object = Mazes.query.filter_by(id=maze_id).first()
        # Get Algorithm

        # Solve maze with algorithm
        maze = Maze(maze_object.height, maze_object.width,
                    json.loads(maze_object.structure))

        solver = MazeSolver(maze=maze)
        algorithm_object = Algorithms.query.filter_by(id=algorithm_id).first()
        algorithm_code = algorithm_object.code
        solver.solve(algorithm_code)
        solver.calculateScore()

        solver_result = {"solution": solver.solution,
                         "visited": solver.visited,
                         "score": solver.score}
        # Return solution
        return jsonify(solver_result)


def get_highscores(maze_id):
    highscores = Highscores.query.filter_by(mazeId=maze_id)
    highscoreList = []
    for highscore in highscores:
        user_email = User.query.filter_by(
            id=highscore.userId).first().email
        highscoreList.append(
            {"name": user_email, "score": highscore.score})
    return highscoreList
