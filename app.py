from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def show_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.get("/sub")
def show_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.get("/mult")
def show_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.get("/div")
def show_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))
