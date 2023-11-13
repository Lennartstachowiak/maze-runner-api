from flask import abort, jsonify
from app.models.algorithm.get_single_algorithm import get_single_algorithm
from app.models.user.get_user import get_user
from db.db import db
from db.models import Algorithms


def rename_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithm_id = request.json["algorithmId"]
    new_name = request.json["newName"]
    algorithm: type[Algorithms] = get_single_algorithm(algorithm_id)
    if not algorithm or algorithm["userId"] != user_id:
        abort(401, "Unauthorized")
    algorithm.name = new_name
    db.session.commit()
    response = {"status": 200}
    return jsonify(response)
