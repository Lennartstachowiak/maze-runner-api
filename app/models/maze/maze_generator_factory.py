from abc import ABC, abstractmethod
import random
from app.models.maze.maze import Cell, Maze


class MazeGeneratorFactory(ABC):
    @abstractmethod
    def create_generator(self):
        pass


class SidewinderFactory(MazeGeneratorFactory):
    def create_generator(self):
        return SidewinderAlgorithm()


class RecursiveBacktrackingFactory(MazeGeneratorFactory):
    def create_generator(self):
        return RecursiveBacktracking()


class MazeStructure:
    @staticmethod
    def generate_structure(height, width):
        structure = []
        for row in range(height):
            structure.append([])
            for column in range(width):
                if row == 0 and column == 0:
                    structure[row].append(Cell(start=True))
                elif row == height - 1 and column == width - 1:
                    structure[row].append(Cell(goal=True))
                else:
                    structure[row].append(Cell())
        return structure


# Abstract Product
class MazeGenerator(ABC):
    @abstractmethod
    def generate_maze(self):
        pass

    def generate(self, size):
        self.height = size
        self.width = size
        self.structure = MazeStructure.generate_structure(self.height, self.width)
        self.generate_maze()
        maze = Maze(self.height, self.width, self.structure)
        maze.calculate_difficulty_of_maze()
        return maze


class RecursiveBacktracking(MazeGenerator):
    # Concrete Product
    def generate_maze(self):
        self._recursive_backtracking(0, 0)

    def _recursive_backtracking(self, row, column):
        neighbors = self._get_randomized_neighbors(row, column)
        for neighbor_row, neighbor_column in neighbors:
            if self._is_valid_cell(neighbor_row, neighbor_column) and self._is_not_visited(
                neighbor_row, neighbor_column
            ):
                self._carve_path(row, column, neighbor_row, neighbor_column)
                self._recursive_backtracking(neighbor_row, neighbor_column)

    def _get_randomized_neighbors(self, row, column):
        neighbors = [
            (row - 1, column),
            (row, column + 1),
            (row + 1, column),
            (row, column - 1),
        ]  # N, E, S, W
        random.shuffle(neighbors)
        return neighbors

    def _is_valid_cell(self, row, column):
        return 0 <= row < self.height and 0 <= column < self.width

    def _is_not_visited(self, row, column):
        cell = self.structure[row][column]
        return cell.north == 1 and cell.east == 1 and cell.south == 1 and cell.west == 1

    def _carve_path(self, current_row, current_column, row, column):
        # North
        if current_row < row:
            self.structure[current_row][current_column].south = 0
            self.structure[row][column].north = 0
            return
        # East
        if current_column < column:
            self.structure[current_row][current_column].east = 0
            self.structure[row][column].west = 0
            return
        # South
        if current_row > row:
            self.structure[current_row][current_column].north = 0
            self.structure[row][column].south = 0
            return
        # West
        if current_column > column:
            self.structure[current_row][current_column].west = 0
            self.structure[row][column].east = 0
            return


class SidewinderAlgorithm(MazeGenerator):
    # Concrete Product
    def generate_maze(self):
        for row in range(self.height):
            run_start = 0
            for column in range(self.width):
                if row > 0 and (column + 1 == self.width or random.randint(0, 2) == 0):
                    # end current run and carve north
                    cell = run_start + random.randint(0, column - run_start)
                    self.structure[row][cell].north = 0
                    self.structure[row - 1][cell].south = 0
                    run_start = column + 1
                elif column + 1 < self.width:
                    # carve east
                    self.structure[row][column].east = 0
                    self.structure[row][column + 1].west = 0
