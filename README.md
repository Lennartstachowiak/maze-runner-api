# Maze runner backend

## Overview

This is the backend for https://github.com/Lennartstachowiak/maze-runner-website.
Here the user authentication and authorisation is handled, the maze and user data is managed, the data is handled with the database, algorithms are executed and mazes are generated.

## Installation

### Flask

Create a virtual enviorment (venv) -> `python3 -m venv venv`
Start venv with -> `source venv/bin/activate`
Install packages for virtual enviorment -> `pip install -r requirements.txt`
For flask commands set flask with -> `export FLASK_APP=run`

## Create database

Migration should already pre set the database

If not run this command:

- `flask db init`

To create the database locally use:

- `flask db migrate -m 'init'`

- `flask db upgrade`

This will create a file called: database.db

## Scripts to set up the database data

`python3 -m scripts.addDummyDataMazeDB`

## Available Scripts

In the project directory, you can run:

#### Start development environment:

`docker compose up`

#### Delete all algorithms for all users:

`python3 -m scripts.deleteAlgorithms`

#### Delete all mazes:

`python3 -m scripts.deleteMazes`
