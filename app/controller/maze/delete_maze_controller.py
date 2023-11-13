from flask import abort, jsonify
from app.models.maze.get_single_maze import get_single_maze
from app.models.user.get_user import get_user_id
from db.db import db
from db import models

Mazes = models.Mazes


def delete_maze_controller(request):
    user_id = get_user_id(request)
    maze_id = request.json["mazeId"]
    maze = get_single_maze(maze_id)
    if not maze or maze.creator != user_id:
        abort(401, "Unauthorized")
    maze.delete()
    db.session.commit()
    return jsonify("Maze deleted!")
