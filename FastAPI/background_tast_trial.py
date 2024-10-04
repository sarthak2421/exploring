import time

import uvicorn
from fastapi import BackgroundTasks, FastAPI
import asyncio
app = FastAPI()

async def write_notification(email: str, message=""):
    await asyncio.sleep(2)
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some msg")
    return {"message": "Notification sent in the background"}

if __name__ == "__main__":
    uvicorn.run(app,port=2000)