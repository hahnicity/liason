"""
liason.bootstrap
~~~~~~~~~~~~~~~~

Setup postgresql on our machine. Create a database of our choosing and
grant privileges on that db to the current user.
"""
from subprocess import call

from liason.defaults import db


def install_postgres():
    """
    Install the most recent version of PostGRESQL on our machine
    """
    call("sudo aptitude install postgresql".split())
    call("sudo aptitude install python-dev".split())
    call("sudo aptitude install libpq-dev".split())


def create_db():
    """
    Create a database of our choosing. Should be postgres user to run
    """
    call("psql -c='CREATE DATABASE {};'".format(db["database"]).split())


def setup_permissions():
    """
    Set up permissions on a db for a desired user.
    """
    call("psql -c='CREATE USER {} WITH PASSWORD {};'".format(
        db["user"], db["password"]).split()
    )
    call("psql -c='GRANT PRIVILEGES ON DATABASE {} to {};'".format(
        db["database"], db["user"]).split()
    )


def create_table():
    """
    Create the table we wish to store our information and the table
    schema as well
    """
    call("psql -d {} -c='CREATE TABLE {} (name varchar (50),"
         "address text, id smallint);'".format(db["database"], db["table"]).
         split())
