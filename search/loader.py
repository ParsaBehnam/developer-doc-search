import sqlite3

def get_articles():
    conn = sqlite3.connect('./data/articles.db')
    cursor = conn.cursor()

    cursor.execute("SELECT url, title, content FROM articles")

    articles = cursor.fetchall()

    conn.close()

    return articles