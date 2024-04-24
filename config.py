from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    if environ.get("FLASK_ENV") == "production":
        SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")

    elif environ.get("DATABASE_TYPE") == "sqlite":
        SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

    elif environ.get("DATABASE_TYPE") == "postgres":
        POSTGRES_USER = environ.get("POSTGRES_USER")
        POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
        POSTGRES_DB = environ.get("POSTGRES_DB")
        SQLALCHEMY_DATABASE_URI = f"""postgresql://{POSTGRES_USER}:{
            POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"""

    else:
        raise ValueError("Invalid value for FLASK_ENV")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = environ.get("SECRET_KEY")

    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    # SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
