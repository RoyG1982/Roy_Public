from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='URL app')

@app.route('/check_URL_liveness', methods=['GET'])
def check_url_liveness():
    url = request.args.get('url')  # Get URL from query parameters

    if not url:
        return jsonify({"status": "error", "message": "No URL provided"}), 400

    try:
        response = requests.get(url, timeout=5)  # Send GET request with a 5-second timeout

        # Check if response is successful (status code 200)
        if response.status_code == 200:
            status = "URL is live!"
        else:
            status = f"URL returned status code {response.status_code}"

    except requests.exceptions.RequestException as e:
        # Catch any errors such as timeout, DNS failure, etc.
        status = f"Error: {str(e)}"

    return jsonify({"status": "success", "message": status})  # Always return a JSON response

if __name__ == '__main__':
    app.run(debug=True)
