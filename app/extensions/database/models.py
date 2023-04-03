from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, Time, VARCHAR, ForeignKey, Boolean, func, UniqueConstraint
from sqlalchemy.orm import column_property
from flask_login import UserMixin

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(VARCHAR(1024), nullable=False)
    first_name = Column(VARCHAR(50), nullable=False)
    
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    owner_user_id = Column(Integer,  ForeignKey('users.id'), nullable=False)
    __table_args__ = (UniqueConstraint('name', 'owner_user_id', name='_name_for_owner'), )

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    date = Column(Date, nullable=False)
    formatted_date = column_property(func.to_char(date, 'dd.mm.yyyy'))
    progress = Column(Integer)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    name = Column(VARCHAR(255))

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    type = Column(VARCHAR(10))
    filename = Column(VARCHAR(255), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lessons.id'), nullable=False)

class UserInSubject(Base):
    __tablename__ = 'users_in_subjects'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    editor = Column(Boolean, nullable=False)