import pytest
import requests

BASE_URL = 'http://localhost:3000'

new_user_data = {
    'name': 'Liz K',
    'email': 'l.w.com'
}

existing_user_data = {
    'name': 'Jason Lee',
    'email': 'Jason.Lee.Wang@sample.com'
}

expected_all_users = {
    "Jason Lee",
    "Liz K"
}
user_name_to_delete = 'Liz K'
user_name_to_delete_none_existing = 'unknown'
user_name_to_get_email = 'Jason Lee'
expected_email = 'Jason.Lee.Wang@sample.com'


def test_hi():
    assert '3' == '3'


def test_time(client):
    response = client.get(f'/time')
    assert response.status_code == 200


def test_create_user(client):
    response = client.post(f'{BASE_URL}/users/create', json=new_user_data)
    assert response.status_code == 200


# def test_create_existing_user():
#     response = requests.post(
#         f'{BASE_URL}/users/create', json=existing_user_data)
#     assert response.status_code == 200
#     expected_data = {
#         'warning': 'The given name is in use, please add another user'}
#     assert response.json() == expected_data


# def test_list_all_users():
#     response = requests.get(
#         f'{BASE_URL}/users'
#     )
#     assert response.status_code == 200
#     expected_data = {
#         'users': expected_all_users
#     }
#     actual_users = set(response.json()['users'])
#     expected_users = expected_data['users']

#     extra_users = expected_users - actual_users
#     if extra_users:
#         print("Extra users in the expected users:", extra_users)
#     assert actual_users == expected_users


# def test_list_user_email():
#     response = requests.get(
#         f'{BASE_URL}/users/email?name={user_name_to_get_email}'
#     )
#     assert response.status_code == 200
#     expected_data = {
#         user_name_to_get_email: expected_email
#     }
#     assert response.json() == expected_data


# def test_delete_given_user():
#     response = requests.delete(
#         f'{BASE_URL}/users/delete?name={user_name_to_delete}')
#     assert response.status_code == 200
#     expected_data = {
#         'Great!': 'successfully deleted the given user'
#     }
#     assert response.json() == expected_data


# def test_delete_none_existing_user():
#     response = requests.delete(
#         f'{BASE_URL}/users/delete?name={user_name_to_delete_none_existing}')
#     assert response.status_code == 200
#     expected_data = {
#         'error': 'no such user'
#     }
#     assert response.json() == expected_data
