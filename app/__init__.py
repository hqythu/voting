"""
flask app
"""
import json
import importlib

from flask import Flask
from flask_redis import FlaskRedis

from config import configs

redis_store = FlaskRedis()


def create_app(name):
    app = Flask(__name__)
    ctx = app.app_context()
    ctx.push()

    app.config.from_object(configs[name])

    redis_store.init_app(app)

    candidates = json.load(open('candidates.json'))
    app.candidates = candidates

    with open('tokens.txt') as f:
        tokens = f.readlines()
        for token in tokens:
            token = token[:-1]
            if not redis_store.sismember('used_token', token):
                redis_store.sadd('unused_token', token)
        redis_store.save()

    main = importlib.import_module('app.main')
    app.register_blueprint(main.main_blueprint)

    return app
