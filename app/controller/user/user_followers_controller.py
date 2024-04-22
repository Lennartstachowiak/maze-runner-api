from app.models.user.get_user import get_user
from app.models.user.get_user_followers import get_user_followers
from flask import jsonify


def user_followers_controller(request):
    user = get_user(request)
    following = get_user_followers(user)
    return jsonify(following)
