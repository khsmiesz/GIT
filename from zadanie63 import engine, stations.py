
from sqlalchemy import create_engine, select, MetaData, Integer, String, Table, Column
from zadanie63 import engine, stations

conn = engine.connect()
s = select(stations).limit(5)
result = conn.execute(s)

for row in result:
   print(row)
