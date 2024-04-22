from app.models.user.get_user import get_user
from app.models.maze.get_followed_mazes import get_followed_mazes
from flask import jsonify


def get_followed_mazes_controller(request):
    user = get_user(request)
    mazes = get_followed_mazes(user)
    return jsonify(mazes)
