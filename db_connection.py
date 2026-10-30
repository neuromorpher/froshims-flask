import sqlite3


def connect_db(db_path):

    conn = sqlite3.connect(db_path) 
    conn.execute("PRAGMA foreign_keys = ON") 
    return conn


