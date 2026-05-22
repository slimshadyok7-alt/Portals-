from telegram import Bot

BOT_TOKEN = "8850623367:AAEipn5gBXE6PbpUbPZH-3yCeKkQQm-1d-U"
CHANNEL_ID = "@summerrrrfiles"

bot = Bot(token=BOT_TOKEN)


async def send_post(title, link):

    text = f"""
🎬 {title}

🔗 {link}
"""

    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=text
    )
