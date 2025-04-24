#sql UPDATE

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
   except Error as e:
       print(e)

   return conn

def update(conn, table, name, **kwargs):
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (name, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE name = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)

if __name__ == "__main__":
   conn = create_connection("myfirstdatabase.db")
   update(conn, "wallets", "Gotówka", saldo="999")
   conn.close()