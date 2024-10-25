from bot.main_bot import MainBot
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


TOKEN = os.getenv('TOKEN')

def start_bot():
    try: 
        main_bot = MainBot()
        main_bot.run(TOKEN)
    except Exception as e:
        print(e)

start_bot()



