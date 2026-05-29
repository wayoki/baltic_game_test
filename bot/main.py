import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    WebAppInfo,
    MenuButtonWebApp,
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GAME_URL = os.getenv("GAME_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())

async def main():
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="Play",
            web_app=WebAppInfo(url=GAME_URL),
        )
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())