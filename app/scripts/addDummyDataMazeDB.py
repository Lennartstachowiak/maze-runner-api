from api import create_api
from app.models.maze.generate_maze import MazeImageDrawer
from app.models.maze.maze_generator_factory import RecursiveBacktrackingFactory
from db.models import Mazes
import base64

api = create_api()
api.app_context().push()

sidewinder_maze_generator = RecursiveBacktrackingFactory().create_generator()

simple_maze = sidewinder_maze_generator.generate(10)
simple_maze_image_byte_array = MazeImageDrawer.generate_maze_image(simple_maze)
simple_maze_image_base_64 = base64.b64encode(
    simple_maze_image_byte_array).decode('utf-8')

medium_maze = sidewinder_maze_generator.generate(20)
medium_maze_image_byte_array = MazeImageDrawer.generate_maze_image(medium_maze)
medium_maze_image_base_64 = base64.b64encode(
    medium_maze_image_byte_array).decode('utf-8')

hard_maze = sidewinder_maze_generator.generate(30)
hard_maze_image_byte_array = MazeImageDrawer.generate_maze_image(hard_maze)
hard_maze_image_base_64 = base64.b64encode(
    hard_maze_image_byte_array).decode('utf-8')

dummy_mazes = [{"id": 100, "isTest": True, "name": "Test Maze", "difficulty": simple_maze.difficulty.name, "imgLink": simple_maze_image_base_64,
               "structure": simple_maze.structure, "height": simple_maze.height, "width": simple_maze.width},
               {"name": "Beginner Maze", "difficulty": simple_maze.difficulty.name, "imgLink": simple_maze_image_base_64,
               "structure": simple_maze.structure, "height": simple_maze.height, "width": simple_maze.width},
               {"name": "Intermediate Maze", "difficulty": medium_maze.difficulty.name, "imgLink": medium_maze_image_base_64,
               "structure": medium_maze.structure, "height": medium_maze.height, "width": medium_maze.width},
               {"name": "Advanced Maze", "difficulty": hard_maze.difficulty.name, "imgLink": hard_maze_image_base_64,
               "structure": hard_maze.structure, "height": hard_maze.height, "width": hard_maze.width}]

for maze in dummy_mazes:
    if "id" in maze:
        new_maze = Mazes(id=maze["id"], isTest=maze["isTest"], name=maze["name"], difficulty=maze["difficulty"],
                         imgLink=maze["imgLink"], structure=str(
                             maze["structure"]),
                         height=int(maze["height"]), width=int(maze["width"]), creator="official")
    else:
        new_maze = Mazes(name=maze["name"], difficulty=maze["difficulty"],
                         imgLink=maze["imgLink"], structure=str(
                             maze["structure"]),
                         height=int(maze["height"]), width=int(maze["width"]), creator="official")
    new_maze.save()
