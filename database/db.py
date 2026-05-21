import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('database/reviewer.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            filename TEXT,
            review_result TEXT,
            timestamp DATETIME,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

def save_review(user_id, filename, result):
    conn = sqlite3.connect('database/reviewer.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reviews (user_id, filename, review_result, timestamp) VALUES (?, ?, ?, ?)',
                   (user_id, filename, result, datetime.now()))
    conn.commit()
    conn.close()
