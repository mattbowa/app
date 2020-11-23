import time

import redis
from flask import Flask
import psycopg2 #

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)
cache = redis.Redis(host='redis', port=6000)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def pg_db():    
    connection = psycopg2.connect(user = "postgres",
                                  password = "matt1234",
                                  host = "postgres12_db",
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM cities"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall() 
   
    print("Print each row and it's columns values")
    for row in mobile_records:
        global city_name
        city_name = row[0]
        print("Variable type = ", type(row[0]), )
        print("Name = ", row[0], )
        print("Location = ", row[1], "\n")
    #return "Hello World!"
    return city_name


@app.route('/')
def hello():
    #count = get_hit_count()
    #return 'Hello World!55 I have been seen {} times.\n'.format(count)
    x = pg_db()
    return x


