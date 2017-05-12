from flask import request
from flask import render_template

from app.main import main_blueprint
from .forms import VotingForm


@main_blueprint.route('/', methods=['get', 'post'])
def index():
    form = VotingForm()
    return render_template('submit.html', form=form)
