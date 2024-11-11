from flask import Flask, make_response, jsonify, request, render_template

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='Time App')

@app.route('/<filename>', methods=['GET'])
def static_files(filename):
    return app.send_static_file(filename)

app.run(debug=True, host="0.0.0.0", port="8080")

    
    