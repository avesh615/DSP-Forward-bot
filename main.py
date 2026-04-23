from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('session', api_id, api_hash)

source_chat = -1001522451083
target_chat = -5157096380

keywords = ['CJG', 'CJF', 'C45']

@client.on(events.NewMessage(chats=source_chat))
async def handler(event):
    msg = event.message.message

    if msg and any(k in msg for k in keywords):
        await client.forward_messages(target_chat, event.message)

client.start()
print("🔥 Bot Started...")
client.run_until_disconnected()
