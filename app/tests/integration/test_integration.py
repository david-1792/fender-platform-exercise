
from fastapi.testclient import TestClient

def test_happy_path(
    client: TestClient,
    create_user_payload: dict,
    update_user_payload: dict
) -> None:
    
    # Register a new user
    response = client.post(
        '/api/users/register',
        json=create_user_payload
    )

    assert response.status_code == 204
    
    # Login with the new user
    response = client.post(
        '/api/login',
        data={
            'username': create_user_payload['email'],
            'password': create_user_payload['password']
        }
    )

    assert response.status_code == 200

    # Set the Authorization header
    client.headers['Authorization'] = f'Bearer {response.json()['access_token']}'

    # Get the user details
    response = client.get('/api/users/me')

    assert response.status_code == 200
    assert response.json()['name'] == create_user_payload['name']

    # Update the user details
    response = client.patch(
        '/api/users/me',
        json=update_user_payload
    )

    assert response.status_code == 200

    # Get the updated user details
    response = client.get('/api/users/me')

    assert response.status_code == 200
    assert response.json()['name'] == update_user_payload['name']

    # Log out
    response = client.post('/api/logout')
    assert response.status_code == 204

    # Log back in with the updated user
    response = client.post(
        '/api/login',
        data={
            'username': update_user_payload['email'],
            'password': update_user_payload['password']
        }
    )

    assert response.status_code == 200

    # Set the Authorization header
    client.headers['Authorization'] = f'Bearer {response.json()["access_token"]}'

    # Delete the user
    response = client.delete('/api/users/me')
    assert response.status_code == 204