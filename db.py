import sqlite3
con = sqlite3.connect("notes.db")
cur = con.cursor()

def createNoteTable():
    cur.execute("CREATE TABLE note(id, title, text)")


def createNoteOnDB():
    cur.execute("""
    INSERT INTO note VALUES
        (0, "This is a note babyyyyyyyyyyyyy", "This is the note."),
        (1, "Note note", "Super secret note.")
    """)
    con.commit()


def getAllNotes():
    res = cur.execute("SELECT * FROM note")
    return res.fetchall()


print(getAllNotes())