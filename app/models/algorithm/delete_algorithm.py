from flask import abort, jsonify
from db.models import Algorithms


def delete_algorithm(user_id, algorithm_id):
    algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
    if (algorithm.userId == user_id):
        algorithm.delete()
        response = {"status": 204}
        return jsonify(response)
    else:
        abort(401, "Unauthorized")
