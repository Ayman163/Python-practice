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
