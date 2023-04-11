import psycopg2
from models import Station

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
)

cur = conn.cursor()


def request2db(req):
    cur.execute(req)
    stationsFromDB = cur.fetchall()

    stations = []

    for i in stationsFromDB:
        stations.append(Station(i[1], i[2], i[3]))


def main():
    request2db('select * from stations')


main()
