import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()

    # ---- course table ----
    cur.execute("""
    CREATE TABLE IF NOT EXISTS course(
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        duration TEXT,
        charges TEXT,
        description TEXT
    )
    """)
    con.commit()

    # ---- student table ----
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        roll INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        admission TEXT,
        course TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
    """)
    con.commit()

    # ---- result table ----
    cur.execute("""
    CREATE TABLE IF NOT EXISTS result(
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT,
        name TEXT,
        course TEXT,
        marks_ob TEXT,
        full_marks TEXT,
        per TEXT
    )
    """)
    con.commit()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        fname text,
        lname text,
        contact text,
        email text,
        question text,
        answer text,
        password text
    )
    """)
    con.commit()

    

    con.close()

create_db()
