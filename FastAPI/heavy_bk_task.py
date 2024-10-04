from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

@app.get('/')
def home():
    return {'Message':"Hello!"}

def task(name:str):
    time.sleep(5)
    print(f'Task completed for {name}')

@app.post('/perform')
def perform(name:str, background_tasks : BackgroundTasks):
    background_tasks.add_task(task,name)
    return{'Message':f'Task started for {name}'}
