import sqlite3
from sqlite3 import Error


def connect(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)

def create_person(conn, person):
    sql = ''' INSERT INTO people(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [person,])
    conn.commit()
    return cur.lastrowid

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM people")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"pythonsqlite.db"

    sql_create_table = """ CREATE TABLE IF NOT EXISTS people (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    conn = connect(database)

    if conn is not None:
        create_table(conn, sql_create_table)

    print(conn)

    person = ('cmoorelabs')
    person_id = create_person(conn, person)

    select_all(conn)


if __name__ == '__main__':
    main()
