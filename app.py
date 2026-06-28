from fastapi import FastAPI
from db import *
from pydantic import BaseModel

from dotenv import load_dotenv
import os

app = FastAPI()

class Note(BaseModel):
    title: str
    text: str

class ApiCall(BaseModel):
    api_key: str
    note: Note

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/notes")
async def getNotes():
    return getAllNotesOnDB()

@app.post("/api/create/note")
async def create_note(apiCall: ApiCall):
    if not checkApiKey(apiCall.api_key): return {"message": "Invalid api key"}

    createNoteOnDB(apiCall.note) 
    return apiCall.note
    

def checkApiKey(api_key):
    load_dotenv()
    saved_api_key = os.getenv('api_key')

    if api_key == saved_api_key:
        return True
    return False