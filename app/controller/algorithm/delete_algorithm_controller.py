from flask import abort, jsonify
from app.models.algorithm.delete_algorithm import delete_algorithm
from app.models.algorithm.get_single_algorithm import get_single_algorithm
from app.models.user.get_user import get_user
from db.models import Algorithms


def delete_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithm_id = request.json["algorithmId"]
    algorithm: type[Algorithms] = get_single_algorithm(algorithm_id)
    if not algorithm or algorithm.user_id != user_id:
        abort(401, "Unauthorized")
    delete_algorithm(algorithm)
    response = {"status": 204}
    return jsonify(response)
