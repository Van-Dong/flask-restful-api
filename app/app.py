import os

from flask import Flask, request, Blueprint
from flask_migrate import Migrate

from .extension import db, ma
from .controller import books
from app import models

MIGRATION_DIR = os.path.join(os.path.dirname(__file__), 'migrations')

def create_app(config_file="config.py"):
    app = Flask(__name__, static_folder=None)
    app.config.from_pyfile(config_file)

    with app.app_context():
        # init database
        db.init_app(app)  # để trước register blueprint
        ma.init_app(app)

        app.register_blueprint(books, url_prefix="/")
    Migrate(app, db, directory=MIGRATION_DIR, models=models)
    return app