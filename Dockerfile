FROM python:3.6.1-onbuild

ENV FLASK_CONFIG=production

EXPOSE 80

CMD python manage.py run_gunicorn
