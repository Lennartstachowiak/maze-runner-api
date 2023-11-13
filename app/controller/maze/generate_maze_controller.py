from flask import jsonify
from app.models.maze.generate_maze import generate_maze
from app.models.user.get_user import get_user_id
from db.db import db
from db.models import Mazes


def generate_maze_controller(request):
    user_id = get_user_id(request)
    maze_name = request.json["mazeName"]
    maze_size = request.json["mazeSize"]
    new_maze: type[Mazes] = generate_maze(user_id, maze_name, maze_size)
    new_maze.save()
    db.session.commit()
    return jsonify("New maze generated!")
