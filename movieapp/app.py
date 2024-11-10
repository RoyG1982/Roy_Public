from flask import Flask, make_response, jsonify, request, render_template
from movie_db import movie_search
import time

app = Flask(__name__)
    
@app.route('/health', methods=['GET'])
def healthcheck():
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='Weather App')

@app.route('/<filename>', methods=['GET'])
def static_files(filename):
    return app.send_static_file(filename)

@app.route('/movie_search', methods=['GET'])
def get_weather():
    time.sleep(1)
    keyword = request.args.get('movie_name')
    result = movie_search('keyword')
    return result

app.run(debug=True, host="0.0.0.0", port="8080")