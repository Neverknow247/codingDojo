from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("index.html", times= 3, color= "rgb(43, 160, 255)")

@app.route("/play/<num>")
def playX(num):
    return render_template("index.html", times= int(num), color= "rgb(43, 160, 255)")

@app.route("/play/<num>/<color>")
def playXColor(num, color):
    return render_template("index.html", times= int(num), color= color)

if __name__ == '__main__':
    app.run(debug=True)