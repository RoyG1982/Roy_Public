from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def url():
    return render_template('index.html')

@app.route('/<filename>')
def file(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)