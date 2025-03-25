from flask import Flask, render_template, session, jsonify, request, redirect, url_for
import os
from user_related_functions import login_user, register_user, get_logged_in_user
from domains import add_domain, add_multiple_domains, get_domains, check
from file_operations import read_users, write_users
from schedule import schedule_func

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login_route():
    return login_user()

@app.route('/logout', methods=['POST'])
def logout_route():
    session.pop('username', None)
    return "User logged out!"

@app.route('/register', methods=['POST'])
def register_route():
    return register_user()

@app.route('/user_homepage')
def user_homepage_route():
    username = get_logged_in_user()
    if not username:
        return redirect(url_for('index'))
    return render_template('user_homepage.html', username=username)

@app.route('/check', methods=['POST'])
def check_route():
    return check()

@app.route('/add', methods=['POST'])
def add_domain_route():
    return add_domain()

@app.route('/add_multiple', methods=['POST'])
def add_multiple_domains_route():
    return add_multiple_domains()

@app.route('/get_domains', methods=['GET'])
def get_domains_route():
    return get_domains()

@app.route('/schedule', methods=['POST'])
def schedule_route():
    return schedule_func()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)