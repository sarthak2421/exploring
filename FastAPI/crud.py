from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

class Member(BaseModel):
    playerid: int
    playername: str

try:
    conn = psycopg2.connect(host='localhost',
                            dbname='teams',
                            user='postgres',
                            password='sarthak7043',
                            port='5432')
    cursor = conn.cursor()
    print("connected")
except Exception as e:
    print(f"Database connection error:{e}")

try:
    app = FastAPI()

    @app.get('/')
    async def show():
        query = 'select * from players;'
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        return records

    @app.post('/add')
    async def add(id:int, name:str):
        query = f"INSERT INTO players(playerid,playername)VALUES({id},'{name}');"
        try:
            cursor.execute(query)
            return {'Message':'Records updated'}
        except Exception as e:
            print(e)
            return {'Error':f'{e}'}

    @app.put('/update')
    def update(id:int,name:str):
        try:
            query = f"update players set playername='{name}' where playerid={id};"
            cursor.execute(query)
            return {'Message': 'Records updated'}
        except Exception as e:
            print(f"Error while updating: {e}")

except Exception as e:
    print(e)