from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def hiName(name):
    return f"Hi {name.capitalize()}!"

@app.route("/repeat/<num>/<value>")
def repeat(num,value):
    _text = ""
    for _i in range(int(num)):
        _text += value
    return _text

@app.route("/integer/<int:num>")
def integer(num):
    return f"{num} is an integer!"

@app.route("/integer/<num>")
def noInteger(num):
    return f"{num} is not an integer!"

@app.route("/<anything>")
def error(anything):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)