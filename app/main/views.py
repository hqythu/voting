import logging
from datetime import datetime
from datetime import timezone
from datetime import timedelta

from flask import request
from flask import render_template

from app.main import main_blueprint
from .forms import VotingForm
from .decorators import time_limits


@main_blueprint.route('/', methods=['GET', 'POST'])
@time_limits(start_time=None,
             end_time=datetime(year=2017, month=5, day=13, hour=15, minute=40,
                               tzinfo=timezone(timedelta(hours=8))),
             end_time_message='投票已经结束')
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
@time_limits(start_time=datetime(year=2017, month=5, day=14, hour=22, minute=00,
                                 tzinfo=timezone(timedelta(hours=8))),
             end_time=None,
             start_time_message='结果尚未公布')
def result():
    pass
