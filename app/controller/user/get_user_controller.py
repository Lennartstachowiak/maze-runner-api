from flask import jsonify
from app.models.user.get_user import get_user


def get_user_controller(request):
    user = get_user(request)

    res = jsonify({
        "id": user.id,
        "email": user.email
    })
    return res
