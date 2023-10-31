from flask import jsonify
from db import models
from services.maze.get_mazes import get_mazes

Mazes = models.Mazes


def get_mazes_contoller():
    mazes = get_mazes()
    return jsonify(mazes)
