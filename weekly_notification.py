from babel.dates import format_datetime
from datetime import datetime, timedelta
import pytz
import discord
from discord.ext import commands, tasks
from config import DISCORD_TOKEN

CHANNEL_ID = 1377628282471841914

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')
    send_mokumoku_message.start()

@tasks.loop(minutes=1)
async def send_mokumoku_message():
    now = datetime.now(pytz.timezone("Asia/Tokyo"))

    # ✅ 土曜の昼12:00だけ投稿（12:00:00〜12:00:59）
    if now.weekday() == 5 and now.hour == 12 and now.minute == 0:
        event_date = now + timedelta(days=7)  # ✅ 次週の土曜日
        date_str = format_datetime(event_date, "M/d(EEE)", locale="ja_JP")

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
