from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

db = SQLAlchemy()

# A migration is like a script that migrates your Python models to the database as tables.
# Each time you make a change, a new migration file is created.
# This way, you can keep track of all the changes that ever happened in
# your application.
migrate = Migrate()


def register_database(api: Flask):
    db.init_app(api)
    migrate.init_app(api, db)


class CRUDMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return
