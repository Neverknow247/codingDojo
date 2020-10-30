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

@app.route("/integer/<num>")
def integer(num):
    if num != int(num):
        return "no"
    else:
        return "yes"

if __name__ == "__main__":
    app.run(debug=True)