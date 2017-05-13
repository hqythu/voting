import logging

from flask import request
from flask import render_template

from app.main import main_blueprint
from .forms import VotingForm


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = VotingForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.selection.data == '':
                return render_template('result.html', message='请选择正确的项')
            selection = form.selection.data
            token = form.token.data
            print(selection, token, flush=True)
            print('ok', flush=True)
        else:
            print('err', flush=True)
            return render_template('result.html', message='提交的表单填写有误')
    else:
        return render_template('submit.html', form=form)


@main_blueprint.route('/result', methods=['GET'])
def result():
    pass
