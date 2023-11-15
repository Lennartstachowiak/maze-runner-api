from app.models.maze.maze import MazeImageFacade, MazeSolver
from app.models.maze.maze_generator_factory import RecursiveBacktrackingFactory


size = 30

# sidewinder_maze_generator = SidewinderFactory().create_generator()
# sidewinderMaze = sidewinder_maze_generator.generate(size)
# sidewinderMazeImage = MazeImageFacade.generate_maze_image(sidewinderMaze)

backtracking_factory = RecursiveBacktrackingFactory().create_generator()
backtrackingMaze = backtracking_factory.generate(size)
backtrackingMazeImage = MazeImageFacade.generate_maze_image(backtrackingMaze)

solver = MazeSolver(maze=backtrackingMaze)
