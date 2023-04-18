import flask_testing
from unittest.mock import patch, Mock
from app.app import create_app
from app.extensions.database.models import User, Subject
from app.extensions.database.crud import db
from flask_login import FlaskLoginClient, login_user

class TestSubjectsRoutesSimple(flask_testing.TestCase):
    TESTING = True

    def create_app(self):
        return create_app()
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.test_client_class = FlaskLoginClient

    def test_subject_adding_page(self):
        response = self.client.get('/add_subject')
        # checks if need to be logged in
        assert response.status_code == 401

class TestSubjectsRoutesWithDatabase(flask_testing.TestCase):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/setbox_test'
    TESTING = True

    def create_app(self):
        return create_app()
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.test_client_class = FlaskLoginClient
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_subjects_success_with_db(self):
        user = User(
            email = 'test_subjects@setbox.de',
            first_name = 'Testy'
        )
        user.set_password('test_password')
        db.session.add(user)
        db.session.commit()
        subject = Subject(
            name = 'Test Subject',
            owner_user_id = user.id
        )
        db.session.add(subject)
        db.session.commit()
        with self.app.test_client(user=user) as client:
            response = client.get('/subject')
        assert response.status_code == 200
        assert b'Test Subject' in response.data
        

class TestSubjectsRoutesWithMocking(flask_testing.TestCase):
    TESTING = True

    def create_app(self):
        return create_app()
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.test_client_class = FlaskLoginClient

    @patch('app.subjects.routes.current_user')
    @patch('app.subjects.routes.db')
    @patch('app.subjects.routes.Lesson')
    @patch('app.subjects.routes.Subject')
    def test_subject_with_mock(self, mock_subject, mock_lesson, mock_db, mock_current_user):
        mock_current_user.id = 1
        #mock_subject.query.filter.return_value = Mock()
        #mock_subject.query.filter.return_value.first.return_value = Mock()
        mock_subject.query.filter.return_value.first.return_value.owner_user_id = 1
        mock_subject.query.filter.return_value.first.return_value.name = 'Test Subject'
        mock_lesson.query.filter.return_value.all.return_value = [Mock(), Mock()]
        response = self.client.get('/subject/1')
        assert response.status_code == 200
        assert b'Test Subject' in response.data
        assert b'Test Lesson' in response.data