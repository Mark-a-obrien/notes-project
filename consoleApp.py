from db import *
from pydantic import BaseModel


class note(BaseModel):
    title:str
    text:str

def createNote():
    title = input("Enter title: ")
    text = input("Enter text: ")
    note.title =  title
    note.text = text
    createNoteOnDB(note) 

def displayAllNotes():
    for i in getAllNotesOnDB():
        print(i)

def displayMenu():
    print("\n\tMenu\n1 : Display all notes\n2 : Create note\n3 : Delete note by ID\n4 : Search for note by title\n0 : Exit")

def deleteNoteById():
    id = input("Enter ID: ")
    deleteByIdOnDB(id)

def searchByTitle():
    title = input("Enter note title:")
    print(searchByTitleOnDB(title))
    

running = True
while running:
    displayMenu()
    num = input("Enter: ")
    if num == "1":
        displayAllNotes()
    elif num == "2":
        createNote()
        displayAllNotes()
    elif num == "3":
         deleteNoteById()
         displayAllNotes()
    elif num == "4":
         searchByTitle()
    elif num == "0":
        running = False

