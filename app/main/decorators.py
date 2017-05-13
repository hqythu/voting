from datetime import datetime
from datetime import timezone
from datetime import timedelta
import functools

from flask import request
from flask import render_template


def time_limits(start_time, end_time,
                start_time_message=None,
                end_time_message=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.now(tz=timezone(timedelta(hours=8)))
            print(now, flush=True)
            if start_time is not None and now < start_time:
                return render_template('message.html',
                                       message=start_time_message)
            if end_time is not None and now > end_time:
                return render_template('message.html', message=end_time_message)
            return func(*args, **kwargs)

        return wrapper

    return decorator
