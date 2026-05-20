import requests
from bs4 import BeautifulSoup
from database import conn, cursor

SOURCE = "https://YOUR_SOURCE_SITE.com"

def scrape():

    html = requests.get(SOURCE).text

    soup = BeautifulSoup(html, "html.parser")

    posts = soup.find_all("a")

    for post in posts:

        try:

            url = post.get("href")

            if not url:
                continue

            if not url.startswith("http"):
                continue

            cursor.execute(
                "SELECT * FROM posts WHERE post_url=?",
                (url,)
            )

            exists = cursor.fetchone()

            if exists:
                continue

            title = post.text.strip()

            thumbnail = "https://example.com/thumb.jpg"

            video_url = url

            cursor.execute("""
            INSERT INTO posts (
                post_url,
                title,
                thumbnail,
                video_url
            ) VALUES (?, ?, ?, ?)
            """, (
                url,
                title,
                thumbnail,
                video_url
            ))

            conn.commit()

            print("NEW:", title)

        except Exception as e:

            print(e)
