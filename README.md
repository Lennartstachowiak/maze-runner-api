# Maze runner backend

## Flask

Create a venv in api_folder -> `python3 -m venv venv`
Start venv with -> `source venv/bin/activate`
For flask command set flask with -> `export FLASK_APP=run`
Install packages for virtual enviorment -> `pip install -r requirements.txt`

## Create database

Currently the database is sqlite

migrate should already pre set the database
If not run this command:

- `flask db init`

To create the database locally use:

- `flask db migrate -m 'init'`
- `flask db upgrade`
  This will create a file called: database.db

If no error occured then it should be set, but you can still check it in postman with the endpoint
/get_all

## Scripts to set up the database data

### `python3 -m scripts.addDummyDataMazeDB`

### `python3 -m scripts.addDummyDataAlgorithmsDB`

## Available Scripts

In the project directory, you can run:

### Start development enviormnet: `docker compose up`

### Delete all algorithms for all users: `python3 -m scripts.deleteAlgorithms`

### Delete all mazes: `python3 -m scripts.deleteMazes`
