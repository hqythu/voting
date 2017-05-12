from flask import Blueprint
import importlib

main_blueprint = Blueprint('main', __name__)

importlib.import_module(f'{__name__}.handler')
