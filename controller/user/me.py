from flask import jsonify
from services.user.get_user import get_user


def me(request):
    user = get_user(request)
    res = jsonify({
        "id": user.id,
        "email": user.email
    })
    return res
