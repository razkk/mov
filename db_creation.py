# !/usr/bin/python
# -*- encoding: utf-8-*-
import sqlite3
import sys



conn = sqlite3.connect('mymov.db')
cur = conn.cursor()
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='stops'"
tb_create= "CREATE TABLE `stops` " \
           "(stop_id VARCHAR(255) NOT NULL PRIMARY KEY, " \
           "stop_code VARCHAR(255), " \
           "stop_name VARCHAR(255), " \
           "stop_desc VARCHAR(255), " \
           "stop_lat DECIMAL(8,6), " \
           "stop_lon DECIMAL(8,6), " \
           "location_type INT(2), " \
           "parent_station VARCHAR(255), " \
           "zone_id VARCHAR(255))"

    #"CREATE TABLE `stops` " \
              #"(stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,location_type,parent_station,zone_id)"
if not cur.execute(tb_exists).fetchone():
    cur.execute(tb_create)

st_file=open('ipt/stops.txt')
stops=st_file.readlines()
st_file.close()

for line in stops:
    token=line.split(',')
    for i in range(0,len(token),1): token[i]=unicode(token[i],"utf-8")
    cur.execute("INSERT OR IGNORE INTO stops VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",token)
    #cur.execute("update stops set stop_id = stop_code, stop_code = stop_id")
conn.commit()



tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='stop_times'"
tb_create= "CREATE TABLE `stop_times` ( " \
        "trip_id VARCHAR(255), " \
        "arrival_time VARCHAR(8), " \
        "departure_time VARCHAR(8), " \
	    "stop_id VARCHAR(255)," \
	    "stop_sequence VARCHAR(255), " \
	    "pickup_type INT(2), " \
	    "drop_off_type INT(2), " \
	    "shape_dist_traveled VARCHAR(8), " \
	    "FOREIGN KEY (trip_id) REFERENCES trips(trip_id), " \
	    "FOREIGN KEY (stop_id) REFERENCES stops(stop_id))"

if not cur.execute(tb_exists).fetchone():
    cur.execute(tb_create)

st_tm_file=open('ipt/stop_times.txt')
stop_times=st_tm_file.readlines()
st_tm_file.close()

for line in stop_times:
    token=line.split(',')
    for i in range(0,len(token),1): token[i]=unicode(token[i],"utf-8")
    cur.execute("INSERT OR IGNORE INTO stop_times VALUES (?, ?, ?, ?, ?, ?, ?, ?)",token)
conn.commit()



tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='trips'"

tb_create = "CREATE TABLE `trips` ("\
	    "route_id VARCHAR(255) NOT NULL PRIMARY KEY,"\
	    "service_id VARCHAR(255),"\
	    "trip_id VARCHAR(255),"\
	    "direction_id TINYINT(1),"\
	    "shape_id VARCHAR(255))"

if not cur.execute(tb_exists).fetchone():
    cur.execute(tb_create)

trips_file=open('ipt/trips.txt')
trips=trips_file.readlines()
trips_file.close()

for line in trips:
    token=line.split(',')
    for i in range(0,len(token),1): token[i]=unicode(token[i],"utf-8")
    cur.execute("INSERT OR IGNORE INTO trips VALUES (?, ?, ?, ?, ?)",token)
conn.commit()

tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='routes'"
tb_create= "CREATE TABLE `routes` ("\
    	"route_id VARCHAR(255) NOT NULL PRIMARY KEY,"\
	    "agency_id VARCHAR(255),"\
	    "route_short_name VARCHAR(50),"\
	    "route_long_name VARCHAR(255),"\
	    "route_desc VARCHAR(255),"\
    	"route_type INT(2),"\
    	"route_color VARCHAR(20))"

if not cur.execute(tb_exists).fetchone():
    cur.execute(tb_create)

routes_file=open('ipt/routes.txt')
routes=routes_file.readlines()
routes_file.close()

for line in routes:
    token=line.split(',')
    for i in range(0,len(token),1): token[i]=unicode(token[i],"utf-8")
    cur.execute("INSERT OR IGNORE INTO routes VALUES (?, ?, ?, ?, ?, ?, ?)",token)
conn.commit()


conn.close()


