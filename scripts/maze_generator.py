from collections import deque
import random
import json
from io import BytesIO
from PIL import Image, ImageDraw
from abc import ABC, abstractmethod


class Cell:
    def __init__(self, north=1, east=1, south=1, west=1, start=False, goal=False):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.start = start
        self.goal = goal

    def __str__(self):
        return json.dumps({"north": self.north, "east": self.east, "south": self.south, "west": self.west, "start": self.start, "goal": self.goal})

    def __repr__(self):
        return self.__str__()
    
class Difficulty:
    def __init__(self,index,name):
        self._index=index
        self._name=name
    @property
    def index(self):
        return self._index
    @property
    def name(self):
        return self._name


class Maze:
    def __init__(self, height, width, structure):
        self.height = height
        self.width = width
        self.structure = structure
        self.difficulty = None

    def calculateDifficultyOfMaze(self):
        size = (self.height+self.width)/2
        if size <= 15:
            self.difficulty = Difficulty(0, "Easy")
        elif size <= 30:
            self.difficulty = Difficulty(1, "Medium")
        else:
            self.difficulty = Difficulty(2, "Hard")


    def __str__(self, solutionList=[]):
        maze_str = ""
        for row_index, row in enumerate(self.structure):
            row_cells = []
            for column_index, cell in enumerate(row):
                # Refactor this part is duplicated
                cell = self.structure[row_index][column_index]
                if type(cell) == dict:
                    cell = Cell(**cell)
                cell_represent = [
                    ["#", " ", " ", "#"],
                    [" ", " ", " ", " "],
                    [" ", " ", " ", " "],
                    ["#", " ", " ", "#"]
                ]

                # Solution
                for solution in solutionList:
                    x, y = solution["node"]
                    if (row_index, column_index) == (x, y):
                        if "next" not in solution:
                            continue
                        next_x, next_y = solution["next"]
                        # Bottom
                        if next_x > x:
                            symbol = "⬇"
                            cell_represent[3][1] = symbol
                            cell_represent[3][2] = symbol
                        # Top
                        if next_x < x:
                            symbol = "⬆"
                            cell_represent[0][1] = symbol
                            cell_represent[0][2] = symbol
                        # Right
                        if next_y > y:
                            symbol = "⮕"
                            cell_represent[1][3] = symbol
                            cell_represent[2][3] = symbol
                        # Left
                        if next_y < y:
                            symbol = "⬅"
                            cell_represent[1][0] = symbol
                            cell_represent[2][0] = symbol

                        cell_represent[1][1] = symbol
                        cell_represent[1][2] = symbol
                        cell_represent[2][1] = symbol
                        cell_represent[2][2] = symbol

                # West
                if cell.west == 1:
                    cell_represent[1][0] = "#"
                    cell_represent[2][0] = "#"

                # North
                if cell.north == 1:
                    cell_represent[0][1] = "#"
                    cell_represent[0][2] = "#"

                # South
                if cell.south == 1:
                    cell_represent[3][1] = "#"
                    cell_represent[3][2] = "#"

                # East
                if cell.east == 1:
                    cell_represent[1][3] = "#"
                    cell_represent[2][3] = "#"

                # Start
                if cell.start == True:
                    cell_represent[1][1] = "S"
                    cell_represent[1][2] = "S"
                    cell_represent[2][1] = "S"
                    cell_represent[2][2] = "S"

                # Goal
                if cell.goal == True:
                    cell_represent[1][1] = "X"
                    cell_represent[1][2] = "X"
                    cell_represent[2][1] = "X"
                    cell_represent[2][2] = "X"

                row_cells.append(cell_represent)

            row_str = ""
            for cell_row_i in range(4):
                cell_row_str = ""
                for cell_row in row_cells:
                    cell_row_str += " ".join(
                        item for item in cell_row[cell_row_i]) + " "
                cell_row_str += "\n"
                row_str += cell_row_str
            maze_str += row_str
        return maze_str

    def __repr__(self):
        return self.__str__()


@abstractmethod
class MazeGenerator(ABC):
    def generate(self, size):
        pass


class SidewinderAlgorithmMazeGenerator(MazeGenerator):
    def generate_init_maze_without_paths(self):
        for row in range(self.height):
            self.structure.append([])
            for column in range(self.width):
                if row == 0 and column == 0:
                    self.structure[row].append(Cell(start=True))
                elif row == self.height-1 and column == self.width-1:
                    self.structure[row].append(Cell(goal=True))
                else:
                    self.structure[row].append(Cell())

    def sidewinder_algorithm(self):
        for row in range(self.height):
            run_start = 0
            for column in range(self.width):
                if row > 0 and (column+1 == self.width or random.randint(0, 2) == 0):
                    # end current run and carve north
                    cell = run_start + random.randint(0, column - run_start)
                    self.structure[row][cell].north = 0
                    self.structure[row-1][cell].south = 0
                    run_start = column+1
                elif column+1 < self.width:
                    # carve east
                    self.structure[row][column].east = 0
                    self.structure[row][column+1].west = 0

    def generate(self, size):
        self.height = size
        self.width = size
        self.structure = []
        self.generate_init_maze_without_paths()
        self.sidewinder_algorithm()
        maze = Maze(self.height, self.width, self.structure)
        maze.calculateDifficultyOfMaze()
        return maze


