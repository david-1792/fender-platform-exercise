from typing import Generator
import uuid

import pytest

from app.api.users.models import User
from app.api.login.models import AccessToken

@pytest.fixture
def register_payload() -> Generator[dict, None, None]:
    payload = {
        'name': 'Fender',
        'email': f'{str(uuid.uuid4())}@fender.com',
        'password': 'Password1!'
    }

    yield payload

    user = User.get_by_email(payload['email'])
    user.delete()

    for token in AccessToken.query(user.id):
        token.delete()

@pytest.fixture
def register_invalid_email_payloads(
    valid_credentials: dict
) -> list[dict]:
    return [
        {
            'name': 'Whatever',
            'email': valid_credentials['username'],
            'password': 'whatever'
        },
        {
            'name': 'Whatever',
            'email': 'notanemail',
            'password': 'whatever'
        }
    ]

@pytest.fixture
def register_invalid_password_payloads() -> list[dict]:
    return [
        {
            'name': 'Whatever',
            'email': 'whatever@fender.com',
            'password': '.'
        },
        {
            'name': 'Whatever',
            'email': 'whatever@fender.com',
            'password': '1' * 200
        }
    ]

@pytest.fixture
def update_me_invalid_email_payloads() -> list[dict]:
    return [
        {'email': 'notanemail'},
        {'email': 'notanemail'}
    ]

@pytest.fixture
def update_me_invalid_password_payloads() -> list[dict]:
    return [
        {'password': '.'},
        {'password': '1' * 200}
    ]