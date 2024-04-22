from flask import jsonify
from app.models.maze.get_my_mazes_objects import get_mazes_objects


def get_user_mazes_controller(request):
    user_id = request.args.get("id")
    mazes_objects = get_mazes_objects(user_id)
    return jsonify(mazes_objects)
