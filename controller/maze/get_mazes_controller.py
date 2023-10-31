from flask import jsonify
from services.maze.get_mazes import get_mazes


def get_mazes_contoller():
    mazes = get_mazes()
    return jsonify(mazes)
