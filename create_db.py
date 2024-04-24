import subprocess
from flask import Flask
from config import Config
from db.db import register_database, db
from flask_migrate import upgrade


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_database(app)
    return app


def database_exists():
    with app.app_context():
        # Perform a check to determine if the database exists
        return db.engine.dialect.has_table(db.engine.connect(), "users")


if __name__ == "__main__":
    app = create_app()
    if not database_exists():
        with app.app_context():
            upgrade(directory="migrations")
            script_command = "python3 -m app.scripts.addDummyDataMazeDB"
            subprocess.run(script_command, shell=True)
