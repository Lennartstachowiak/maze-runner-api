from db.db import register_database
from app.routes.maze import register_maze_routes
from app.routes.user import register_user_routes
from app.routes.algorithm import register_algorithm_routes
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
    register_algorithm_routes(api)
    return api


api = create_api()
