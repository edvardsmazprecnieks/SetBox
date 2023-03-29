from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ
from .models import Base
from app import config

DATABASE_URI = config.DATABASE_URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)