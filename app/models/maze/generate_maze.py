import base64
from flask import abort, make_response
from app.models.maze.maze import MazeImage, RecursiveBacktrackingFactory
from db import models

Mazes = models.Mazes


def generate_maze(user_id, maze_name, maze_size):
    if maze_size > 30 or maze_size < 4:
        abort(400, "Invalid request")
    maze_generator = RecursiveBacktrackingFactory().create_generator()

    maze = maze_generator.generate(int(maze_size))
    maze_image_byte_array = MazeImage.generateMazeImage(maze)
    maze_image_base_64 = base64.b64encode(
        maze_image_byte_array).decode('utf-8')

    new_maze = Mazes(
        name=maze_name,
        difficulty=maze.difficulty.name,
        imgLink=maze_image_base_64,
        structure=str(maze.structure),
        height=int(maze.height),
        width=int(maze.width),
        creator=user_id)

    return new_maze
