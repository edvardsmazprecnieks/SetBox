import pytest
from app.app import create_app
from os import environ
from flask_migrate import upgrade
from app.extensions.database.models import db
from sqlalchemy.orm import DeclarativeBase

base = DeclarativeBase()

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite://"
    })

    yield app

@pytest.fixture
def client(app):
    with app.app_context():
        upgrade()
        yield app.test_client()
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()
