import sqlite3
import os

def create_db():    
    con = sqlite3.connect(database=r'rms.db')
    cur = con.cursor()
    
    # Employee Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            eid INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            doj TEXT,
            pass TEXT,
            role TEXT,
            address TEXT,
            salary TEXT
        )
    """)
    con.commit()
    
    # Category Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS category(
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    con.commit()
    
    # Items Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items(
            itm_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            name TEXT,
            price TEXT,
            qty TEXT,
            status TEXT
        )
    """)
    con.commit()
    
    # Tables Management Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tables(
            tid INTEGER PRIMARY KEY AUTOINCREMENT,
            table_no TEXT UNIQUE NOT NULL,
            waitress TEXT,
            cleaner TEXT,
            water_boy TEXT,
            time_slot TEXT,
            table_date TEXT
        )
    """)
    con.commit()
    
    # Ensure `table_date` column exists if the table was created earlier without it
    try:
        cur.execute("ALTER TABLE tables ADD COLUMN table_date TEXT")
        con.commit()
    except sqlite3.OperationalError:
        # Column already exists
        pass
    
    con.close()

# Call to create or update the database schema
create_db()
