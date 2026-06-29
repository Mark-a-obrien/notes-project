from fastapi import FastAPI
from db import *
from pydantic import BaseModel

from dotenv import load_dotenv
import os

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

app = FastAPI()

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

class Note(BaseModel):
    title: str
    text: str

class ApiCall(BaseModel):
    api_key: str
    note: Note

def get_api_key(api_key_header: str = Depends(api_key_header)):
    if checkApiKey(api_key_header):
        return api_key_header
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key"
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/notes")
async def getNotes(api_key: str = Depends(get_api_key)):
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