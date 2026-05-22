from scraper import get_new_posts
from downloader import download_video
from uploader_bot import upload_to_diskwala
from telegram_bot import send_post

import asyncio
import time


async def run_bot():

    posts = get_new_posts()

    for post in posts:

        title = post["title"]
        url = post["url"]

        print("DOWNLOADING...")
        video_path = download_video(url, "video.mp4")

        print("UPLOADING...")
        diskwala_link = await upload_to_diskwala(video_path)

        print("POSTING...")
        await send_post(title, diskwala_link)

        print("DONE")


while True:

    asyncio.run(run_bot())

    print("WAITING 5 MINUTES...")

    time.sleep(300)
