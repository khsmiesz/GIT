#sql DELETE

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
   except Error as e:
       print(e)

   return conn

def delete(conn, table, **kwargs):
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)

   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()
   print("Deleted")

conn=create_connection("myfirstdatabase.db")
delete(conn, "wallets", name="Gotówka")