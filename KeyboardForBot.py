from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,        # "Сжимает" клавиатуру под размеры интерфейса пользователя
                               #one_time_keyboard=True       # Скрывает клавиатуру после нажатия кнопки
                               )

button1 = KeyboardButton('/help')
button2 = KeyboardButton('/description')
button3 = KeyboardButton('/LogIn')



keyboard.add(button1, button2)
keyboard.add(button3)
