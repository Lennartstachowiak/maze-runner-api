from flask import jsonify
from app.models.maze.get_mazes_objects import get_mazes_objects


def get_mazes_contoller():
    mazes_objects = get_mazes_objects()
    return jsonify(mazes_objects)
