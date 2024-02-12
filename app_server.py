from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime
from pprint import pprint
import os

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['users_db']
collection = db['users']


@app.route('/', methods=['GET'])
# display the welcome message
def get_data():
    data = {'message': 'Welcome to my APP! Let\'s summarize the notes!'}
    return jsonify(data)


@app.route('/time', methods=['GET'])
# get the current time
def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'Current time': current_time})


@app.route('/users/create', methods=['POST'])
# creat a user
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({'Error': 'Name is not provided'})
    if not email:
        s = "Email is not provided"
        pprint()
        return

    # check if the user exists
    eixisting_user = collection.find_one({'name': name})
    if eixisting_user:
        return jsonify({'warning': 'The given name is in use, please add another user'})

    # insert newly created user into mongodb
    new_user = {'name': name, 'email': email}
    collection.insert_one(new_user)
    return jsonify({'Congrats!': 'User created successfully'})


@app.route('/users', methods=['GET'])
# list all users names
def get_users():
    users = [user['name'] for user in collection.find(
        {}, {'_id': 0, 'name': 1})]  # excludes id but with name
    return jsonify({'users': users})


@app.route('/users/email', methods=['GET'])
# given a user and get email
def get_user_email():
    user_name = request.args.get('name')
    if not user_name:
        return jsonify({'error': 'please provide a valid user name'})
    user = collection.find_one({'name': user_name}, {'_id': 0, 'email': 1})
    # if user is not exist
    if user is None:
        return jsonify({'error': 'there is not such user'})
    user_email = user.get('email')
    return jsonify({user_name: user_email})


@app.route('/users/delete', methods=['DELETE'])
# delete a given user
def delete_user_by_name():
    user_name = request.args.get('name')
    if not user_name:
        return jsonify({'error': 'must provide a user name'})

    # check if user exits
    user = collection.find_one({'name': user_name})
    if user is None:
        return jsonify({'error': 'no such user'})
    # delete
    deleted = collection.delete_one({'name': user_name})
    if deleted.deleted_count == 1:
        return jsonify({'Great!': 'successfully deleted the given user'})
    else:
        return jsonify({'sorry': 'failed to delete the given user'})


os.environ['FLASK_ENV'] = 'production'

if __name__ == '__main__':
    # 0.0.0.0 it will bind to all available network interfaces within the docker container
    app.run(host='0.0.0.0', debug=True, port=3000)
    # app.run(host='localhost', debug=True, port=8080)
