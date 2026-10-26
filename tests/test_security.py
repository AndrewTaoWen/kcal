import os
import sys
import re
import pytest
from pathlib import Path

os.environ['SECRET_KEY'] = 'test-secret-not-for-production'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from calculator import app, db
from calculator.models import User

@pytest.fixture(autouse=True)
def isolated_database():
    with app.app_context():
        db.create_all()
    yield
    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_security_upgrade_preserves_pages_and_csrf():
    with app.test_client() as client:
        for url in ['/', '/budget', '/intake', '/expenditure', '/register', '/login']:
            response = client.get(url)
            assert response.status_code == 200, (url,response.status_code)
        response = client.post('/register', data={'username':'alice','email_address':'alice@example.com','password1':'long-secret','password2':'long-secret'})
        assert response.status_code == 200
        assert b'User has been created' not in response.data

def test_password_hashing_and_verification():
    with app.app_context():
        user=User(username='alice',email_address='alice@example.com',password='long-secret')
        assert user.password_hash != 'long-secret'
        assert user.check_password_correction('long-secret')
        assert not user.check_password_correction('incorrect')

def test_fresh_database_cli():
    result = app.test_cli_runner().invoke(args=['init-db'])
    assert result.exit_code == 0
    with app.app_context():
        assert User.query.count() == 0


def test_registration_and_login_with_csrf():
    def token(response):
        return re.search(rb'name="csrf_token"[^>]*value="([^"]+)"', response.data).group(1).decode()
    with app.test_client() as client:
        csrf=token(client.get('/register'))
        result=client.post('/register',data={'csrf_token':csrf,'username':'alice','email_address':'alice@example.com','password1':'long-secret','password2':'long-secret'})
        assert result.status_code==302
        with app.app_context():
            assert User.query.filter_by(username='alice').one().check_password_correction('long-secret')
        client.get('/logout')
        csrf=token(client.get('/login'))
        assert client.post('/login',data={'csrf_token':csrf,'username':'alice','password':'long-secret'}).status_code==302
