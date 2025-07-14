import pytest
from app import create_app
from models import db, Course

import pytest
from app import create_app
from models import db, Course

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'


    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.add(Course(title="Test Course"))
            db.session.commit()
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test Course" in response.data
