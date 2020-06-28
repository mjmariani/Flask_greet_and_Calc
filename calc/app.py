# Put your app in here.
from flask import Flask, request #installed flask in venv
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b params."""
    
    a = int(request.args.get("a")) ##casting the value that is paired with key -> a 
    b = int(request.args.get("b")) ##casting the value that is paired with key -> b
    
    result = add(a, b)
    return str(result)
    
@app.route("/sub")
def do_sub():
    """Subtract a and b parameters."""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    
    return str(result)    

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters. """
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    result = mult(a, b)
    
    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters.
    """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
    
    
}
    
@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)  ##uses whatever is put into oper as key for operators dictionary then pulls in value and sets result to the return value of operations module function that is set after the value is pulled from the operators dictionary
    
    return str(result)    