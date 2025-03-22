from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='temperature conversion app')

@app.route('/temperature_conversion', methods=['GET'])
def temp_convert():
    temp_c = request.args.get('temp_c')  # Get temperature C from query parameters
    temp_c = float(temp_c)  # Convert to integer
    temp_f = (temp_c * 9/5) + 32  # Convert Celsius to Fahrenheit

    return jsonify({
        "celsius": temp_c,
        "fahrenheit": temp_f,
    })

if __name__ == '__main__':
    app.run(debug=True)
