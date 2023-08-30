from db.db import register_database, db, migrate
from routes.maze import register_maze_routes
from routes.user import register_user_routes
from flask import Flask
from flask_cors import CORS
from config import Config


def create_api():
    api = Flask(__name__)
    CORS(api, supports_credentials=True)
    api.config.from_object(Config)
    register_database(api)
    register_user_routes(api)
    register_maze_routes(api)
    return api


api = create_api()
