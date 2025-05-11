#zadanie 6.3

import sqlite3
import sqlalchemy 
from sqlite3 import Error
from sqlalchemy import select

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

if __name__== '__main__':
    db_file = "myseconddatabase2.db"
    conn=create_connection(db_file)

from sqlalchemy import create_engine, Table, Column, Integer, Float, String, MetaData

engine=create_engine('sqlite:///myseconddatabase2.db')
meta=MetaData()


stations = Table(
   'stations', meta,
   Column('station', String, primary_key=True),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', String),
   Column('country', String),
   Column('state', String)
)

measures= Table( 'measures', meta,
                Column('station', String, foreign_key=True),
                Column('date', String,),
                Column('precip', Float),
                Column('tobs', Integer))

meta.create_all(engine)
print(engine.table_names())

s = select(measures).limit(5)
result = conn.execute(s)

for row in result:
   print(row)