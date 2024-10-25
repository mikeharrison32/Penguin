from bot.main_bot import MainBot
import os
from dotenv import load_dotenv
from flask import Flask
import threading
import os
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('TOKEN')

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=os.getenv("PORT", 5000))


def start_bot():
    try: 
        main_bot = MainBot()
        main_bot.run(TOKEN)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    threading.Thread(target=run).start()

    start_bot()
