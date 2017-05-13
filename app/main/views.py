import logging
from datetime import datetime
from datetime import timezone
from datetime import timedelta

from flask import request
from flask import render_template
from flask import current_app

from app import redis_store
from app.main import main_blueprint
from .forms import VotingForm
from .decorators import time_limits


@main_blueprint.route('/', methods=['GET', 'POST'])
# @time_limits(start_time=None,
#              end_time=datetime(year=2017, month=5, day=13, hour=15, minute=40,
#                                tzinfo=timezone(timedelta(hours=8))),
#              end_time_message='投票已经结束')
def index():
    form = VotingForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.selection.data == '':
                return render_template('message.html', message='请选择正确的项')
            selection = form.selection.data
            token = form.token.data
            if redis_store.sismember('used_token', token):
                return render_template('message.html', message='Token已被使用')
            if not redis_store.sismember('unused_token', token):
                return render_template('message.html', message='不正确的Token')
            pipe = redis_store.pipeline(transaction=True)
            pipe.srem('unused_token', token)\
                .sadd('used_token', token)\
                .incr(selection, amount=1)\
                .execute()
            redis_store.save()
            return render_template('message.html', message='提交成功')
        else:
            return render_template('message.html', message='提交的表单填写有误')
    else:
        return render_template('submit.html', form=form)


@main_blueprint.route('/voted', methods=['GET'])
def voted():
    tokens = redis_store.smembers('used_token')
    return '<br>'.join(map(lambda t: t.decode('utf-8'), tokens))


@main_blueprint.route('/result', methods=['GET'])
# @time_limits(start_time=datetime(year=2017, month=5, day=14, hour=22, minute=00,
#                                  tzinfo=timezone(timedelta(hours=8))),
#              end_time=None,
#              start_time_message='结果尚未公布')
def result():
    res = [(key, redis_store.get(key)) for key in current_app.candidates]
    print(res, flush=True)
    return '<br>'.join(
        map(lambda x: current_app.candidates[x[0]] + ': ' +
                      (x[1].decode('utf-8') if x[1] else '0'), res))
