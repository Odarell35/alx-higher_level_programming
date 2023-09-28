#!/usr/bin/python3
"""Script to list State objects from a MySQL database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, database_name, state_search = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create an SQLAlchemy engine and session
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database_name}')
    session = Session(engine)

    # Query for all State objects and sort by states.id
    state = session.query(State).filter_by(name=state_search).order_by(State.id).first()

    # Display the results
    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")

    # Close the session
    session.close()