#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route("/count/<int:num>")
def count(num):
    print(f"{num}")
    for i in range(num):
        print(f"{i}")
    return f"{num}"

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    result = 0
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        result = f"Cannot perfom a {num1} {operation} {num2} operation"
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
