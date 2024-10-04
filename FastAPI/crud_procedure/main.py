from fastapi import FastAPI, Request
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel, Field

try:
    conn = psycopg2.connect(host='localhost',
                            dbname='teams',
                            user='postgres',
                            password='sarthak7043',
                            port='5432',
                            cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("connected")
except Exception as e:
    print(f"Database connection error:{e}")

class Candidate(BaseModel):
    camp_id: int
    name: str
    phone: int
    email: str
    gender: str=Field(max_length=1)

app = FastAPI()

@app.middleware("http")
async def addmiddleware(request:Request,call_next):
    print('Middleware working')
    response = await call_next(request)
    print(response)
    return response

@app.get('/')
async def home():
    return {'Message':'Home Page'}

@app.get('/showCandidates')
async def showCandidates():
    query = 'select * from Candidates();'
    cursor.execute(query)
    records = cursor.fetchall()
    return records

@app.post('/addCandidates')
async def add_candidate(candidate:Candidate):
    # camp_id = candidate.camp_id
    # candidate_name = candidate.name
    # phone = candidate.phone
    # email = candidate.email
    # gender = candidate.gender
    # print("CALL addCandidate({},{},{},{},{})".format(candidate.camp_id,candidate.name,candidate.phone,candidate.email,candidate.gender))


    # cursor.execute("CALL sp_insert_Candidate_trial2({},'{}',{},'{}','{}')".format(candidate.camp_id,candidate.name,candidate.phone,candidate.email,candidate.gender))
    cursor.execute("select * from Insertcandidate({},'{}',{},'{}','{}')".format(candidate.camp_id,candidate.name,candidate.phone,candidate.email,candidate.gender))
    conn.commit()
    record = cursor.fetchall()
    return {'Result':record}
'''{
    "camp_id": 2,
    "name": "Nobody",
    "phone": 12345,
    "email": "nobody@gmail.com",
    "gender": "F"
}'''

@app.get('/show')
def pagination(limit:int,offset:int=0):
    if limit and offset:
        query = "SELECT * FROM showCandidates({},{});"
        cursor.execute(query.format(limit,offset))
        records = cursor.fetchall()
        return records

