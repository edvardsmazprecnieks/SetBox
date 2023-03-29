from flask import Flask
from . import subjects, lesson, schedule, user, for_database


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(subjects.routes.blueprint)
    app.register_blueprint(lesson.routes.blueprint)
    app.register_blueprint(schedule.routes.blueprint)
    app.register_blueprint(for_database.routes.blueprint)
    app.register_blueprint(user.routes.blueprint)