from flask import jsonify
from app.models.algorithm.get_algorithms import get_algorithms
from app.models.algorithm.get_algorithms_object import get_algorithms_objects
from app.models.user.get_user import get_user


def get_algorithms_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithms = get_algorithms(user_id)
    algorithms_object_list = get_algorithms_objects(algorithms)
    return jsonify(algorithms_object_list)
