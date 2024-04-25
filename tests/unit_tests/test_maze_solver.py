from tests.dummy_maze import get_dummy_maze
from tests.dummy_algorithm import get_dummy_algorithm
from app.models.maze.get_maze_algorithm_solution import get_maze_algorithm_solution


def check_if_path_is_correct(path):
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
    path_clone = path[:]
    previous_step = tuple(path_clone.pop(0))
    for x, y in path_clone:
        neighbors = [(x + delta_x, y + delta_y) for delta_x, delta_y in deltas]
        if previous_step not in neighbors:
            return False
        previous_step = (x, y)
    return True


def test_maze_solver():
    dummy_maze = get_dummy_maze()
    dummy_algorithm = get_dummy_algorithm()
    solution = get_maze_algorithm_solution(dummy_maze, dummy_algorithm)
    solution_path = solution["solution"]
    visited_path = solution["visited"]
    assert isinstance(solution_path, list)
    assert solution_path[0] == [0, 0]  # Solution path starts at [0, 0]
    assert solution_path[-1] == [9, 9]  # Solution path ends at [9, 9]
    assert visited_path[0] == [0, 0]  # Visited path starts at [0, 0]
    assert visited_path[-1] == [9, 9]  # Visited path ends at [9, 9]
    is_solution_path_correct = check_if_path_is_correct(solution_path)
    assert is_solution_path_correct
