from flask import abort, jsonify
from app.models.algorithm.delete_algorithm import delete_algorithm
from app.models.user.get_user import get_user


def delete_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithm_id = request.json["algorithmId"]
    is_deleted = delete_algorithm(user_id, algorithm_id)
    if (is_deleted):
        response = {"status": 204}
        return jsonify(response)
    else:
        abort(401, "Unauthorized")
