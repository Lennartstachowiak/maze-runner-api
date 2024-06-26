from app.routes.validation import register_validation
from db.db import register_database
from app.routes.maze import register_maze_routes
from app.routes.user import register_user_routes
from app.routes.algorithm import register_algorithm_routes
from flask import Flask
from flask_cors import CORS
from config import Config
from os import environ
from dotenv import load_dotenv

load_dotenv()


def create_api():
    api = Flask(__name__)
    allow_origin = [environ.get("ALLOW_ORIGIN")]
    CORS(api, supports_credentials=True, origins=allow_origin)
    api.config.from_object(Config)
    register_database(api)
    register_user_routes(api)
    register_maze_routes(api)
    register_algorithm_routes(api)
    register_validation(api)
    return api


api = create_api()
