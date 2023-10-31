import base64
from flask import jsonify, make_response, request
import json
from services.user.get_user import get_user_id
from scripts.maze_generator import Maze, SidewinderFactory, RecursiveBacktrackingFactory, MazeImage, MazeSolver
from db import models
from db.db import db

User = models.User
Mazes = models.Mazes
Highscores = models.Highscores
Algorithms = models.Algorithms


def register_maze_routes(api):
    @ api.route("/v1/get_mazes", methods=["GET"])
    def get_mazes():
        mazes = []
        for maze in Mazes.query.filter_by(creator=0):
            if maze.isTest:
                continue
            highscoreList = get_highscores(maze.id)
            mazes.append({"id": maze.id, "name": maze.name,
                          "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList})
        return jsonify(mazes)

    @ api.route("/v1/get_my_mazes", methods=["GET"])
    def get_my_mazes():
        user_id = get_user_id(request)
        mazes = []
        for maze in Mazes.query.filter_by(creator=user_id):
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
        is_test = maze_object.isTest

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
            return jsonify(error_message)
        elif is_test:
            # Update is working
            algorithm_object.isWorking = True
            db.session.commit()
        check = solver.check_solution()
        if not check[0]:
            return jsonify(check)
        solver.calculateScore()

        solver_result = {"solution": solver.solution,
                         "visited": solver.visited,
                         "score": solver.score}
        # Return solution
        return jsonify(solver_result)

    @api.route("/v1/generate_maze", methods=["POST"])
    def generate_maze():
        user_id = get_user_id(request)
        maze_name = request.json["mazeName"]
        maze_size = request.json["mazeSize"]
        if maze_size > 30:
            error_message = "Invalid request"
            response = make_response(error_message, 400)
            return response
        maze_generator = RecursiveBacktrackingFactory().create_generator()

        maze = maze_generator.generate(int(maze_size))
        maze_image_byte_array = MazeImage.generateMazeImage(maze)
        maze_image_base_64 = base64.b64encode(
            maze_image_byte_array).decode('utf-8')

        new_maze = Mazes(
            name=maze_name,
            difficulty=maze.difficulty.name,
            imgLink=maze_image_base_64,
            structure=str(maze.structure),
            height=int(maze.height),
            width=int(maze.width),
            creator=user_id)

        new_maze.save()


def get_highscores(maze_id):
    highscores = Highscores.query.filter_by(mazeId=maze_id)
    highscoreList = []
    for highscore in highscores:
        user_email = User.query.filter_by(
            id=highscore.userId).first().email
        highscoreList.append(
            {"name": user_email, "score": highscore.score})
    return highscoreList
