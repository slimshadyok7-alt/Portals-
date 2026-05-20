from flask import Flask
from threading import Thread
import os
import time

from database import conn, cursor
from scraper import scrape
from downloader import download_video
from uploader import upload
from telegram_bot import post_telegram

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running"

def run_web():

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

while True:

    try:

        scrape()

        cursor.execute("""
        SELECT
        post_url,
        title,
        thumbnail,
        video_url
        FROM posts
        WHERE posted=0
        """)

        posts = cursor.fetchall()

        for post in posts:

            post_url, title, thumbnail, video_url = post

            print("PROCESSING:", title)

            filepath = download_video(
                video_url,
                "video.mp4"
            )

            uploaded_link = upload(filepath)

            post_telegram(
                title,
                thumbnail,
                uploaded_link
            )

            cursor.execute("""
            UPDATE posts
            SET posted=1,
            uploaded_link=?
            WHERE post_url=?
            """, (
                uploaded_link,
                post_url
            ))

            conn.commit()

            print("DONE:", title)

    except Exception as e:

        print(e)

    time.sleep(300)
