#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sqlalchemy import create_engine

if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(eng)

    Ses = sessionmaker(bind=eng)
    ses = Session()

    newstate = State(name='California')
    newcity = City(name='San Francisco')
    newState.cities.append(newcity)

    ses.add(newstate)
    ses.add(newcity)
    ses.commit()
