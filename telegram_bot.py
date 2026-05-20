from telegram import Bot

BOT_TOKEN = "8850623367:AAEipn5gBXE6PbpUbPZH-3yCeKkQQm-1d-U"

CHANNEL = "@summerrrrfiles"



def post_telegram(title, thumbnail, link):

    text = f"{title}\n\n{link}"

    bot.send_photo(
        chat_id=CHANNEL,
        photo=thumbnail,
        caption=text
    )
