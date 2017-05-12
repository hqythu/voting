"""
flask app
"""

from config import configs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from modulefinder import importlib

db = SQLAlchemy()


def create_app(name):
    app = Flask(__name__)
    app.config.from_object(configs[name])

    db.init_app(app)

    main = importlib.import_module('app.main')
    app.register_blueprint(main.main_blueprint)

    return app
