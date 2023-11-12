# Maze runner backend

## Description

This is the backend for https://github.com/Lennartstachowiak/maze-runner-website.
Here the user authentication and authorisation is handled, the maze and user data is managed, the data is handled with the database, algorithms are executed and mazes are generated.

# Getting Started

You can run the programm locally in two different ways.

- Running with **Docker** (recommended)
- Running with **Python**

## Running with **Docker** (recommended)

### Prerequisites

- **Docker**
  - It is a platform that allows you to package, distribute, and run applications using containers.

### Installation

To use Docker with this project, you'll need to have Docker installed on your system. If you haven't installed Docker yet, follow these steps:

1.  Visit the Docker website: https://www.docker.com

2.  Download the installer for your operating system (e.g., Docker Desktop for Windows, Docker Desktop for macOS, Docker Engine for Linux).

3.  Run the installer and follow the on-screen instructions to complete the installation.

4.  Once the installation is complete, start the Docker application.

        💡 For detailed installation instructions and   system requirements, please refer to the official Docker documentation.

### Setting up the environment

You need to create a `.env` file in the root directory and need to add some PostgreSQL data for the database:

- `POSTGRES_USER=your_username`
- `POSTGRES_PASSWORD=your_password`
- `POSTGRES_DB=your_db_name`

Furthermore you also need to add to `.env`

- `SECRET_KEY=your_secret_key`

This key will be used for encryption of sessions and cookies.

### Running the application

In root directory run:

`docker compose up`

This command will set up everything for you automatically.

**Now you are ready to go!**

---

---

## Running with **Python**

### Prerequisites

- Python
- pip

### Installation

Check out the official website of python (https://www.python.org/) to install python for your operating system.

### Flask

#### In root directory (if `venv`` already exist skip to step 3):

1. Create a virtual enviorment (venv) -> `python3 -m venv venv`

2. Start venv with -> `source venv/bin/activate`

3. Install packages for virtual enviorment -> `pip install -r requirements.txt`

4. For flask commands set flask with -> `export FLASK_APP=run`

### Create database

Migration should already pre set the database

If not run this command:

- `flask db init`

To create the database locally use:

- `flask db migrate -m 'init'`

- `flask db upgrade`

This will create a file called: database.db

### Scripts to set up the database data

`python3 -m scripts.addDummyDataMazeDB`

### Start project

`docker compose up`

### Available Scripts

In the project directory, you can run:

#### Start development environment:

`docker compose up`

#### Delete all algorithms for all users:

`python3 -m scripts.deleteAlgorithms`

#### Delete all mazes:

`python3 -m scripts.deleteMazes`
