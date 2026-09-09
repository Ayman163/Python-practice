import sqlite3

def init_db():
    conn = sqlite3.connect("traffic_system.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS violations  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            speed  INTEGER,
            speed_limit  INTEGER
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

init_db()
