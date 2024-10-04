from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

try:
    conn = URL.create(host='localhost',
                      database='teams',
                      username='postgres',
                      password='sarthak7043',
                      port=5432,
                      drivername="postgresql")

                            #cursor_factory=RealDictCursor
    engine = create_engine(conn)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("connected")
except Exception as e:
    print(f"Database connection error:{e}")

app = FastAPI()

class Person(BaseModel):
    name: str
    occupation: str
    age: int






