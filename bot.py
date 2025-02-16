import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import dotenv_values

config = dotenv_values()
bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    user = message.from_user
    user_id = user.id
    user_config = {
        "first_name": user.first_name,
        "addresses": [],
        "cashback_points": 0,
    }

    write_user_config(user_id=user_id, config=user_config)
    await message.reply(f"У меня есть обутки", {user.first_name})

async def main():
    print('Я работаю!')
    await dp.start_polling(bot)


asyncio.run(main())