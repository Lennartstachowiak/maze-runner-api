from flask import jsonify, request
from db.db import db
import json
from scripts.maze_generator import Maze, MazeSolver
from db import models

Mazes = models.Mazes
Algorithms = models.Algorithms

def register_algorithm_routes(api):
    @api.route("/v1/get_algorithms", methods=["GET"])
    def get_algorithms():
        algorithmList = []
        for algorithm in Algorithms.query.all():
            algorithmList.append(
                {"id": algorithm.id, "name": algorithm.name, "code": algorithm.code})
        return jsonify(algorithmList)
    
    @api.route("/v1/save_algorithm_changes",methods=["POST"])
    def save_algorithm():
        algorithm_id = request.json["algorithmId"]
        new_code = request.json["newCode"]
        algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
        algorithm.code = new_code
        # Commit the changes
        db.session.commit()
        response = {"status": 200}
        return jsonify(response)