from flask import Flask, render_template, session, jsonify, request, redirect, url_for
import json
import os
import requests
import ssl
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import concurrent.futures

user_file_path = 'users.json'
domain_file = 'domains.json'

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = read_users()

    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True
        print(f"User logged in: {username}")
        print(f"Session after login: {session}")
        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Username or password is incorrect.")

@app.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = read_users()

    if username in users:
        return jsonify(success=False, message="Username already exists.")
    
    users[username] = password
    write_users(users)

    return jsonify(success=True)

@app.route('/user_homepage')
def user_homepage_route():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('user_homepage.html', username=username)

def read_users():
    if not os.path.exists(user_file_path):
        return {}
    with open(user_file_path, 'r') as file:
        return json.load(file)

def write_users(users):
    with open(user_file_path, 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/check', methods=['POST'])
def check():
    domain = request.form['domain'].strip()  # Clean up the domain input
    result, cert_info = check_domain_liveness(domain)
    return jsonify(result=result, cert_info=cert_info)

def check_domain_liveness(domain):
    try:
        # Add 'https://' if not present
        if not domain.startswith(('http://', 'https://')):
            domain = 'https://' + domain
        
        response = requests.head(domain, timeout=5, allow_redirects=True)
        
        # Check SSL certificate details
        cert_info = get_ssl_certificate_info(domain)

        if response.status_code == 200:
            return "Live", cert_info
        else:
            return f"Not reachable (Status code: {response.status_code})", cert_info
            
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}", None

def get_ssl_certificate_info(hostname):
    # Ensure the hostname is without 'https://', 'http://' for SSL check
    if hostname.startswith("https://"):
        hostname = hostname[8:]
    elif hostname.startswith("http://"):
        hostname = hostname[7:]

    # Get the SSL certificate of the server
    context = ssl.create_default_context()

    try:
        # Connect to the server and retrieve the certificate
        with socket.create_connection((hostname, 443)) as conn:
            with context.wrap_socket(conn, server_hostname=hostname) as ssl_sock:
                cert = ssl_sock.getpeercert()

        # Extract Common Name (CN) from the certificate
        common_name = ""
        for field in cert['subject']:
            for key, value in field:
                if key == 'commonName':
                    common_name = value

        # Extract Valid Until date
        valid_until = cert['notAfter']
        valid_until_date = datetime.strptime(valid_until, "%b %d %H:%M:%S %Y GMT")

        return common_name, valid_until_date
    
    except Exception as e:
        return f"Failed to get SSL certificate info for {hostname}: {e}"

@app.route('/add', methods=['POST'])
def add_domain():
    print(f"Current session: {session}")
    username = session.get('username')
    if not username:
        print("Username not found in session")
        return jsonify({"status": "error", "message": "User not logged in."}), 401

    domain = request.form.get('domain').strip()  # Clean up the domain input

    if not domain:
        return jsonify({"status": "error", "message": "Domain not provided"}), 400

    try:
        with open(domain_file, 'r') as file:
            domains = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        domains = {}

    if username not in domains:
        domains[username] = []

    if domain not in domains[username]:
        domains[username].append(domain)

    with open(domain_file, 'w') as file:
        json.dump(domains, file, indent=4)

    return jsonify({"status": "success", "message": "Domain(s) added successfully. Please refresh the page to see updates."}), 200

@app.route('/add_multiple', methods=['POST'])
def add_multiple_domains():
    print(f"Current session: {session}")
    username = session.get('username')
    if not username:
        print("Username not found in session")
        return jsonify({"status": "error", "message": "User not logged in."}), 401

    data = request.get_json()
    domains = [domain.strip() for domain in data.get('domains', [])]  # Clean up each domain

    if not domains:
        return jsonify({"status": "error", "message": "No domains provided"}), 400

    try:
        with open(domain_file, 'r') as file:
            all_domains = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_domains = {}

    if username not in all_domains:
        all_domains[username] = []

    count = 0
    for domain in domains:
        if domain and domain not in all_domains[username]:  # Check for non-empty and uniqueness
            all_domains[username].append(domain)
            count += 1

    with open(domain_file, 'w') as file:
        json.dump(all_domains, file, indent=4)

    # Add domains to session
    if 'domains' not in session:
        session['domains'] = []
    
    session['domains'].extend(domains)
    session.modified = True

    return jsonify({"status": "success", "message": f"{count} domain(s) added successfully. Please refresh the page to see updates."}), 200

@app.route('/get_domains', methods=['GET'])
def get_domains():
    username = session.get('username')
    if not username:
        return jsonify({"status": "error", "message": "User not logged in."}), 401

    try:
        with open(domain_file, 'r') as file:
            all_domains = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_domains = {}

    user_domains = all_domains.get(username, [])
    
    domains_with_liveness_and_cert_info = []
    
    # Use ThreadPoolExecutor to check domains concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {executor.submit(check_domain_liveness, domain): domain for domain in user_domains}
        for future in as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                liveness, cert_info = future.result()
                domains_with_liveness_and_cert_info.append({
                    "domain": domain,
                    "liveness": liveness,
                    "cert_info": cert_info
                })
            except Exception as exc:
                print(f'{domain} generated an exception: {exc}')
                domains_with_liveness_and_cert_info.append({
                    "domain": domain,
                    "liveness": "Error",
                    "cert_info": None
                })

    return jsonify({"status": "success", "domains": domains_with_liveness_and_cert_info})

if __name__ == '__main__':
    app.run(debug=True)
