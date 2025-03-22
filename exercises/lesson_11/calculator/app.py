from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', title='calculator app')

@app.route('/calculate', methods=['GET'])
def calculate():
    input_number_1 = int(request.args.get('input_number_1', 0))  # Default to 0 if missing
    input_number_2 = int(request.args.get('input_number_2', 0))  # Default to 0 if missing
    arithmetic_operation = request.args.get('arithmetic_operation')  # Get arithmetic_operation from query parameters
    if arithmetic_operation == "add":
        result = input_number_1 + input_number_2
    elif arithmetic_operation =="subtract":
        result = input_number_1 - input_number_2
    elif arithmetic_operation =="multiply":
        result = input_number_1 * input_number_2
    elif arithmetic_operation == "divide":
        if input_number_2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = input_number_1 / input_number_2

    return jsonify({
        "input_number_1": input_number_1,
        "input_number_2": input_number_2,
        "arithmetic_operation": arithmetic_operation,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)
