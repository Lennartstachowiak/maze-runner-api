from flask import jsonify
from app.models.algorithm.get_single_algorithm import get_single_algorithm


def get_single_algorithm_controller(request):
    algorithm_id = request.args.get("id")
    algorithm = get_single_algorithm(algorithm_id)
    return jsonify(algorithm)
