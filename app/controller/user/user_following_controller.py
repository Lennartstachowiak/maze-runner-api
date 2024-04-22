from app.models.user.get_user import get_user
from app.models.user.get_user_following import get_user_following
from flask import jsonify


def user_following_controller(request):
    user = get_user(request)
    following = get_user_following(user)
    return jsonify(following)
