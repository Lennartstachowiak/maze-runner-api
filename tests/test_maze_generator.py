import pytest
from app.models.maze.maze_generator_factory import SidewinderFactory, SidewinderAlgorithm, Cell


def test_maze_generator_factory_for_sidewinder():
    result = SidewinderFactory().create_generator()
    assert isinstance(result, SidewinderAlgorithm)


@pytest.fixture
def sidewinder_maze():
    size = 3
    sidewinder_maze_generator = SidewinderFactory().create_generator()
    sidewinderMaze = sidewinder_maze_generator.generate(size)
    return sidewinderMaze


def test_generated_maze_size(sidewinder_maze):
    assert len(sidewinder_maze.structure) == 3
    assert len(sidewinder_maze.structure[0]) == 3


def test_generated_maze_goals(sidewinder_maze):
    assert sidewinder_maze.structure[0][0].start is True
    assert sidewinder_maze.structure[-1][-1].goal is True


def test_sidewinder_algorithm(sidewinder_maze):
    initial_maze = [[Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell()]]
    assert initial_maze is not sidewinder_maze.structure
