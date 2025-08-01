import os
from pyrogram import Client, filters

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_string = os.environ["SESSION_STRING"]
from_chat_id = int(os.environ["FROM_CHAT_ID"])
to_chat_id = int(os.environ["TO_CHAT_ID"])

app = Client(
    name="my_bot",
    session_string=session_string,
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters.chat(from_chat_id))
async def forward_message(client, message):
    try:
        await message.forward(to_chat_id)
        print(f"✅ Message forwarded from {from_chat_id} to {to_chat_id}")
    except Exception as e:
        print(f"❌ Failed to forward message: {e}")

app.run()