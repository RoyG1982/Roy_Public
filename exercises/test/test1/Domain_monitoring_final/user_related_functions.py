from flask import session, request, jsonify
from file_operations import read_users, write_users

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = read_users()

    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True
        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Username or password is incorrect.")

def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = read_users()

    if username in users:
        return jsonify(success=False, message="Username already exists.")

    users[username] = password
    write_users(users)

    return jsonify(success=True)

def get_logged_in_user():
    return session.get('username')
