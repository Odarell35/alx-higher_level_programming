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
    ed_state = State(name="Louisiana")
    session.add(ed_state)
    session.commit()

    # Display the results
    print(ed_state.id)

    # Close the session
    session.close()
