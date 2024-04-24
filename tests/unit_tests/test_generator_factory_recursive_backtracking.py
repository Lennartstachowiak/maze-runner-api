import pytest
from app.models.maze.maze_generator_factory import (
    RecursiveBacktrackingFactory,
    RecursiveBacktracking,
    Cell,
)
import copy


def test_maze_generator_factory_for_sidewinder():
    # Check if generator is expected instance
    result = RecursiveBacktrackingFactory().create_generator()
    assert isinstance(result, RecursiveBacktracking)


@pytest.fixture
def recursive_backtracking_maze():
    size = 10
    recursive_backtracking_maze_generator = RecursiveBacktrackingFactory().create_generator()
    recursive_backtracking_maze = recursive_backtracking_maze_generator.generate(size)
    return recursive_backtracking_maze


def test_generated_maze_size(recursive_backtracking_maze):
    # Test if width and height is as expected
    assert len(recursive_backtracking_maze.structure) == 10
    assert len(recursive_backtracking_maze.structure[0]) == 10


def test_generated_maze_goals(recursive_backtracking_maze):
    # Test of maze has goal and start as expected
    assert recursive_backtracking_maze.structure[0][0].start is True
    assert recursive_backtracking_maze.structure[-1][-1].goal is True


def test_sidewinder_algorithm(recursive_backtracking_maze):
    # Test if structure changes and is not empty / initial structure
    initial_maze = [
        [Cell(), Cell(), Cell()],
        [Cell(), Cell(), Cell()],
        [Cell(), Cell(), Cell()],
    ]
    assert initial_maze is not recursive_backtracking_maze.structure


def test_maze_has_valid_path(recursive_backtracking_maze):
    start_position = (0, 0)

    def has_path_to_goal(position: tuple, visited=set(), queue=set()):
        queue.add(position)
        while len(queue) > 0:
            x, y = queue.pop()
            current_cell: Cell = recursive_backtracking_maze.structure[x][y]
            visited.add((x, y))
            if current_cell.goal:
                return True
            directions = ["north", "east", "south", "west"]
            deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
            for i in range(len(directions)):
                direction = directions[i]
                current_cell_dict = current_cell.to_dict()
                if current_cell_dict[direction] == 1:
                    continue
                delta = deltas[i]
                dx, dy = delta
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in visited:
                    queue.add((new_x, new_y))
        return False

    assert has_path_to_goal(start_position) is True


def test_maze_doesnt_have_open_walls(recursive_backtracking_maze):
    maze_height = len(recursive_backtracking_maze.structure)
    maze_width = len(recursive_backtracking_maze.structure[0])

    def check_for_open_walls():
        # Check Top and Bottom
        for i in range(maze_width):
            current_cell_top: Cell = recursive_backtracking_maze.structure[0][i]
            if current_cell_top.north == 0:
                return False
            current_cell_bottom: Cell = recursive_backtracking_maze.structure[maze_height - 1][i]
            if current_cell_bottom.south == 0:
                return False
        # Check left and right
        for i in range(maze_height):
            current_cell_left: Cell = recursive_backtracking_maze.structure[i][0]
            if current_cell_left.west == 0:
                return False
            current_cell_right: Cell = recursive_backtracking_maze.structure[i][maze_width - 1]
            if current_cell_right.east == 0:
                return False
        return True

    assert check_for_open_walls() is True


def test_maze_randomness():
    # Test if two generated mazes with the same config are different
    size = 10
    recursive_backtracking_maze_generator = RecursiveBacktrackingFactory().create_generator()
    first_maze = recursive_backtracking_maze_generator.generate(size)
    second_maze = recursive_backtracking_maze_generator.generate(size)
    first_maze_copy = copy.deepcopy(first_maze)

    is_same_maze_same = first_maze.__str__() == first_maze_copy.__str__()
    is_different_maze_different = first_maze.__str__() != second_maze.__str__()
    assert is_same_maze_same and is_different_maze_different
