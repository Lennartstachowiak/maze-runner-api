from flask import jsonify
from services.algorithm.save_algorithm import save_algorithm
from services.user.get_user import get_user


def save_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithm_id = request.json["algorithmId"]
    new_code = request.json["newCode"]
    is_saved = save_algorithm(user_id, algorithm_id, new_code)
    if is_saved:
        response = {"status": 200}
        return jsonify(response)
    else:
        response = {"status": 401}
        return jsonify(response)
