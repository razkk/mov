import sqlite3

conn= sqlite3.connect('mymov.db')
cur=conn.cursor()

find_origin_stop_id="SELECT * FROM stops WHERE stop_code='25635'"
cur.execute(find_origin_stop_id)
origin_id=cur.fetchone()[0]  #change to fetchone instide all

find_dest_stop_id="SELECT * FROM stops WHERE stop_code='21127'"
cur.execute(find_dest_stop_id)
dest_id=cur.fetchone()[0]
print "Origin id: ",origin_id
print "Destination id: ",dest_id

find_stop_id_routes="SELECT * FROM stop_times WHERE stop_id=?"
#origin routes
cur.execute(find_stop_id_routes, (origin_id,))
origin_trips=[]
for row in cur.fetchall():
     origin_trips.append(row[0])
print "Trips that goes through origin station: ",origin_trips
#destination routs
cur.execute(find_stop_id_routes, (dest_id,))
dest_trips=[]
for row in cur.fetchall():
     dest_trips.append(row[0])
print "Trips that goes through destination station: ",dest_trips


shared_trips= [val for val in origin_trips if val in dest_trips]
shared_trips=set(shared_trips)
shared_trips=list(shared_trips)
print "Shared trips for both origin and destination: ",shared_trips

find_shared_routes="SELECT * FROM trips WHERE trip_id=?"
#print shared_trips[0]
shared_routes=[]
for trip in shared_trips:
    cur.execute(find_shared_routes,(trip,))
    res=cur.fetchone()
    if res: shared_routes.append(res[0])

print shared_routes

find_line_from_route="SELECT * FROM routes WHERE route_id=?"
lines=[]
for route in shared_routes:
    cur.execute(find_line_from_route,(route,))
    res= cur.fetchone()
    lines.append(res[2])

print "Lines are:", set(lines)
conn.close()