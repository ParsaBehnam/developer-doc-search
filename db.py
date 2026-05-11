import sqlite3

def create_database():
    conn = sqlite3.connect('./data/articles.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   url TEXT UNIQUE,
                   title TEXT,
                   content TEXT)
    """)

    conn.commit()
    conn.close()

