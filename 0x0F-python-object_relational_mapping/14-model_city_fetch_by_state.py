#!/usr/bin/python3
"""Model city fetch by state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def city_list(City):
    """list city by state"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database_name), pool_pre_ping=True)
    s = Session(engine)
    results = s.query(State, City).filter(City.state_id == State.id).order_by(City.id).all()

    for i, j in results:
        print(f"{i.name}: ({j.id}) {j.name}")
    s.commit()
    s.close()


if __name__== "__main__":
    city_list(City)
