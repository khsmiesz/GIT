#SQL READ

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        print (f'Connected to {db_file}, sqlite version: {sqlite3.version}')
    except sqlite3.Error as e:
        print(e)
    return conn

conn=create_connection("myfirstdatabase.db")
cur=conn.cursor()
cur.execute("SELECT * FROM transactions")
rows=cur.fetchall()
print(rows)
row=cur.fetchone()
print(row)

def select_task_by_status(conn, user_name):
   cur = conn.cursor()
   cur.execute("SELECT * FROM transactions WHERE user_name=?", (user_name,))
   rows = cur.fetchall()
   return rows

select_task_by_status(conn, "Amanda")

def select_all(conn, table):
    cur=conn.cursor()
    cur.execute(f'SELECT * FROM {table}')
    rows=cur.fetchall()
    return rows

select_all(conn, "wallets")

def select_where(conn, table, **query):
    cur=conn.cursor()
    qs=[]
    values=()
    for k, v in query.items():
        qs.append(f'{k}=?')
        values+=(v,)
    q="AND".join(qs)
    cur.execute(f'SELECT * FROM {table} WHERE {q}', values)
    rows=cur.fetchall()
    return rows

select_where(conn, "transactions", user_name="Kasia") 