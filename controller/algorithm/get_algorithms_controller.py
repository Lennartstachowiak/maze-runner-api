from flask import jsonify
from services.algorithm.get_algorithms import get_algorithms
from services.user.get_user import get_user


def get_algorithms_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithmList = get_algorithms(user_id)
    return jsonify(algorithmList)
