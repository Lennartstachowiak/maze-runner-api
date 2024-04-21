from flask import abort, jsonify
from app.models.maze.delete_highscore import delete_highscore
from app.models.maze.delete_maze import delete_maze
from app.models.maze.get_maze_highscores import get_maze_highscores
from app.models.maze.get_single_maze import get_single_maze
from app.models.user.get_user import get_user_id
from db.db import db
from db import models

Mazes = models.Mazes
Highscores = models.Highscores


def delete_maze_controller(request):
    user_id = get_user_id(request)
    maze_id = request.json["mazeId"]
    maze: type[Mazes] = get_single_maze(maze_id)
    if not maze or maze.creator != user_id:
        abort(401, "Unauthorized")
    highscores = get_maze_highscores(maze_id)
    for highscore in highscores:
        delete_highscore(highscore)
    delete_maze(maze)
    return jsonify("Maze deleted!")
