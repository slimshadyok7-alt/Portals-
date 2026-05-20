from flask import Flask
from threading import Thread
import os
import time
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

print("PLAYWRIGHT WORKING")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())

while True:
    time.sleep(60)
