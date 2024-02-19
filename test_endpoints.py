from flask import jsonify


# test Flask PyMongo CRUD application with mongomock


def test_create_user(client):
    user_data = {
        'name': 'test',
        'email': 'test@example.com',
    }

    response = client.post('/users/create', json=user_data)
    assert response.status_code == 200
    print(response.json)
    assert response.get_json() == {'Congrats!': 'User created successfully'}


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_time(client):
    response = client.get('/time')
    assert response.status_code == 200


def test_create_existing_user(client):
    user_data = {
        'name': 'test',
        'email': 'test@example.com',
    }
    response = client.post('/users/create', json=user_data)
    assert response.status_code == 200
    print(response.json)
    assert response.get_json() == {'Congrats!': 'User created successfully'}

    response = client.post('/users/create', json=user_data)
    assert response.status_code == 200
    expected_data = {
        'warning': 'The given name is in use, please add another user'}
    assert response.get_json() == expected_data


def test_list_all_users(client):
    user_data = {
        'name': 'test',
        'email': 'test@example.com',
    }
    response = client.post('/users/create', json=user_data)
    assert response.status_code == 200
    print(response.json)
    assert response.get_json() == {'Congrats!': 'User created successfully'}

    response = client.get('/users')
    assert response.status_code == 200
    expected_all_users = {
        'test'
    }
    expected_data = {'users': list(expected_all_users)}
    assert response.get_json() == expected_data


def test_list_user_email(client):
    user_data = {
        'name': 'test',
        'email': 'test@example.com',
    }
    response = client.post('/users/create', json=user_data)
    assert response.status_code == 200
    print(response.json)
    assert response.get_json() == {'Congrats!': 'User created successfully'}

    response = client.get('/users/email')
    assert response.status_code == 200
    expected_data = {'error': 'please provide a valid user name'}
    assert response.get_json() == expected_data


def test_delete_null_user(client):
    response = client.delete(
        '/users/delete')
    assert response.status_code == 200
    expected_data = {
        'error': 'must provide a user name'
    }
    assert response.get_json() == expected_data
