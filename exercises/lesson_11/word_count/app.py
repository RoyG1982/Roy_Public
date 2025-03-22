from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='word count tool')

@app.route('/word_count', methods=['GET'])
def word_count():
    text_input = request.args.get('text_input')  # Get input_text from query parameters
    words = len(text_input.split())

    return jsonify({"number_of_words": words})  # Always return a JSON response

if __name__ == '__main__':
    app.run(debug=True)