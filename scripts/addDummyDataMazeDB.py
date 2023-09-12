from api import create_api
from db.models import Mazes
from scripts.maze_generator import MazeGeneratorFactory, MazeImage
import base64

api = create_api()
api.app_context().push()

sidewinder_maze_generator = MazeGeneratorFactory.create_maze_generator(
    "sidewinder")

simple_maze = sidewinder_maze_generator.generate(15)
simple_maze_image_byte_array = MazeImage.generateMazeImage(simple_maze)
simple_maze_image_base_64 = base64.b64encode(
    simple_maze_image_byte_array).decode('utf-8')

medium_maze = sidewinder_maze_generator.generate(30)
medium_maze_image_byte_array = MazeImage.generateMazeImage(medium_maze)
medium_maze_image_base_64 = base64.b64encode(
    medium_maze_image_byte_array).decode('utf-8')

hard_maze = sidewinder_maze_generator.generate(45)
hard_maze_image_byte_array = MazeImage.generateMazeImage(hard_maze)
hard_maze_image_base_64 = base64.b64encode(
    hard_maze_image_byte_array).decode('utf-8')

dummy_mazes = [{"name": "Beginner Maze", "difficulty": simple_maze.difficulty.name, "imgLink": simple_maze_image_base_64,
               "structure": simple_maze.structure, "height": simple_maze.height, "width": simple_maze.width},
               {"name": "Intermediate Maze", "difficulty": medium_maze.difficulty.name, "imgLink": medium_maze_image_base_64,
               "structure": medium_maze.structure, "height": medium_maze.height, "width": medium_maze.width},
               {"name": "Advanced Maze", "difficulty": hard_maze.difficulty.name, "imgLink": hard_maze_image_base_64,
               "structure": hard_maze.structure, "height": hard_maze.height, "width": hard_maze.width}]

for maze in dummy_mazes:
    new_maze = Mazes(name=maze["name"], difficulty=maze["difficulty"],
                     imgLink=maze["imgLink"], structure=str(maze["structure"]),
                     height=int(maze["height"]), width=int(maze["width"]))
    new_maze.save()
