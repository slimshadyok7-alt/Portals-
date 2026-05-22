from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_new_posts():

    options = Options()

    options.binary_location = "/data/data/com.termux/files/usr/bin/chromium"

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    url = "https://xbaaz.com/#_"

    driver.get(url)

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    driver.quit()

    posts = []

    links = soup.find_all("a")

    for link in links[:20]:

        href = link.get("href")

        if href and "http" in href:

            posts.append({
                "title": link.text.strip() or "Video",
                "url": href
            })

    return posts
