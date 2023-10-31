from flask import jsonify
from app.models.maze.get_mazes import get_mazes


def get_mazes_contoller():
    mazes = get_mazes()
    return jsonify(mazes)
