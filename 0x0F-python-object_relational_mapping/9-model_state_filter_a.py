#!/usr/bin/python3
"""Script to list State objects from a MySQL database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLAlchemy engine and session
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database_name}')
    session = Session(engine)

    # Query for all State objects and sort by states.id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
