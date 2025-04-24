#Zadanie 6.2
#sql CREATE

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

def execute_sql(conn, sql):
    try:
        c=conn.cursor()
        c.execute(sql)
    except Error as e:
        print (e)

def add_wallet(conn, wallet):
    sql = """INSERT INTO wallets(name, saldo)
    VALUES(?, ?)"""
    cur=conn.cursor()
    cur.execute(sql, wallet)
    conn.commit()
    return wallet[0]
    
def add_transactions(conn, transaction):
    sql= """INSERT INTO transactions(user_name, wallet_name, type_of_transaction, amount, date)
    VALUES(?, ?, ?, ?, ?)"""
    cur=conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return transaction[0]
   

if __name__== '__main__':
    db_file = "myfirstdatabase.db"
    conn=create_connection(db_file)

    create_wallets_sql = """
    --wallets table 
    CREATE TABLE IF NOT EXISTS wallets (
    name text PRIMARY KEY,
    saldo float
    );"""
    create_transactions_sql = """
    --transactions table
    CREATE TABLE IF NOT EXISTS transactions (
    user_name text PRIMARY KEY,
    wallet_name text NOT NULL,
    type_of_transaction VARCHAR(10) NOT NULL,
    amount float,
    date text,
    FOREIGN KEY (wallet_name) REFERENCES wallets (name));"""

    if conn is not None:
        execute_sql(conn, create_wallets_sql)
        execute_sql(conn, create_transactions_sql)
        wallet=("Cash", "22,50")
        transaction=("Kasia", "Cash", "income", "1000", "2025-02-22 00:00:00")
        add_wallet(conn, wallet)
        add_transactions(conn, transaction)
        conn.commit()
        wallet1=("Account", "8000")
        wallet2=("Savings", "0")
        transaction1=("Amanda", "Account", "income", "22", "2025-02-22 00:00:00")
        transaction2=("Czesiek", "Savings", "income", "800", "2025-02-22 00:00:00")
        add_transactions(conn, transaction1)
        add_wallet(conn, wallet1)
        add_wallet(conn, wallet2)
        add_transactions(conn, transaction2)
        conn.commit()
        conn.close()

    
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