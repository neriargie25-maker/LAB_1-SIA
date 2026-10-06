from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    op = data.get('operation', 'add')

    if op == 'add':
        result = num1 + num2
    elif op == 'subtract':
        result = num1 - num2
    elif op == 'multiply':
        result = num1 * num2
    elif op == 'divide':
        result = num1 / num2 if num2 != 0 else "Error: Divide by zero"
    elif op == 'modulo':
        result = num1 % num2 if num2 != 0 else "Error: Modulo by zero"
    elif op == 'power':
        result = num1 ** num2
    elif op == 'square_root':
        result = math.sqrt(num1) if num1 >= 0 else "Error: Negative sqrt"
    else:
        result = "Unknown operation"

    return jsonify({
        'result': result,
        'num1': num1,
        'num2': num2,
        'operation': op
    })

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'Python is running!'})

if __name__ == '__main__':
    app.run(port=5001, debug=True)