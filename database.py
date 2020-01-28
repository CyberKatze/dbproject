from flask import g
import psycopg2
import psycopg2.extras
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn, conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def get_db():
    if not hasattr(g, 'db'):
        g.db = connect()

    return g.db
