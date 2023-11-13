from flask import jsonify
from app.models.algorithm.create_algorithm_object import create_algorithm_object
from app.models.algorithm.get_single_algorithm import get_single_algorithm
from db.models import Algorithms


def get_single_algorithm_controller(request):
    algorithm_id = request.args.get("id")
    algorithm: type[Algorithms] = get_single_algorithm(algorithm_id)
    algorithm_object = create_algorithm_object(algorithm)
    return jsonify(algorithm_object)
