import uuid
import pytest

@pytest.fixture
def create_user_payload() -> dict:
    return {
        'name': 'Jonny Greenwood',
        'email': f'{str(uuid.uuid4())}@fender.com',
        'password': 'Password1!'
    }

@pytest.fixture
def update_user_payload() -> dict:
    return {
        'name': 'Ed O\'Brien',
        'email': f'{str(uuid.uuid4())}@fender.com',
        'password': 'Password2!'
    }