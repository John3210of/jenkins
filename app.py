# app.py
from flask import Flask, request
from calculator import add, subtract, multiply, divide
import os

app = Flask(__name__)

pod_name = os.getenv('POD_NAME', 'Unknown Pod')
pod_ip = os.getenv('POD_IP', 'Unknown IP')

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

    # 결과에 Pod 이름과 IP를 포함하여 로드 밸런싱 상태를 확인할 수 있게 함
    return f"Result: {result}\nServed by: {pod_name} ({pod_ip})"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
