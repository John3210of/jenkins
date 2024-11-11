# app.py
from flask import Flask, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    operation = request.args.get('operation')

    if a is None or b is None or operation not in ['add', 'subtract', 'multiply', 'divide']:
        return "Invalid input. Make sure to provide 'a', 'b', and 'operation' parameters.", 400

    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    else:
        return "Unknown operation.", 400

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
