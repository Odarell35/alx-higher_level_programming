#!/usr/bin/python3
"""Model city fetch by state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLAlchemy engine and session
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database_name}')
    session = Session(engine)

    # Query for all State objects and sort by states.id
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()

    # Display the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()

    # Close the session
    session.close()
