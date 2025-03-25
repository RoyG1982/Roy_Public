from flask import session, request, jsonify
import json
import os
import requests
import socket
import ssl
from datetime import datetime 
from concurrent.futures import ThreadPoolExecutor, as_completed

domain_file = 'domains.json'

def check():
    domain = request.form['domain'].strip()
    result, cert_info = check_domain_liveness(domain)
    return jsonify(result=result, cert_info=cert_info)

def check_domain_liveness(domain):
    try:
        if not domain.startswith(('http://', 'https://')):
            domain = 'https://' + domain

        response = requests.head(domain, timeout=5, allow_redirects=True)
        cert_info = get_ssl_certificate_info(domain)

        if response.status_code == 200:
            return "Live", cert_info
        else:
            return f"Not reachable (Status code: {response.status_code})", cert_info
            
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}", None

def get_ssl_certificate_info(hostname):
    if hostname.startswith("https://"):
        hostname = hostname[8:]
    elif hostname.startswith("http://"):
        hostname = hostname[7:]

    context = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, 443)) as conn:
            with context.wrap_socket(conn, server_hostname=hostname) as ssl_sock:
                cert = ssl_sock.getpeercert()

        common_name = next((value for field in cert['subject'] for key, value in field if key == 'commonName'), "")
        valid_until_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT")

        return common_name, valid_until_date
    
    except Exception as e:
        return f"Failed to get SSL certificate info for {hostname}: {e}"

def add_domain():
    username = session.get('username')
    if not username:
        return jsonify({"status": "error", "message": "User not logged in."}), 401

    domain = request.form.get('domain').strip()
    if not domain:
        return jsonify({"status": "error", "message": "Domain not provided"}), 400

    domains = read_domains()
    if username not in domains:
        domains[username] = []

    if domain not in domains[username]:
        domains[username].append(domain)

    write_domains(domains)
    return jsonify({"status": "success", "message": "Domain added successfully."}), 200

def add_multiple_domains():
    username = session.get('username')
    if not username:
        return jsonify({"status": "error", "message": "User not logged in."}), 401

    data = request.get_json()
    domains = [domain.strip() for domain in data.get('domains', [])]

    if not domains:
        return jsonify({"status": "error", "message": "No domains provided"}), 400

    all_domains = read_domains()
    if username not in all_domains:
        all_domains[username] = []

    new_domains = [domain for domain in domains if domain not in all_domains[username]]
    all_domains[username].extend(new_domains)

    write_domains(all_domains)
    return jsonify({"status": "success", "message": f"{len(new_domains)} domains added successfully."}), 200

def get_domains():
    username = session.get('username')
    if not username:
        return jsonify({"status": "error", "message": "User not logged in."}), 401

    all_domains = read_domains()
    user_domains = all_domains.get(username, [])

    domains_with_info = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {executor.submit(check_domain_liveness, domain): domain for domain in user_domains}
        for future in as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                liveness, cert_info = future.result()
                domains_with_info.append({
                    "domain": domain,
                    "liveness": liveness,
                    "cert_info": cert_info
                })
            except Exception as e:
                domains_with_info.append({
                    "domain": domain,
                    "liveness": "Error",
                    "cert_info": None
                })

    return jsonify({"status": "success", "domains": domains_with_info})

def read_domains():
    if not os.path.exists(domain_file):
        return {}
    with open(domain_file, 'r') as file:
        return json.load(file)

def write_domains(domains):
    with open(domain_file, 'w') as file:
        json.dump(domains, file, indent=4)