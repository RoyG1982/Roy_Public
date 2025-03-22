from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='Time App')

@app.route('/get_time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'time': current_time})
    
if __name__ == '__main__':
    app.run(debug=True)