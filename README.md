# Maze Runner Backend

#### Table of Contents

- [Description](#description)
- [Getting Started](#started)
- [Running with Docker (recommended)](#docker)
  - [Prerequisites](#prerequisitesdocker)
  - [Tested versions](#testedversion)
  - [Installation](#installation)
  - [Setting up the environment](#envdocker)
  - [Running the application](#rundocker)
- [Running with Python](#python)
  - [Prerequisites](#prerequisitespython)
  - [Flask](#flask)
  - [Installation](#installationpython)
  - [Create database](#databasepython)
  - [Running the application](#runpython)
- [Available Scripts](#scripts)

## Description <a name="description">

This is the backend for [Maze Runner Website](https://github.com/Lennartstachowiak/maze-runner-website).
The user authentication and authorisation is handled, the maze and user data is managed, the data is handled with the database, algorithms are executed and mazes are generated here.

- The backend is built with [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/3.0.x/).
- For the database creation it uses [SQLAlchamy](https://www.sqlalchemy.org/) as ORM and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) to handle SQLAlchemy database migrations.

# Getting Started <a name="started">

You can run the programm locally in two different ways.

- Running with **Docker** (recommended)
- Running with **Python**

## Running with **Docker** (recommended) <a name="docker">

### Prerequisites <a name="prerequisitesdocker">

- **Docker**
  - It is a platform that allows you to package, distribute, and run applications using containers.

### Tested versions <a name="testedversion">

- **Docker** version 24.0.6, build ed223bc

  - Check with

        docker -v

- **Docker Compose** version v2.22.0-desktop.2

  - Check with:

        docker-compose -v

### Installation <a name="installation">

To use Docker with this project, you'll need to have Docker installed on your system. If you haven't installed Docker yet, follow these steps:

1.  Visit the Docker website: https://www.docker.com

2.  Download the installer for your operating system (e.g., Docker Desktop for Windows, Docker Desktop for macOS, Docker Engine for Linux).

3.  Run the installer and follow the on-screen instructions to complete the installation.

4.  Once the installation is complete, start the Docker application.

> 💡 For detailed installation instructions and system requirements, please refer to the official Docker documentation.

### Setting up the environment <a name="envdocker">

You need to create a `.env` file in the root directory and need to add some PostgreSQL data for the database:

    DATABASE_TYPE=postgres
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=your_db_name

Furthermore you also need to add to `.env`

    SECRET_KEY=your_secret_key
    ALLOW_ORIGIN=http://localhost:*

These keys will be used for encryption and to allow localhost requests.

### Running the application <a name="rundocker">

In root directory run:

    docker compose up

This command will set up everything for you automatically.

**Now you are ready to go!** 🚀

---

## Running with **Python** <a name="python">

### Prerequisites <a name="prerequisitespython">

- Python

### Installation <a name="installationpython">

- Python
  - Check out the official website of python (https://www.python.org/) to install python for your operating system.

### Flask <a name="flask">

#### In root directory (if `venv` already exist skip to step 2):

1.  Create a virtual enviorment (venv):

        python3 -m venv venv

2.  Start venv with:

        source venv/bin/activate

3.  Install packages for virtual enviorment:

        pip install -r requirements.txt

4.  For flask commands set flask with:

        export FLASK_APP=run

    > ⚠️ Needed if you encounter this error `Error: Failed to find Flask application or factory in module 'app'. Use 'app:name' to specify one.`

### Create database <a name="databasepython">

> 💡 We will use a `SQLite` locally with this approach. `PostgreSQL` will be used for docker.

#### Set up enviorment

You need to create a `.env` file in the root directory and need to add the database type:

    DATABASE_TYPE=sqlite
    SECRET_KEY=your_secret_key
    ALLOW_ORIGIN=http://localhost:*

#### Set up database

Migration folder (`/migrations`) for the database structure should already set.

If not run this command:

-     flask db init
-     flask db migrate -m 'init'

To create the database locally use:

-     flask db upgrade

This will create a file called: database.db

#### Changing the database

If you want to modify the db you need to create a migration commit like this:

-     flask db migrate -m 'your changes'

#### Scripts to set up the database data

In the root directory run:

    python3 -m app.scripts.addDummyDataMazeDB

### Running the application <a name="runpython">

    python3 run.py

**Now you are ready to go!** 🚀

---

## Available Scripts <a name="scripts">

In the project directory you can run:

### **Add data**

#### Add dummy data highscores for each maze and user

    python3 -m app.scripts.addDummyDataHighscoresDB

#### Add all example algorithms for a user **(will be done by default already)**:

    python3 -m app.scripts.addDummyDataAlgorithmsDB user_id

#### Add all official mazes to db **(will be done by default already)**:

    python3 -m app.scripts.addDummyDataMazeDB

### **Delete data**

#### Delete all algorithms for all users:

    python3 -m app.scripts.deleteAlgorithms

#### Delete all mazes:

    python3 -m app.scripts.deleteMazes

#### Delete all highscores:

    python3 -m app.scripts.deleteHighscores

#### Delete all expired sessions:

    python3 -m app.scripts.deleteExpiredSessions

#### Delete all user session:

    python3 -m app.scripts.deleteSession user_id
