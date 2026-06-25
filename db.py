import sqlite3
con = sqlite3.connect("notes.db")
cur = con.cursor()

def createNoteTable():
    cur.execute("CREATE TABLE note(id INTEGER PRIMARY KEY AUTOINCREMENT, title, text)")

def createNoteOnDB(note):
    cur.execute(f"""
    INSERT INTO note (title, text)
        VALUES 
        ("{note['title']}", "{note['text']}")
    """)
    con.commit()

def getAllNotesOnDB():
    res = cur.execute("SELECT * FROM note")
    return res.fetchall()

def searchByTitleOnDB(title):
    cur.execute("SELECT * FROM note WHERE title LIKE ?", (f'%{title}%',))
    results = cur.fetchall()
    return results

def deleteByIdOnDB(id):
    cur.execute(f"Delete FROM note WHERE ID={id}")
    con.commit()


