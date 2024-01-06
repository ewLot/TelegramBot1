from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from KeyboardForBot import keyboard

load_dotenv()
bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot has started!')


async def send_message_to_user(user_id, text, parse_mode="MarkdownV2", reply_markup=None):
    await bot.send_message(chat_id=user_id, text=text, parse_mode=parse_mode, reply_markup=reply_markup)


# Command texts in Markdown format
TextForHelper = """
*Commands:*
`/start` - Start working with the Telegram bot
`/help` - List of bot commands"""

TextForDescription = """
*Description:*
The **Student Laundry Service** bot is still under development...
"""


# Command handlers
@dp.message_handler(commands=['start'])
async def say_hello(message: types.Message):
    await send_message_to_user(
        message.from_user.id,
        "Welcome to our Telegram bot!",
        parse_mode="MarkdownV2",
        reply_markup=keyboard
    )
    await message.delete()


@dp.message_handler(commands=['help'])
async def show_helper(message: types.Message):
    await send_message_to_user(
        message.from_user.id,
        TextForHelper,
        parse_mode="MarkdownV2"
    )


@dp.message_handler(commands=['description'])
async def show_description(message: types.Message):
    await send_message_to_user(
        message.from_user.id,
        TextForDescription,
        parse_mode="MarkdownV2"
    )


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)