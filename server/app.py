#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input>')
def print_string(input):
    return f'Your Input is: {input}.'
@app.route('/count/<int:value>')
def count(value):
    result = [int(i) for i in range(value)]
    return result
@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1,operator,num2):
    if operator =='*':
        result = [num1*num2]
    elif operator=='+':
        result = [num1+num2]
    elif operator =='-':
        result = [num1-num2]
    elif operator=='div':
        result= [num1/num2]
    elif operator =='%':
        result = [num1%num2]
    else: 
        result = "Invalid Operator"

    return result

if __name__ == '__main__':
    app.run(port=5555, debug=True)
