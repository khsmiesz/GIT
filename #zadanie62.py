# `ex_01_conection_to_db.py`

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)
if __name__ == '__main__':
    create_projects_sql = """
    -- projects table
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        nazwa text NOT NULL,
        start_date text,
        end_date text
    );
    """
    create_tasks_sql = """
    -- zadanie table
    CREATE TABLE IF NOT EXISTS tasks (
       id integer PRIMARY KEY,
       project_id integer NOT NULL,
       nazwa VARCHAR(250) NOT NULL,
       opis TEXT,
       status VARCHAR(15) NOT NULL,
       start_date text NOT NULL,
       end_date text NOT NULL,
       FOREIGN KEY (project_id) REFERENCES projects (id)
    );
   """

    db_file = "database.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_projects_sql)
        execute_sql(conn, create_tasks_sql)
        conn.close()

INSERT INTO projects(id, nazwa, start_date, end_date)
   VALUES (1,
           "Zrób zadania",
           "2020-05-08 00:00:00",
           "2020-05-10 00:00:00");