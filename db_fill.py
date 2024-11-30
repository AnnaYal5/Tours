from data import tours
from models import Tour, db, Departure
from app import app
buffer_dict = {}

with app.app_context():
    buffer_set: set = set()
    db.create_all()
    for key, value in tours.items():
        tour = Tour(**value)
        db.session.add(tour)
        db.session.commit()
    #     buffer_set.add(value["departure"])
    # for departure in buffer_set:
    #     dpt = Departure(name=departure)
    #     db.session.add(dpt)
    #     db.session.commit()
