from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from os import environ
from app import config
from flask_migrate import Migrate

DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

db = SQLAlchemy()
migrate = Migrate()

Base = declarative_base()

def recreate_database():
    Base.metadata.drop_all(engine)