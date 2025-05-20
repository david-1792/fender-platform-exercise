
from fastapi.testclient import TestClient

# POST /login
def test_login(
    client: TestClient,
    valid_credentials: dict
) -> None:
    response = client.post(
        '/api/login',
        data=valid_credentials
    )

    assert response.status_code == 200
    assert response.json()['access_token']

def test_login_invalid_credentials(
    client: TestClient,
    invalid_credentials: list[dict]
) -> None:
    for credentials in invalid_credentials:
        response = client.post(
            '/api/login',
            data=credentials
        )

        assert response.status_code == 401

# POST /users/register
def test_register(
    client: TestClient,
    register_payload: dict
) -> None:
    response = client.post(
        '/api/users/register',
        json=register_payload
    )

    assert response.status_code == 204
    
def test_register_invalid_email(
    client: TestClient,
    register_invalid_email_payloads: dict
) -> None:
    for payload in register_invalid_email_payloads:
        response = client.post(
            '/api/users/register',
            json=payload
        )

        assert response.status_code in (400, 422)

def test_register_invalid_password(
    client: TestClient,
    register_invalid_password_payloads: dict
) -> None:
    for payload in register_invalid_password_payloads:
        response = client.post(
            '/api/users/register',
            json=payload
        )

        assert response.status_code in (400, 422)

# GET /users/me
def test_me(
    client: TestClient,
    valid_token: str
) -> None:
    response = client.get(
        '/api/users/me',
        headers={'Authorization': f'Bearer {valid_token}'}
    )

    assert response.status_code == 200
    assert response.json()['id']

def test_me_invalid_token(
    client: TestClient,
    invalid_token: str
) -> None:
    response = client.get(
        '/api/users/me',
        headers={'Authorization': f'Bearer {invalid_token}'}
    )
    
    assert response.status_code == 401

# PATCH /users/me
def test_update_me(
    client: TestClient,
    valid_token: str
) -> None:
    response = client.patch(
        '/api/users/me',
        headers={'Authorization': f'Bearer {valid_token}'},
        json={'name': 'I updated the name'}
    )

    assert response.status_code == 200
    assert response.json()['name'] == 'I updated the name'

def test_update_me_invalid_token(
    client: TestClient,
    invalid_token: str
) -> None:
    response = client.patch(
        '/api/users/me',
        headers={'Authorization': f'Bearer {invalid_token}'},
        json={'name': 'I updated the name'}
    )

    assert response.status_code == 401

def test_update_me_invalid_email(
    client: TestClient,
    valid_token: str,
    update_me_invalid_email_payloads: dict
) -> None:
    for payload in update_me_invalid_email_payloads:
        response = client.patch(
            '/api/users/me',
            headers={'Authorization': f'Bearer {valid_token}'},
            json=payload
        )

        assert response.status_code in (400, 422)

def test_update_me_invalid_password(
    client: TestClient,
    valid_token: str,
    update_me_invalid_password_payloads: dict
) -> None:
    for payload in update_me_invalid_password_payloads:
        response = client.patch(
            '/api/users/me',
            headers={'Authorization': f'Bearer {valid_token}'},
            json=payload
        )

        assert response.status_code in (400, 422)

# DELETE /users/me
def test_delete_me(
    client: TestClient,
    valid_token: str
) -> None:
    response = client.delete(
        '/api/users/me',
        headers={'Authorization': f'Bearer {valid_token}'}
    )

    assert response.status_code == 204

def test_delete_me_invalid_token(
    client: TestClient,
    invalid_token: str
) -> None:
    response = client.delete(
        '/api/users/me',
        headers={'Authorization': f'Bearer {invalid_token}'}
    )
    
    assert response.status_code == 401

# POST /logout
def test_logout(
    client: TestClient,
    valid_token: str
) -> None:
    response = client.post(
        '/api/logout',
        headers={'Authorization': f'Bearer {valid_token}'}
    )
    
    assert response.status_code == 204

def test_logout_invalid_token(
    client: TestClient,
    invalid_token: str
) -> None:
    response = client.post(
        '/api/logout',
        headers={'Authorization': f'Bearer {invalid_token}'}
    )
    
    assert response.status_code == 401
