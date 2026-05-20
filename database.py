import sqlite3

conn = sqlite3.connect("posts.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    post_url TEXT PRIMARY KEY,
    title TEXT,
    thumbnail TEXT,
    video_url TEXT,
    uploaded_link TEXT,
    posted INTEGER DEFAULT 0
)
""")

conn.commit()
