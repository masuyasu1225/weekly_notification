import discord
from discord.ext import commands, tasks
from datetime import datetime
import pytz
from config import DISCORD_TOKEN

CHANNEL_ID = 1126337537070338211  # ← 実際のIDに置き換えてね

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user} (ID: {bot.user.id})')
    print("🟡 send_test_message.start() を呼び出します")
    send_test_message.start()

@tasks.loop(seconds=5)
async def send_test_message():
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    print(f"🕒 テスト送信処理：{now.strftime('%Y-%m-%d %H:%M:%S')}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"🔁 テスト送信：{now.strftime('%Y/%m/%d')}")
    else:
        print("⚠️ チャンネルが見つかりません。")

bot.run(DISCORD_TOKEN)
