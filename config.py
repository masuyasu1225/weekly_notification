from dotenv import load_dotenv
import os

# .env 明示的にパス指定して読み込み（これでほぼ確実）
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# デバッグ出力
if DISCORD_TOKEN is None:
    print("DISCORD_TOKEN が読み込めませんでした。")
else:
    print(f"トークン読み込み成功: {DISCORD_TOKEN[:5]}...")