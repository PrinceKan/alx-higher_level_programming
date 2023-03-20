#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_states():
    """ list_states function that uses to list the states from the database """
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db_connect = f"mysql+mysqldb://{mysql_username}:{mysql_password}\
        @localhost:3306/{database_name}"

    engine = create_engine(db_connect, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    Session = session()

    new_state = Session.query(State).filter(State.id == 2).one()
    new_state.name = "New Mexico"
    Session.commit()

    Session.close()


if __name__ == "__main__":
    list_states()
