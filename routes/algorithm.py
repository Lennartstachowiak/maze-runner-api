from flask import jsonify, request
from db.db import db
import json
from scripts.maze_generator import Maze, MazeSolver
from db import models
import textwrap
from routes.user import get_user

Mazes = models.Mazes
Algorithms = models.Algorithms
algorithm_schema_code = """
function returnSolution(node, maze) {
    const solution = [];
    const visited = [];

    function solveMaze(node) {
    
    }

    solveMaze(node);
    return JSON.stringify([solution, visited])
}
""".strip() + '\n'


def register_algorithm_routes(api):
    @api.route("/v1/get_algorithms", methods=["GET"])
    def get_algorithms():
        user = get_user(request)
        user_id = user.id
        algorithmList = []
        for algorithm in Algorithms.query.filter_by(userId=user_id).all():
            algorithmList.append(
                {"id": algorithm.id, "name": algorithm.name, "code": algorithm.code})
        return jsonify(algorithmList)

    @api.route("/v1/save_algorithm_changes", methods=["POST"])
    def save_algorithm():
        algorithm_id = request.json["algorithmId"]
        new_code = request.json["newCode"]
        algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
        algorithm.code = new_code
        # Commit the changes
        db.session.commit()
        response = {"status": 200}
        return jsonify(response)

    @api.route("/v1/add_new_algorithm", methods=["POST"])
    def add_new_algorithm():
        algorithms_count = len(Algorithms.query.all())
        new_algorithm = Algorithms(
            name=f"Algorithm nr. {algorithms_count}", code=algorithm_schema_code)
        new_algorithm.save()
        response = {"status": 201}
        return jsonify(response)

    @api.route("/v1/delete_algorithm", methods=["DELETE"])
    def delete_algorithm():
        algorithm_id = request.json["algorithmId"]
        algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
        algorithm.delete()
        response = {"status": 204}
        return jsonify(response)

    @api.route("/v1/rename_algorithm", methods=["PATCH"])
    def rename_algorithm():
        algorithm_id = request.json["algorithmId"]
        new_name = request.json["newName"]
        algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
        algorithm.name = new_name
        db.session.commit()
        response = {"status": 200}
        return jsonify(response)
