from typing import Generator
import uuid

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.auth import get_password_hash

from app.api.users.models import User
from app.api.login.models import AccessToken

@pytest.fixture(scope='session')
def client() -> TestClient:
    return TestClient(app)

@pytest.fixture
def valid_credentials() -> Generator[dict, None, None]:
    user_id = str(uuid.uuid4())
    user_password = 'Password1!'

    user = User(
        PK='USER',
        SK=f'USER#{user_id}',
        _TYPE='USER',
        id=user_id,
        name='Test User',
        email=f'{user_id}@fender.com',
        password_hash=get_password_hash(user_password)
    )

    user.save()

    yield {
        'username': user.email,
        'password': user_password
    }

    user.delete()
    for token in AccessToken.query(user.id):
        token.delete()

@pytest.fixture
def valid_token(
    client: TestClient,
    valid_credentials: dict
) -> str:
    response = client.post(
        '/api/login',
        data=valid_credentials
    )
    
    assert response.status_code == 200
    return response.json()['access_token']

@pytest.fixture
def invalid_token() -> str:
    return 'invalidtoken'

@pytest.fixture
def invalid_credentials() -> list[dict]:
    return [
        {
            'username': 'wrong@fender.com',
            'password': 'Password1!'
        },
        {
            'username': 'test@fender.com',
            'password': 'wrongpassword'
        }
    ]