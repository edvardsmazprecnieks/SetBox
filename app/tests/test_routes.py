from app.extensions.database.models import User
from app.extensions.database.crud import db
from flask_login import login_user, logout_user

#test for same route
#def test_for_same_route(client):
#    response = client.get('/')
#    assert client.get('/index').data == response.data

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to SetBox!' in response.data

def test_login_success(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_login_content_has_email(client):
    response = client.get('/login')
    assert b'E-mail' in response.data

def test_login_content_has_password(client):
    response = client.get('/login')
    assert b'Password' in response.data

def test_register_success(client):
    response = client.get('/register')
    assert response.status_code == 200

def test_register_content_has_email(client):
    response = client.get('/register')
    assert b'E-mail' in response.data

def test_register_content_has_password(client):
    response = client.get('/register')
    assert b'Password' in response.data

def test_login_required_for_subjects(client):
    response = client.get('/subject')
    assert response.status_code == 401

def test_login_required_for_lessonadder(client):
    response = client.get('/lessonadder')
    assert response.status_code == 401

def test_login_required_for_add_subject(client):
    response = client.get('/add_subject')
    assert response.status_code == 401

def test_register_functionality(client):
    response = client.post('/register', data={
        'email': 'setbox@testing_register.com',
        'password' : 'test_password',
        'password_confirmation' : 'test_password',
        'fname' : 'Setbox'
    }, follow_redirects=True)
    user_query = User.query.filter_by(email="setbox@testing_register.com").all()
    assert len(user_query) == 1
    assert len(response.history) == 1
    assert response.request.path == '/subject'

def test_login_functionality(client):
    user = User(
        email='setbox@testing_login.com',
        first_name='Setbox'
    )
    user.set_password('test_password')
    db.session.add(user)
    db.session.commit()
    response = client.post('/login', data={
        'email': 'setbox@testing_login.com',
        'password' : 'test_password'
    }, follow_redirects=True)
    # NOT WORKING
    assert user.is_authenticated == True
    assert len(response.history) == 1
    assert response.request.path == '/subject'
    

def test_logout_functionality(client):
    user = User(
        email='setbox@testing_logout.com',
        first_name='Setbox'
    )
    user.set_password('test_password')
    db.session.add(user)
    db.session.commit()
    login_user(user)
    # NOT WORKING
    assert user.is_authenticated == True
    response = client.get('/logout', follow_redirects=True)
    # NOT WORKING
    assert user.is_authenticated == False
    assert len(response.history) == 1
    assert response.request.path == '/login'

    

def test_should_return_subject_name():
    user = User(
        email='setbox@testing_logout.com',
        first_name='Setbox'
    )
    user.set_password('test_password')
    

    