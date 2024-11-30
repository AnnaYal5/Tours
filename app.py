from flask import Flask, render_template, request
import data
from models import db, User
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
bcrypt = Bcrypt(app)

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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        u_email = request.form.get("email")
        password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8')
        user = User(username=username,  password=password, u_email=u_email)
        db.session.add(user)
        db.session.commit()
    return render_template("reg.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
