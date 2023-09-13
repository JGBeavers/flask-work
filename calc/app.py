from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def adding():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtracting():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a, b))

@app.route('/mult')
def multiplying():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a, b))

@app.route('/div')
def dividing():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a, b))


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route('/math/<operator>')
def do_operation(operator):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operators[operator](a, b)

    return str(result)