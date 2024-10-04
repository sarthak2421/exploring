import json

from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

try:
    conn = psycopg2.connect(host='localhost', dbname='teams', user='postgres', password='sarthak7043', port="5432")#, cursor_factory=RealDictCursor
    cursor = conn.cursor()
    print('database connected')

    query = 'select * from players;'
    cursor.execute(query)
    print(cursor.fetchall())
    # data = cursor.fetchall()
    # print(json.dumps(data))
    cursor.close()
except Exception as e:
    print(e)