# Maze Runner Backend

#### Table of Contents

- [Documentation](#documentation)
  - [Overview](#overview)
  - [Diagrams](#diagram)
  - [Controllers](#controllers)
  - [Design Patterns](#design)
- [Getting Started](#started)
  - [Running with Docker (recommended)](#docker)
    - [Prerequisites](#prerequisitesdocker)
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
- [Relational Database](#database)
  - [Database Queries](#databasequeries)
- [Security](#security)
  - [List of cyber security measures](#measures)
  - [Thread Models](#thread)
    - [List of Security Vulnerabilities and Weaknesses](#vulnerabilities)

---

# Documentation <a name="documentation"></a>

## Overview <a name="overview"></a>

Here is the link to the hosted website of [Maze Runner](https://maze-runner-website.vercel.app/).

This is the backend for [Maze Runner Website](https://github.com/Lennartstachowiak/maze-runner-website).

- Maze Runner is a application on which users can compete against each other by creating algorithms to solve mazes.
- Each successful solution path from the start to the goal will be added to the highscore list.
- Users can generate new mazes which they own and can practice with.
- Algorithms can directly be created and edited in the application and can be tested while writing the code.
  - Errors will be shown as well.

The user authentication and authorisation is handled, the maze and user data is managed, the data is handled with the database, algorithms are executed and mazes are generated here.

### Tech Stack

- The backend is built with [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/3.0.x/).
- The database is [PostgreSQL](https://www.postgresql.org/) and it uses [SQLAlchamy](https://www.sqlalchemy.org/) as ORM and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) to handle SQLAlchemy database migrations.

### Project Structure / Diagram <a name="diagram"></a>

#### Structure - C4 Diagram

|                     [Context Diagram](images/1_mms_overview.png)                      |                    [Container Diagram](images/2_application_overview.png)                    |
| :-----------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------: |
|    <img src="images/1_mms_overview.png" alt="User Overview" style="width: 160%;">     | <img src="images/2_application_overview.png" alt="Application Overview" style="width: 60%;"> |
|                  [Component Diagram](images/3_backend_overview.png)                   |                       [Code Diagram](images/4_backend_controller.png)                        |
| <img src="images/3_backend_overview.png" alt="Backend Overview" style="width: 120%;"> |   <img src="images/4_backend_controller.png" alt="Backend Controller" style="width: 80%;">   |

#### Maze Creation - UML Class Diagram

> 💡 Smaller Diagrams of each Design Pattern can be find [here](#design)

<img src="images/maze_creation_class_diagram.png" alt="Maze Creation class diagram">

## Controllers <a name="controllers"></a>

> 💡 Orchestrating Application Flow and User Interactions

<img src="images/5_backend_controller_path.png" alt="Code Diagram with path" style="width: 70%;">

### User

These are controller which handle user related tasks.

- [Login Controller](app/controller/user/login_controller.py)
  - Allow users to sign in to application.
- [Register Controller](app/controller/user/register_user_controller.py)
  - Allow users to register to application.
- [Logout Controller](app/controller/user/logout_controller.py)
  - Allow users to log out of application.
- [Authentication Controller](app/controller/user/get_user_controller.py)
  - Authenticats user with session cookie.
- [Session Controller](app/controller/user/session_controller.py)
  - Creates a new session for a user with expiry date and deletes old sessions.

### Maze

These are controller which handle maze related tasks. From fetching mazes to generate new mazes and solving them.

- [Get Mazes Controller](app/controller/maze/get_mazes_controller.py)
  - Fetches all official mazes.
- [Get Single Maze Controller](app/controller/maze/get_single_maze_controller.py)
  - Fetches one specific maze.
  - This can be a user own maze or an official maze.
- [Get User Mazes Contoller](app/controller/maze/get_my_mazes_controller.py)
  - Fetches all mazes of the user.
- [Get Maze Solution Controller](app/controller/maze/get_maze_algorithm_solution_controller.py)
  - Handles to generate the solution for a maze and the given user algorithm.
- [Generate Maze Controller](app/controller/maze/generate_maze_controller.py)
  - Allows users to generate their own mazes.
- [Delete Maze Controller](app/controller/maze/delete_maze_controller.py)
  - Allows users to delete their own mazes.
- [Add Maze Highscore Controller](app/controller/maze/add_maze_highscore.py)
  - Adding the score achieved by users on mazes with their alogrithms.
- [Remove Maze Highscore Controller](app/controller/maze/remove_maze_highscore.py)
  - Removes user highscore if the user achieves a better score with another algorithm.

### Algorithm

These are controller which handle algorithm related tasks. A algorithm can be newly created or changes can be saved.

- [Get Algorithms Controller](app/controller/algorithm/get_algorithms_controller.py)
  - Fetches all users algorithms.
- [Get Single Algorithm Controller](app/controller/algorithm/get_single_algorithm_controller.py)
  - Fetches one specific algorithm of the user.
- [Add New Algorithm Controller](app/controller/algorithm/add_new_algorithm_controller.py)
  - Creates a new algorthm for the user.
- [Delete Algorithm Controller](app/controller/algorithm/delete_algorithm_controller.py)
  - Deletes a existing algorihm of the user.
- [Rename Algorithm Controller](app/controller/algorithm/rename_algorithm_controller.py)
  - Renames an user algorithm for the user.
- [Save Algorithm Controller](app/controller/algorithm/save_algorithm_controller.py)
  - Saves changes made to the algorithm.

## Design Patterns <a name="design"></a>

### Abstract Factory Method

I created a [MazeGeneratorFactory](app/models/maze/maze_generator_factory.py) and two Factories ([SidewinderFactory](app/models/maze/maze_generator_factory.py), [RecursiveBacktrackingFactory](app/models/maze/maze_generator_factory.py)).

The factories are used in the file [generate_maze.py](app/models/maze/generate_maze.py) in the class `MazeGenerator` (line 29).

<img src="images/abstract_factory_method.png" alt="Abstract Factory Method" style="width: 70%;">

### Builder

I created a [NewMazeBuilder](app/models/maze/generate_maze.py) and a [NewMazeDirector](app/models/maze/generate_maze.py) to build a [NewMaze](app/models/maze/generate_maze.py).

<img src="images/builder_pattern.png" alt="Builder Pattern" style="width: 70%;">

I created a simple [UserBuilder](app/models/user/register_user.py) which created the user at the registration.

### Facade

I created a [MazeCreationFacade](app/models/maze/generate_maze.py) which simplifies the usage of the underlying subsystems by providing a higher-level and more user-friendly interface to create a maze.

<img src="images/facade_pattern.png" alt="Facade Pattern" style="width: 70%;">

### Model-View-Controller (MVC)

I created a MVC architectural structure for the backend application.

- View = [Routes](app/routes)
- Controller = [Controllers](app/controller)
- Model = [Models](app/models)

---

# Getting Started <a name="started"></a>

You can run the programm locally in two different ways.

- Running with **Docker** (recommended)
- Running with **Python**

## Running with **Docker** (recommended) <a name="docker"></a>

### Prerequisites <a name="prerequisitesdocker"></a>

- **Docker**
  - It is a platform that allows you to package, distribute, and run applications using containers.

#### Tested versions <a name="testedversion"></a>

- **Docker** version 24.0.6, build ed223bc

  - Check with

        docker -v

- **Docker Compose** version v2.22.0-desktop.2

  - Check with:

        docker-compose -v

### Installation <a name="installation"></a>

To use Docker with this project, you'll need to have Docker installed on your system. If you haven't installed Docker yet, follow these steps:

1.  Visit the Docker website: https://www.docker.com

2.  Download the installer for your operating system (e.g., Docker Desktop for Windows, Docker Desktop for macOS, Docker Engine for Linux).

3.  Run the installer and follow the on-screen instructions to complete the installation.

4.  Once the installation is complete, start the Docker application.

> 💡 For detailed installation instructions and system requirements, please refer to the official Docker documentation.

### Setting up the environment <a name="envdocker"></a>

You need to create a `.env` file in the root directory and need to add some PostgreSQL data for the database:

    DATABASE_TYPE=postgres
    POSTGRES_USER=your_username
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=your_db_name

Furthermore you also need to add to `.env`

    SECRET_KEY=your_secret_key
    ALLOW_ORIGIN=http://localhost:3000

These keys will be used for encryption and to allow localhost requests.

### Running the application <a name="rundocker"></a>

In root directory run:

    docker compose up

This command will set up everything for you automatically.

**Now you are ready to go!** 🚀

---

## Running with **Python** <a name="python"></a>

### Prerequisites <a name="prerequisitespython"></a>

- Python

### Installation <a name="installationpython"></a>

- Python
  - Check out the official website of python (https://www.python.org/) to install python for your operating system.

### Flask <a name="flask"></a>

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

### Create database <a name="databasepython"></a>

> 💡 We will use a `SQLite` locally with this approach. `PostgreSQL` will be used for docker.

#### Set up enviorment

You need to create a `.env` file in the root directory and need to add the database type:

    DATABASE_TYPE=sqlite
    SECRET_KEY=your_secret_key
    ALLOW_ORIGIN=http://localhost:3000

If you get an error by setting up the database, make sure to run:

    source .env

#### Set up database <a name="migration"></a>

Migration folder (`/migrations`) for the database structure should already exist.

If not, run this command:

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

### Running the application <a name="runpython"></a>

    python3 run.py

**Now you are ready to go!** 🚀

---

## Available Scripts <a name="scripts"></a>

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

---

# Clean Code <a name="cleancode"></a>

### Readability and Cleanliness

- I use snake case for variables, methods and function names
  - [app/models/maze/get_single_highscore.py](app/models/maze/get_single_highscore.py)
- I use pascal case for class names
  - [app/models/maze/maze_generator_factory.py](app/models/maze/maze_generator_factory.py)
- Every function explains what it does and every dependency describes what it is (Intention is given):
  - [app/models/user/register_user.py](app/models/user/register_user.py)
  - [app/models/maze/delete_maze.py](app/models/maze/delete_maze.py)
- DRY principle is followed
  - For example `get_single_maze` is used always if a function tries to get a maze by its id ([app/models/maze/get_single_maze.py](app/models/maze/get_single_maze.py), [app/models/maze/get_followed_mazes.py](app/models/maze/get_followed_mazes.py))
- For better understanding what complex methods are doing I used DocStrings as well as for all API endpoints
  - [app/models/maze/maze.py](app/models/maze/maze.py)
  - [app/routes/user.py](app/routes/user.py)

### Clear separation of concerns and well structured

- Function, methods and classes are doing one thing and are folloing the Single-Responsibility Principle
  - Examples:
    - [maze_generator_factory](app/models/maze/maze_generator_factory.py)
    - [generate_maze](app/models/maze/generate_maze.py)
  - In maze generator factory can also be seen that each method has few arguments as well
- The functions are able to test and that can be seen in the [tests folder](tests/)
- Errors are handled and are also returned to the user
  - Error thrown if mistake:
    - [Getting user example](app/models/user/get_user.py)
    - [Maze conflict example](app/controller/maze/generate_maze_controller.py)
  - Error handeling in endpoints:
    - [Error validation](app/routes/validation.py)

### Tools (analysis, styling and formatting)

#### Formatting

For formatting I use [black](https://github.com/psf/black).
It runs before every commit and formates the code if it doesn't agree to the configuration format. If black does a change the commit fails and changes have to be reviewed for another commit try.

#### Style checking

[flake8](https://github.com/PyCQA/flake8) is checking if the code follows the PEP8 (Python) style to assure quality of the code. This also runs before every commit and fails if commit has a style conflict.
flake8 also runs again in an github action after the commit for Pull Requests. A Pull Request can only be merged if the actions pass.

### Refactoring Workflow

Example:

- Maze Solver
  - Added tests (Commit: 624a6c6)
  - Refactor code (Commit: 539b5a1)

---

# Relational Database <a name="database"></a>

<img src="db/erd.png" alt="Entity Realtionship Diagram">

- In the ERD can be seen that the database in normalized
  - No data is duplicated
  - Relationship between tables

The set up of the database can be found in the db/ folder.

The [db.py](db/db.py) file is used to register the database in the project.

In [db/models.py](db/models.py) are all the models for the database which are managed by SQLAlchamy an ORM.
The database includes tables like Users, SessionAuth, Mazes, Highscores, Algorithms, MazeFollowers, and UserFollowers, holding user info, session details, mazes, scores, and follower connections.
Every table has constraints to prevent mistakes at the creation, like unique email or names or duplicated followers.

For managing my database over time I also use [migrations](migrations). The migration can be found in migrations folder. Migrations is used as a version control system for the database to upgrade or downgrade the db.
The scripts for that are explained in the documentation section about [setting up the database](#migration)

### Testing and quering to the database

To see how the database can be queried there are some test created for demonstration.

#### Tests

- [test_db](tests/integration_tests/test_db.py) is having some test to query to the db.
  - Creating a new entry in the db and quering it for User, Maze and Algorithm
  - Database is SQLite and only created during the test and doesn't interfere with the production or development database
- [create_test_data](tests/integration_tests/create_test_data.py) is used to create dummy data for testing and also demonstrated how do create data to the database

#### Queries <a name="databasequeries"></a>

Database queries can be found in the files of the models folder.
Queries for each table:

##### Mazes

- [Create new maze in db](app/models/maze/add_maze.py)
- [Delete maze](app/models/maze/delete_maze.py)
- [Search for maze is available by name](app/models/maze/check_if_maze_available.py)
- [Get official mazes (not generated by users)](app/models/maze/get_mazes_objects.py)
- [Get user generated mazes by id](app/models/maze/get_my_mazes_objects.py)
- [Get a sinlge maze by id](app/models/maze/get_single_maze.py)

##### Highscores

- [Create new highscore for maze in db](app/models/maze/add_maze_highscore.py)
- [Delete highscore in db](app/models/maze/delete_highscore.py)
- [Get single highscore by id](app/models/maze/get_single_highscore.py)

##### Highscores & Users & Algorithm (Join)

- [Get maze highscores by maze id](app/models/maze/get_maze_highscores.py)

##### MazeFollowers

- [Follow maze as user](app/models/maze/follow_maze.py)

##### MazeFollowers & Mazes (Join)

- [Get user followed mazes](app/models/maze/get_followed_mazes.py)

##### Algorithms

- [Create a new algorithm to the database](app/models/algorithm/add_new_algorithm.py)
- [Rename a algorithm (update data)](app/models/algorithm/rename_algorithm.py)
- [Delete algorithm in db](app/models/algorithm/delete_algorithm.py)
- [Get algorithms by user id](app/models/algorithm/get_algorithms.py)
- [Update algorithm](app/models/algorithm/save_algorithm.py)

##### Users

- [Get user for login](app/models/user/login_user.py)
- [Create user for registrations](app/models/user/register_user.py)
- [Search for user with email](app/models/user/search_users.py)

##### UserFollowers

- [Follow a user](app/models/user/follow_user.py)

##### UserFollowers & Users (Join)

- [Get a following list of user](app/models/user/get_user_following.py)
- [Get followers of user](app/models/user/get_user_followers.py)

##### SessionAuth & Users (Join)

- [Get user by session](app/models/user/get_user.py)

##### SessionAuth

- [Remove sesstion (for login or expired)](app/models/user/remove_session.py)
- [Create new session (login or registration)](app/models/user/handle_session.py)
- [Add session to db](app/models/user/add_session.py)

##### Test database queries

- [Create test data](tests/integration_tests/create_test_data.py)
- [Test db and query db for tests](tests/integration_tests/test_db.py)

### Performance

I optimized the quering of data by indexing typical data points. That can be see on the ERD or in [db/models.py](db/models.py).

Furthermore, I created joins to not query multiple times for some data from different tables.

- [get_followed_mazes](app/models/maze/get_followed_mazes.py) is joining Maze data and Maze follower data.
- [get_maze_highscores](app/models//maze/get_maze_highscores.py) is joining User, Algorithm, and Highscore tables.
- [get_user_highscore](app/models/maze/get_user_highscore.py) is joining User, Maze, Algorithm and Highscore tables.

### Database Security

The database is secure against SQL Injections through the use of SQLAlchamy.

The production database is creating backups everyday to prevent data loss.

### Data

The data currently is limited and is generated by users who register theirself and creata algorithm, mazes and follow each user.

Official data is created during the setup of the database automatically for production and development by using the [script to create dummy data](app/scripts/addDummyDataMazeDB.py). The use can be seen in the [docker file](docker-compose.yaml) (line 28).

Generating data is also covered in the documentation section about the [scripts](#scripts).

---

# Security <a name="security"></a>

The following parts are security measures for the **backend application** here as well as for the [**frontend application**](https://github.com/Lennartstachowiak/maze-runner-website).

## List of cyber security measures <a name="measures"></a>

- **CORS** Allow-Origin: Controls and restricts access to resources from different origins.
- **Request Origin** Header check at endpoints: Verifies the request's origin header to prevent unauthorized cross-origin requests.
- Cookie with **httponly** attribute: Prevents JavaScript access to the cookie, reducing the risk of session hijacking and unauthorized account access.
- Cookie with **secure** attribute: Ensures that the cookie is transmitted only over secure and encrypted HTTPS connections.
- Backend and frontend hosted on **HTTPS**: Both the backend and frontend are hosted using HTTPS for secure communication.
- Password is **hashed and salted**: Passwords are securely encrypted using a hash function and unique salts for increased security.
- Authentication: Users are required to create and **secure passwords**.

## Thread Models <a name="thread"></a>

![Thread Model Table](images/thread_model_table.png)

![Thread Model](images/thread_model.png)

### List of Security Vulnerabilities and Weaknesses <a name="vulnerabilities"></a>

The following list is partly already included in the upper diagram. The diagram was created with help with the following bulletpoints:

- SQL Injections and stored XSS
- Lack of two-factor authentication for password-based authentication
- Insufficient input sanitization:
  - Failure to validate and restrict user input based on expected format (e.g., allowing only alphanumeric characters)
  - Pain points in my application:
    - Username and algorithm name inputs
    - Code in algorithms
- Insufficient output encoding:
  - Failure to encode user-generated content before displaying it in HTML or JavaScript contexts
- DDoS or DoS vulnerability
- Elevation of Privilege:
  - Possible to access other user mazes by manipulating the URL ID
- Lack of logging of the identity of the caller
