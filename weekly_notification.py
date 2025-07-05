from babel.dates import format_datetime
from datetime import datetime, timedelta
import pytz
import discord
from discord.ext import commands, tasks
from config import DISCORD_TOKEN

CHANNEL_ID = 1126337537070338211

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')
    send_mokumoku_message.start()

@tasks.loop(seconds=10)  # ← テスト用。運用時は minutes=1 に戻す
async def send_mokumoku_message():
    now = datetime.now(pytz.timezone("Asia/Tokyo"))

    # 今週土曜日を計算
    days_ahead = (5 - now.weekday()) % 7
    event_date = now + timedelta(days=days_ahead)

    # ✅ 日本語で日付＋曜日を整形（例：7/6(土)）
    date_str = format_datetime(event_date, "M/d(EEE)", locale="ja_JP")

    # メッセージ本文
    message = f"""{date_str} 9:00~12:00もくもく会
参加できる人→🙆‍♂️
参加できない人→🙅‍♀️
のどっちかをこのメッセージに押してね"""

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        sent = await channel.send(message)
        await sent.add_reaction("🙆‍♂️")
        await sent.add_reaction("🙅‍♀️")
    else:
        print("⚠️ チャンネルが見つかりません。")

bot.run(DISCORD_TOKEN)
