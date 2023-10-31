from flask import jsonify
from services.maze.get_highscores import get_highscores
from services.maze.get_my_mazes import get_my_mazes
from services.user.get_user import get_user_id
from db import models

Mazes = models.Mazes


def get_my_mazes_controller(request):
    user_id = get_user_id(request)
    mazes = get_my_mazes(user_id)
    return jsonify(mazes)
