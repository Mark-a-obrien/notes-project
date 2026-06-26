from fastapi import FastAPI
from db import *
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    title: str
    text: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/notes")
async def getNotes():
    return getAllNotesOnDB()

@app.post("/api/create/note")
async def create_note(note: Note):
    print(type(note))
    createNoteOnDB(note) 
    return note