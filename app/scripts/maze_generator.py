from app.models.maze.maze import MazeImage, MazeSolver, RecursiveBacktrackingFactory


size = 30

# sidewinder_maze_generator = SidewinderFactory().create_generator()
# sidewinderMaze = sidewinder_maze_generator.generate(size)
# sidewinderMazeImage = MazeImage.generateMazeImage(sidewinderMaze)

backtracking_factory = RecursiveBacktrackingFactory().create_generator()
backtrackingMaze = backtracking_factory.generate(size)
backtrackingMazeImage = MazeImage.generateMazeImage(backtrackingMaze)

solver = MazeSolver(maze=backtrackingMaze)
