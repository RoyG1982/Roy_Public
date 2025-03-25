from flask import session, request, jsonify
from file_operations import read_users, write_users

def schedule_func():
    if 'username' not in session:
        return jsonify({"status": "error", "message": "User not logged in."}), 401
    
    data = request.get_json()
    input_time = data.get('input_time')

    if not input_time:
        return jsonify({"status": "error", "message": "Invalid input."}), 400

    print(input_time)  # Simulate scheduling logic
    return jsonify({"status": "success", "time": input_time}), 200