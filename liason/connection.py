"""
liason.connection
~~~~~~~~~~~~~~~~~
"""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from liason.defaults import db


def make_engine(**kwargs):
    """
    Return our database engine
    """
    db.update(kwargs)
    return create_engine("{}://{}:{}@{}/{}".format(
        db["engine"],
        db["user"],
        db["password"],
        db["hostname"],
        db["database"])
    )


def make_session(engine):
    """
    Create a database session
    """
    Session = sessionmaker(bind=engine)
    return Session()


@contextmanager
def execute_session(session):
    """
    Execute some kind of action with a session object
    """
    try:
        yield
    except:
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close()
