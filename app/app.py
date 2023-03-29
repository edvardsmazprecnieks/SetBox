import os

import psycopg2
from flask import Flask
from . import subjects, lesson, schedule

# def schedule():
#     timeidentifier = ['color8m', 'color8tu', 'color8w', 'color8th', 'color8f', 'color9m', 'color9tu', 'color9w', 'color9th', 'color9f', 'color10m', 
#                   'color10tu', 'color10w', 'color10th', 'color10f', 'color11m', 'color11tu', 'color11w', 'color11th', 'color11f', 'color12m',
#                   'color12tu', 'color12w', 'color12th', 'color12f', 'color13m', 'color13tu', 'color13w', 'color13th', 'color13f', 'color14m',
#                   'color14tu', 'color14w', 'color14th', 'color14f', 'color15m', 'color15tu', 'color15w', 'color15th', 'color15f', 'color16m',
#                   'color16tu', 'color16w', 'color16th', 'color16f', 'color17m', 'color17tu', 'color17w', 'color17th', 'color17f']

#     "style='background: blue'"

def get_database_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="setbox",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )
    return connection


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(subjects.routes.blueprint)
    app.register_blueprint(lesson.routes.blueprint)
    app.register_blueprint(schedule.routes.blueprint)
