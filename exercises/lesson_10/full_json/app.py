from flask import Flask, make_response, jsonify, request, render_template
import movie_finder
import time

app = Flask(__name__)
    
@app.route('/health', methods=['GET'])
def healthcheck():
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='Movie App')

@app.route('/<filename>', methods=['GET'])
def static_files(filename):
    return app.send_static_file(filename)

@app.route('/get_movies', methods=['GET'])
def get_movies():
    time.sleep(7)
    keyword = request.args.get('keyword')
    movies = movie_finder.get_movie_info(keyword)

    return jsonify(movies)

app.run(debug=True, host="0.0.0.0", port="8080")