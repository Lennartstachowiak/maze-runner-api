from flask import jsonify
from app.models.algorithm.add_new_algorithm import add_new_algorithm
from app.models.algorithm.get_new_algorithm import get_new_algorithm
from app.models.user.get_user import get_user
from db.models import Algorithms


def add_new_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    new_algorithm: type[Algorithms] = get_new_algorithm(user_id)
    add_new_algorithm(new_algorithm)
    response = {"status": 201}
    return jsonify(response)
