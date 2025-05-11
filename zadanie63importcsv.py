import csv
from zadanie63 import engine, stations, measures

ins = stations.insert()

stations_list = []

with open("clean_stations.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)
    next(reader)
    next(reader)

    for row in reader:
        stations_list.append({
            'station': row[0],
            'latitude': float(row[1]),
            'longitude': float(row[2]),
            'elevation': float(row[3]),
            'name': row[4],
            'country': row[5],
            'state': row[6]
        })
conn=engine.connect()
conn.execute(ins, stations_list)


ins2=measures.insert()
measures_list=[]

with open("clean_measures.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        measures_list.append({
            'station': row[0],
            'date': (row[1]),
            'precip': float(row[2]),
            'tobs': int(row[3])
        })

conn.execute(ins2, measures_list)