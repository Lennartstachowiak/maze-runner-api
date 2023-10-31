from flask import jsonify
from app.models.algorithm.add_new_algorithm import add_new_algorithm
from app.models.user.get_user import get_user


def add_new_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    isNewAlgorithm = add_new_algorithm(user_id)
    if isNewAlgorithm:
        response = {"status": 201}
        return jsonify(response)
