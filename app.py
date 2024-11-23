from flask import Flask, render_template, request
import data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title=data.title, departures=data.departures, tours=data.tours)


@app.route("/departures/<departure>")
def departures(departure: str):
    tours_departure = []
    tours_list = []
    for key, tour in data.tours.items():
        if tour.get("departure") == departure.lower():
            tours_departure.append(key)
    for tour_departure in tours_departure:
        tours_list.append(data.tours.get(tour_departure))
    print(tours_list)
    return render_template("departures.html", tours_departure=tours_list, tours=data.tours)


@app.route("/tours")
def tours():
    return render_template("tours.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
