from flask import jsonify
from app.models.user.follow_user import follow_user
from app.models.user.get_user import get_user
from flask import abort


def follow_user_controller(request):
    try:
        user_id = get_user(request)
        user_id_followed = request.json["userIdFollowed"]
        register_data = follow_user(user_id, user_id_followed)
        if register_data == 409:
            abort(409, 'Conflict')
        response = {"status": 200}
        return jsonify(response)
    except:
        abort(400, "Internal server error")
