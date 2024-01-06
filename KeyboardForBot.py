from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Function to create a keyboard with specified buttons
def create_keyboard(*buttons):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for button_text in buttons:
        button = KeyboardButton(button_text)
        keyboard.add(button)
    return keyboard

# List of buttons
button_texts = ['/help', '/description', '/LogIn']

# Creating the keyboard using the function
keyboard = create_keyboard(*button_texts)
