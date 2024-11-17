import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Path to the JSON file where user data will be stored
users_file_path = 'users.json'

# Load existing users data from the JSON file (if it exists)
def load_users():
    try:
        with open(users_file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Write user data to the JSON file
def save_users(users):
    with open(users_file_path, 'w') as file:
        json.dump(users, file, indent=2)

# Route to serve the registration page (HTML form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission (POST request)
@app.route('/register', methods=['POST'])
def register():
    # Get the form data (username and password)
    username = request.json.get('username')
    password = request.json.get('password')

    # Validate the input
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Load existing users
    users = load_users()

    # Check if the username already exists
    if username in users:
        return jsonify({'error': 'Username already taken'}), 400

    # Add the new user to the users dictionary
    users[username] = password

    # Save the updated users dictionary to the JSON file
    save_users(users)

    return jsonify({'message': 'User registered successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
