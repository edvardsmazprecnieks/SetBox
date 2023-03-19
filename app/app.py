import os

import psycopg2
from flask import Flask
from . import subjects, lesson, schedule

app = Flask(__name__)
app.config.from_object('app.config')

app.register_blueprint(subjects.routes.blueprint)
app.register_blueprint(lesson.routes.blueprint)
app.register_blueprint(schedule.routes.blueprint)

def get_database_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="setbox",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return connection

