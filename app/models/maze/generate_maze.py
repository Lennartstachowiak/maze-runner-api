from abc import ABC, abstractmethod
import base64
from enum import Enum
from io import BytesIO
from PIL import Image, ImageDraw
from flask import abort
from app.models.maze.maze_generator_factory import RecursiveBacktrackingFactory, SidewinderFactory
from db import models

Mazes = models.Mazes


class GenerationTypes:
    class GenerationTypesEnum(Enum):
        RECURSIVEBACKTRACKING = "RecursiveBacktracking"
        SIDEWINDER = "Sidewinder"

    def is_type_valid(self, type):
        return type in self.GenerationTypesEnum.__members__.values()


class InputValidation:
    def validate(self, maze_size, type):
        if maze_size > 30 or maze_size < 4:
            return False
        if GenerationTypes().is_type_valid(type):
            return False
        return True


class MazeGenerator:
    def generate_maze(self, maze_size, type):
        if type == "RecursiveBacktracking":
            maze_generator = RecursiveBacktrackingFactory().create_generator()
        elif type == "Sidewinder":
            maze_generator = SidewinderFactory().create_generator()

        maze = maze_generator.generate(int(maze_size))
        return maze


class MazeImageDrawer:
    def __init__(self):
        self.cell_size = 100
        self.cell_border = 10

    def generate_maze_image(self, maze):
        width = maze.width
        height = maze.height
        cells = maze.structure
        img = Image.new(
            "RGBA",
            (width * self.cell_size,
             height * self.cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)
        for row in range(height):
            for column in range(width):
                cell = cells[row][column]

                left_border = 0 if column != 0 else self.cell_border
                right_border = 0 if column != width-1 else self.cell_border
                top_border = 0 if row != 0 else self.cell_border
                bottom_border = 0 if row != height-1 else self.cell_border

                if cell.west == 1:
                    left_border += self.cell_border
                if cell.north == 1:
                    top_border += self.cell_border
                if cell.east == 1:
                    right_border += self.cell_border
                if cell.south == 1:
                    bottom_border += self.cell_border

                left = column * self.cell_size + left_border
                top = row * self.cell_size + top_border
                right = (column + 1) * self.cell_size - right_border
                bottom = (row + 1) * self.cell_size - bottom_border

                rect = [(left, top), (right, bottom)]

                if maze.structure[row][column].start:
                    draw.rectangle(rect, fill="red")
                elif maze.structure[row][column].goal:
                    draw.rectangle(rect, fill="green")
                else:
                    draw.rectangle(rect, fill="white")
        filename = "maze.png"
        byte_array = BytesIO()
        # use filename in save() for local testing to generate pngs
        # and use byte_array to save it as sendable data
        img.save(byte_array, format="png")
        maze_image_byte_array = byte_array.getvalue()
        maze_image_base_64 = base64.b64encode(
            maze_image_byte_array).decode('utf-8')
        return maze_image_base_64


class NewMaze:
    def __init__(self):
        self.name = None
        self.difficulty = None,
        self.img = None,
        self.structure = None,
        self.height = None,
        self.width = None,
        self.creator = None

    def get_new_maze(self):
        new_maze = Mazes(
            name=self.name,
            difficulty=self.difficulty,
            imgLink=self.img,
            structure=self.structure,
            height=self.height,
            width=self.width,
            creator=self.creator)
        return new_maze


class MazeBuilderInterface(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_difficulty(self, difficulty):
        pass

    @abstractmethod
    def set_img(self, img):
        pass

    @abstractmethod
    def set_structure(self, structure):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_creator(self, creator):
        pass

    @abstractmethod
    def get_maze(self):
        pass


class NewMazeBuilder(MazeBuilderInterface):
    def __init__(self):
        self.maze = NewMaze()

    def set_name(self, name):
        self.maze.name = name
        return self

    def set_difficulty(self, difficulty):
        self.maze.difficulty = difficulty
        return self

    def set_img(self, img):
        self.maze.img = img
        return self

    def set_structure(self, structure):
        self.maze.structure = structure
        return self

    def set_height(self, height):
        self.maze.height = height
        return self

    def set_width(self, width):
        self.maze.width = width
        return self

    def set_creator(self, creator):
        self.maze.creator = creator
        return self

    def get_maze(self):
        return self.maze.get_new_maze()


class NewMazeDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_new_maze(self, name, difficulty, img, structure, height, width, creator):
        self.builder.set_name(name).set_difficulty(difficulty).set_img(img).set_structure(
            structure).set_height(height).set_width(width).set_creator(creator)


class MazeCreationFacade:
    def __init__(self):
        self.maze = None
        self.input_validation = InputValidation()
        self.maze_generator = MazeGenerator()
        self.maze_image_drawer = MazeImageDrawer()

    def get_generated_maze(self, user_id, maze_name, maze_size, type):
        isValid = self.input_validation.validate(maze_size, type)
        if (isValid == False):
            abort(400, "Invalid request")
        self.maze = self.maze_generator.generate_maze(maze_size, type)
        img = self.maze_image_drawer.generate_maze_image(self.maze)

        builder = NewMazeBuilder()
        director = NewMazeDirector(builder)
        director.construct_new_maze(
            name=maze_name, difficulty=self.maze.difficulty.name, img=img, structure=str(self.maze.structure), height=int(self.maze.height), width=int(self.maze.width), creator=user_id)
        new_maze = builder.get_maze()

        return new_maze
