from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def eightByEight():
    return render_template("index.html", numX= 8, numY= 8)

if __name__ == '__main__':
    app.run(debug=True)