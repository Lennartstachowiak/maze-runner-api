import pytest
from maze_generator import SidewinderFactory, SidewinderAlgorithmMazeGenerator, Cell, Maze
from copy import copy


def test_maze_generator_factory_for_sidewinder():
    result = SidewinderFactory().create_generator()
    assert isinstance(result, SidewinderAlgorithmMazeGenerator)


@pytest.fixture
def sidewinder_algorithm():
    maze = SidewinderAlgorithmMazeGenerator()
    maze.height = 3
    maze.width = 3
    maze.vector_list = []
    return maze


def test_generate_init_maze_without_paths(sidewinder_algorithm):
    generator = sidewinder_algorithm
    generator.generate_init_maze_without_paths()
    assert len(generator.vector_list) == 3
    assert len(generator.vector_list[0]) == 3
    assert generator.vector_list[0][0].start is True
    assert generator.vector_list[-1][-1].goal is True


def test_sidewinder_algorithm(sidewinder_algorithm):
    generator = sidewinder_algorithm
    initial_maze = [[Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell()]]
    generator.vector_list = copy(initial_maze)
    generator.sidewinder_algorithm()
    assert initial_maze is not generator.vector_list


def test_generate_for_sidewinder_algorithm_generator(sidewinder_algorithm):
    size = 3
    generator = SidewinderAlgorithmMazeGenerator()
    maze = generator.generate(size)
    assert isinstance(maze, Maze)
    assert maze.height is size
    assert maze.width is size
    assert len(maze.vector_list) is size
    assert len(maze.vector_list[0]) is size
