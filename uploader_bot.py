from telethon import TelegramClient
import asyncio

API_ID = 35285611
API_HASH = "42b062be538da1c4542ea4e8c8caa4ce"

PHONE = "+919970998820"

BOT_USERNAME = "@DiskWalaFileUploaderBot"

client = TelegramClient(
    "diskwala_session",
    API_ID,
    API_HASH
)

async def upload_to_diskwala(filepath):

    await client.start(PHONE)

    print("UPLOADING...")

    await client.send_file(
        BOT_USERNAME,
        filepath
    )

    await asyncio.sleep(20)

    messages = await client.get_messages(
        BOT_USERNAME,
        limit=1
    )

    text = messages[0].message

    print(text)

    return text

def upload(filepath):

    return asyncio.run(
        upload_to_diskwala(filepath)
    )
