from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/departures")
def departures():
    return render_template("departures.html")


@app.route("/tours")
def tours():
    return render_template("tours.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
