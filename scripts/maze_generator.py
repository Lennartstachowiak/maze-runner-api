from collections import deque
import random
import json
import subprocess
from io import BytesIO
from PIL import Image, ImageDraw
from abc import ABC, abstractmethod
from flask import jsonify


class Cell:
    def __init__(self, north=1, east=1, south=1, west=1, start=False, goal=False):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.start = start
        self.goal = goal

    def to_dict(self):
        return {
            "north": self.north,
            "east": self.east,
            "south": self.south,
            "west": self.west,
            "start": self.start,
            "goal": self.goal
        }

    def get_neigbour(self, position):
        x, y = position
        neigbours = []
        directions = [(-1, 0), [0, 1], [1, 0], [0, -1]]  # N, O, S, W
        for is_wall, (dx, dy) in zip([self.north, self.east, self.south, self.west], directions):
            if not is_wall:
                neigbour_x, neigbour_y = x + dx, y + dy
                neigbours.append([neigbour_x, neigbour_y])

        return neigbours

    def __str__(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.__str__()


class Difficulty:
    def __init__(self, index, name):
        self._index = index
        self._name = name

    def to_dict(self):
        maze_dict = {
            "index": self._index,
            "name": self._name,
        }
        return maze_dict

    def __str__(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.__str__()

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

    def to_dict(self):
        maze_dict = {
            "height": self.height,
            "width": self.width,
            "structure": self.structure,
            "difficulty": self.difficulty
        }
        return maze_dict

    def __str__(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return self.__str__()

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


def bfs(node, maze, solution, visited):
    queue = deque([(node, [])])

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

    def solve(self, algorithm_code):
        start = self._find_start()
        maze_json = json.dumps(self.maze.to_dict())
        if start and algorithm_code:
            try:
                command = ['node', '-p',
                           f'{algorithm_code}; returnSolution(JSON.parse(\'{json.dumps(start)}\'), {maze_json})']
                result = subprocess.run(
                    command,
                    capture_output=True,
                    encoding='utf-8',
                )
                stderr = result.stderr
                stdout = result.stdout
                solution, visited = json.loads(stdout)
                self.solution = solution
                self.visited = visited
            except subprocess.CalledProcessError as e:
                print(
                    f"Command execution failed with exit code {e.returncode}")
                print("ERROR", e.output)
        else:
            raise ValueError("No starting point in the maze")

        if not self.solution:
            raise ValueError("No solution found")

    def check_solution(self):
        solution = self.solution
        visited = self.visited
        if not solution:
            return (False, "No solution yet")
        found_goal = False
        # Check solution path
        for index, step in enumerate(solution):
            x, y = step
            cell = Cell(*self.maze.structure[x][y].values())
            neigbours = cell.get_neigbour((x, y))
            if cell.goal:
                found_goal = True
            try:
                next_step = solution[index + 1]
            except IndexError:
                break
            if next_step not in neigbours:
                return (False, "Solution path wrong")
        # Check visited path
        start_visited = visited[0]
        can_be_visited = [start_visited]
        for step in visited:
            x, y = step
            cell = Cell(*self.maze.structure[x][y].values())
            neigbours = cell.get_neigbour([x, y])
            can_be_visited.extend(neigbours)
            if [x, y] not in can_be_visited:
                return (False, "Visited path wrong")
        if not found_goal:
            return (False, "No Goal found")
        return (True, "All good")

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
        self.score = round(final_score, 2)


solver = MazeSolver(maze=sidewinderMaze)
