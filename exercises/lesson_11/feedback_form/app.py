from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='feedback app')

@app.route('/feedback', methods=['GET'])
def feedback():
    username = request.args.get('username')  # Get username from query parameters
    email = request.args.get('email')  # Get email from query parameters
    comment = request.args.get('comment')  # Get comment from query parameters

    # Log to a file
    with open("feedback_log.txt", "a") as log_file:  # "a" mode appends to the file
        log_file.write(f"Username: {username}, Email: {email}, Comment: {comment}\n")

    return jsonify({"username": username, "email": email, "comment": comment})  # Always return a JSON response

if __name__ == '__main__':
    app.run(debug=True)
