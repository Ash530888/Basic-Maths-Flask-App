from flask import Flask
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")


@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum")
def sum_route():
    num1 = float (request. args.get ( 'num1'))
    num2 = float(request.args.get 'num2')
    result = summation (numl, num2)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get ( 'num1'))
    num2 = float (request.args.get ('num2'))
    result = subtraction (numi, num2)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = float (request.args.get ('num1'))
    num2 = float (request.args.get 'num2'))
    result = multiplication (numl, num2)
    return str(result)

