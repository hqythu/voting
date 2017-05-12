from flask import Blueprint
from modulefinder import importlib

main_blueprint = Blueprint('main', __name__)

importlib.import_module(f'{__name__}.handler')
