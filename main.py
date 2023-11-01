from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from SomeCon import TOKEN
from KeyboardForBot import keyboard

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('I have been started up!')


TextForHelper = """
<em>/start</em> - начать работу с телеграмм ботом
<em>/help</em> - список команд бота"""

TextForDescription = """
Бот <u><strong>Student laundry service</strong></u> ещё в процессе разработки...
"""



@dp.message_handler(commands=['start'])
async def SayHello(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш Телеграмм бот!",
                           parse_mode="HTML",
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=['help'])
async def ShowHelper(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=TextForHelper,
                           parse_mode="HTML",)


@dp.message_handler(commands=['description'])
async def ShowDescription(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=TextForDescription,
                           parse_mode="HTML")



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
