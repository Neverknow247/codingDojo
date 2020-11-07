from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def eightByEight():
    return render_template("index.html", numX= 8, numY= 8, color1= "white", color2= "black")

@app.route("/<x>")
def eightByX(x):
    return render_template("index.html", numX= int(x), numY= 8, color1= "white", color2= "black")

@app.route("/<x>/<y>")
def XByY(x, y):
    return render_template("index.html", numX= int(x), numY= int(y), color1= "white", color2= "black")

@app.route("/<x>/<y>/<color1>/<color2>")
def XByYColor(x, y, color1, color2):
    return render_template("index.html", numX= int(x), numY= int(y), color1= color1, color2= color2)

if __name__ == '__main__':
    app.run(debug=True)