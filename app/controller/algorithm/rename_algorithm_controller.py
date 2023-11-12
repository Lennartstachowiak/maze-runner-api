from flask import abort, jsonify
from app.models.algorithm.rename_algorithm import rename_algorithm
from app.models.user.get_user import get_user
from db.db import db


def rename_algorithm_controller(request):
    user = get_user(request)
    user_id = user.id
    algorithm_id = request.json["algorithmId"]
    new_name = request.json["newName"]
    is_renamed = rename_algorithm(user_id, algorithm_id, new_name)
    if (is_renamed):
        db.session.commit()
        response = {"status": 200}
        return jsonify(response)
    else:
        abort(401, "Unauthorized")
