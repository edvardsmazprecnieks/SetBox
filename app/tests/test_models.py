from werkzeug.security import generate_password_hash
from app.extensions.database.models import User, Subject, Lesson, File, UserInSubject
from app.extensions.database.crud import db


# Integration tests for testing the models 

# Test if user is saved to the database and generate_password_hash can be saved to the database
def test_save_user(client):
    user = User(
        email = 'testing_new_user@test.com',
        password = generate_password_hash('test_password'),
        first_name = 'Test')
    
    db.session.add(user)
    db.session.commit()

    user_query = User.query.filter_by(email="testing_new_user@test.com").all()
    assert user_query is not None

def test_save_user(client):
    user = User(
        email = 'testing_new_user@test.com',
        password = generate_password_hash('test_password'),
        first_name = 'Test')
    
    db.session.add(user)
    db.session.commit()

    user_query = User.query.filter_by(email="testing_new_user@test.com").all()
    assert user_query is not None


def test_new_user(client):
    #GIVEN a User model
    user = User(
        email = 'testing_new_user@test.com',
        first_name = 'Test')
    user.set_password('test_password')
    #WHEN a new User is created
    #THEN check the email, name, and password fields are defined correctly
    assert user.email == 'testing_new_user@test.com'
    assert user.first_name == 'Test'
    assert user.password != 'test_password'

