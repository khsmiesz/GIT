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
        wallet=("Gotówka", "22,50")
        add_wallet(conn, wallet)
        transaction=("Kasia", "Gotówka", "income", "1000", "2025-02-22 00:00:00")
        add_transactions(conn, transaction)
        conn.commit()
        conn.close()
    


