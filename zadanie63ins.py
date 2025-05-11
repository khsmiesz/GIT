from zadanie63 import engine, stations
ins=stations.insert().values(station='USC00519397',latitude='21.2716',longitude='-157.8168',elevation='3.0',name='WAIKIKI 717.2',country='US',state='HI')
conn=engine.connect()
result=conn.execute(ins)
conn.execute(ins, [{'station':'USC00513117','latitude':21.4234,'longitude':-157.8015, 'elevation':14.6, 'name':'KANEOHE 838.1','country':'US','state':'HI'},
                    {'station':'USC00514830','latitude':21.5213,'longitude':-157.8374,'elevation':7.0,'name':'KUALOA RANCH HEADQUARTERS 886.9','country':'US','state':'HI'}])
