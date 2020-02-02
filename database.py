from flask import g, current_app
import psycopg2
import psycopg2.extras
from config import db_config


def connect_db():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        

        # connect to the PostgreSQL server
        conn = psycopg2.connect(current_app.config.get('DATABASE_URL'))

    except (Exception, psycopg2.DatabaseError) as error:
        raise error
    return conn, conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def get_db():
    db = connect_db()
    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]
    

    return g.postgres_db_cur

def init_db():
    db =connect_db()
    db[1].execute(open('tables.sql','r').read())
    db[0].commit()
    db[1].close()
    db[0].close()

