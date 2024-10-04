from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel, Field
import psycopg2
from typing import Optional

try:
    conn = psycopg2.connect(host='localhost',
                            dbname='teams',
                            user='postgres',
                            password='sarthak7043',
                            port='5432')#,
                            #cursor_factory=RealDictCursor
    cursor = conn.cursor()
    print("connected")
except Exception as e:
    print(f"Database connection error:{e}")

app = FastAPI()

class Person(BaseModel):
    name: str = Field(min_length=4)
    occupation: str
    age: int

@app.get('/')
async def home():
    return {'Message':'Welcome!!'}

@app.get('/show')
async def show():
    query = 'select * from person;'
    cursor.execute(query)
    records = cursor.fetchall()
    return records

@app.post('/add')
async def add(person: Person):
    query = "insert into person(name,occupation,age) values ('{}','{}',{});"
    try:
        cursor.execute(query.format(person.name,person.occupation,person.age))
        conn.commit()
        return {'Message':'Record added successfully'}
    except Exception as e:
        print(f"Error while adding data : {e}")

@app.put('/update/{id}')
async def update(id:int,person: Person):
    query = "update person set name='{}', occupation='{}', age = {} where id = {}"
    try:
        cursor.execute(query.format(person.name,person.occupation,person.age,id))
        conn.commit()
        return {'message':'record updated successfully'}
    except Exception as e:
        print(f"Error while updating data : {e}")

@app.delete('/delete')
async def delete(id:int):
    query = f"delete from person where id={id};"
    try:
        cursor.execute(query)
        conn.commit()
        return {'message':'record deleted successfully'}
    except Exception as e:
        print(f"Error while deleting data : {e}")







