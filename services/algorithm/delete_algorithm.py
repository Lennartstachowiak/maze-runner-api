from flask import jsonify
from db import models

Algorithms = models.Algorithms


def delete_algorithm(algorithm_id, user_id):
    algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
    if (algorithm.userId == user_id):
        algorithm.delete()
        response = {"status": 204}
        return jsonify(response)
    else:
        response = {"status": 401}
        return jsonify(response)
