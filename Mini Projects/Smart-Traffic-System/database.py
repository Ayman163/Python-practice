import sqlite3 

DB_NAME = "traffic_system.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS violations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    speed INTEGER,
    speed_limit INTEGER
    )""")
    conn.commit()
    conn.close()

def add_violations(speed, speed_limit):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO violations (speed, speed_limit) VALUES (?, ?)", (speed, speed_limit))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_violations():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM violations")
    rows = cursor.fetchall()
    conn.close()
    return rows
