import os

import psycopg2
from flask import Flask
from . import subjects, lesson, schedule

# def schedule():
#     Maths = [
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 1, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0]
#     ]
   
#     for list in Maths:
#         hour = 8
#         color = f"color{hour}"
#         for n in list:
#             daycounter = 0
#             if n >= 0:
#                 if daycounter == 0:
#                     color = f"color{daycounter}m"
#                 elif daycounter == 1:
#                     color = f"color{daycounter}tu"
#                 elif daycounter == 2:
#                     color = f"color{daycounter}w"
#                 elif daycounter == 3:
#                     color = f"color{daycounter}th"
#                 elif daycounter == 4:
#                     color = f"color{daycounter}f"
#                 else: 
#                     color = ""
#             daycounter += 1
#         hour += 1
#         colorwithstyle = "style='background: blue'"



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
