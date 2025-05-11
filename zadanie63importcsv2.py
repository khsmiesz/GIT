import csv
from zadanie63 import engine, stations, measures


ins2=measures.insert()
measures_list=[]

with open("clean_measure.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        measures_list.append({
            'station': row[0],
            'date': (row[1]),
            'precip': float(row[2]),
            'tobs': int(row[3])
        })
conn=engine.connect()
conn.execute(ins2, measures_list)

conn.execute("SELECT * FROM stations LIMIT 5").fetchall()