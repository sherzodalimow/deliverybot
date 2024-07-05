# Knopki
from telebot import types

# knopka otpravka nomera

def num_button():
    # sozdayom prostranstvo
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # sozdayom knpoki
    but1 = types.KeyboardButton("Send number📞", request_contact=True)
    # dobovlyaem prostranstvo
    kb.add(but1)
    return kb