class MazeGeneratorFactory:
    @staticmethod
    def create_maze_generator(algorithm):
        if algorithm == "sidewinder":
            return SidewinderAlgorithmMazeGenerator()
        else:
            raise ValueError("Invalid algorithm name")


# Facade
class MazeImage:
    def generateMazeImage(maze):
        cell_size = 100
        cell_border = 10
        width = maze.width
        height = maze.height
        cells = maze.structure
        img = Image.new(
            "RGBA",
            (width * cell_size,
             height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)
        for row in range(height):
            for column in range(width):
                cell = cells[row][column]

                left_border = 0 if column != 0 else cell_border
                right_border = 0 if column != width-1 else cell_border
                top_border = 0 if row != 0 else cell_border
                bottom_border = 0 if row != height-1 else cell_border

                if cell.west == 1:
                    left_border += cell_border
                if cell.north == 1:
                    top_border += cell_border
                if cell.east == 1:
                    right_border += cell_border
                if cell.south == 1:
                    bottom_border += cell_border

                left = column * cell_size + left_border
                top = row * cell_size + top_border
                right = (column + 1) * cell_size - right_border
                bottom = (row + 1) * cell_size - bottom_border

                rect = [(left, top), (right, bottom)]

                if maze.structure[row][column].start:
                    draw.rectangle(rect, fill="red")
                elif maze.structure[row][column].goal:
                    draw.rectangle(rect, fill="green")
                else:
                    draw.rectangle(rect, fill="white")
        filename = "maze.png"
        byte_array = BytesIO()
        # use filename in save() for local testing
        # and use byte_array to save it as sendable data
        img.save(byte_array, format="png")
        image_data = byte_array.getvalue()
        return image_data


size = 15

sidewinder_maze_generator = MazeGeneratorFactory.create_maze_generator(
    "sidewinder")
sidewinderMaze = sidewinder_maze_generator.generate(size)
sidewinderMazeImage = MazeImage.generateMazeImage(sidewinderMaze)


def dfs(node, maze, solution, visited):
    (x, y) = node
    # Refactor this part is duplicated
    cell = maze.structure[x][y]
    if type(cell) == dict:
        cell = Cell(**cell)
    if cell.goal:
        solution.append(node)
        return True
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # W, N, E, S
    for direction, (dx, dy) in zip(['west', 'north', 'east', 'south'], directions):
        next_x, next_y = x + dx, y + dy
        if (0 <= next_x < maze.height and
            0 <= next_y < maze.width and
            not (next_x, next_y) in visited and
                getattr(cell, direction) == 0):
            visited.append((next_x, next_y))
            if dfs((next_x, next_y), maze, solution, visited):
                solution.append(node)
                return True
    return False


def bfs(start_node, maze, solution, visited):
    queue = deque([(start_node, [])])

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.append(node)

        (x, y) = node
        cell = maze.structure[x][y]
        if type(cell) == dict:
            cell = Cell(**cell)

        if cell.goal:
            solution.extend(path + [node])
            return True

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # W, N, E, S

        for direction, (dx, dy) in zip(['west', 'north', 'east', 'south'], directions):
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < maze.height and
                0 <= next_y < maze.width and
                (next_x, next_y) not in visited and
                    getattr(cell, direction) == 0):

                queue.append(((next_x, next_y), path + [node]))

    return False


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.solution = []
        self.visited = []
        self.score = None

    def _find_start(self):
        for row in range(self.maze.height):
            for col in range(self.maze.width):
                # Refactor this part is duplicated
                cell = self.maze.structure[row][col]
                if type(cell) == dict:
                    cell = Cell(**cell)
                if cell.start:
                    return (row, col)

    def solve(self, algorithm=""):
        start = self._find_start()
        if start:
            if algorithm == "258e6ff8b3fa4856b320eda39b22950f":
                dfs(start, self.maze, self.solution,
                    self.visited)
            bfs(start, self.maze, self.solution,
                self.visited)
        else:
            raise ValueError("No starting point in the maze")

        if not self.solution:
            raise ValueError("No solution found")
        
    def calculateScore(self):
        # The score will be calculate by efficency of the solution and search percentage
        #   - efficency -> solution steps divided by maze size 0 to ∞
        #   - search -> how many cells have been visited in the maze to find the solution (0 to 1)
        # In the end we calculate the efficency and add the efficency multiplied by the search score
        maze_height = self.maze.height
        maze_width = self.maze.width
        efficiency_score = (maze_height*maze_width)/len(self.solution)
        search_score = len(self.visited)/(maze_height*maze_width)
        final_score = efficiency_score+efficiency_score*search_score
        self.score = round(final_score,2)



solver = MazeSolver(maze=sidewinderMaze)
solver.solve()
