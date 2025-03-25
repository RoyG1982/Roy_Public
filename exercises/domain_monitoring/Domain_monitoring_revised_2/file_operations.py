import json
import os

user_file_path = 'users.json'

def read_users():
    if not os.path.exists(user_file_path):
        return {}
    with open(user_file_path, 'r') as file:
        return json.load(file)

def write_users(users):
    with open(user_file_path, 'w') as file:
        json.dump(users, file, indent=4)
