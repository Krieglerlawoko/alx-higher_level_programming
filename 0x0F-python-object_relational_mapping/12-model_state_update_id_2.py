#!/usr/bin/python3
"""State object with the name passed as argument from the database printd
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    newInstance = session.query(State).filter_by(id=2).first()
    newInstance.name = 'New Mexico'
    session.commit()
