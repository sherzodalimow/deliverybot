import telebot
import button as bt
import DB as db

# sozdayom obyekt bota
bot = telebot.TeleBot("6539005051:AAGTlvqN1UFCWm5L2Hr9z-cP1HIeYfy3VIA")

# obrabotka komandi start

@bot.message_handler(commands=["start"])
def start_message(msg):
    user_id = msg.from_user.id
    check = db.check_user(user_id)

    if check:
        bot.send_message(user_id, "Hi, welcome!")
    else:
        bot.send_message(user_id, "Hi, lets register!\n"
                         "Write your name")
        # perexod na etap poluceniya imeni

    bot.register_next_step_handler(msg,get_name)

#etap poluceniya imeni
def get_name(msg):
    user_id = msg.from_user.id
    user_name = msg.text

    bot.send_message(user_id, "Cool, now send ur number!",
                     reply_markup=bt.num_button())

    #perexod na etap poluceniya nomera
    bot.register_next_step_handler(msg, get_number, user_name)

# etap poluceniya nomer
def get_number(msg, user_name):
    user_id = msg.from_user.id
    # esli polzovatel otrpavil po knopke
    if msg.contact:
        user_number = msg.contact.phone_number
        db.register(user_id, user_name, user_number)
        bot.send_message(user_id, "Registration succsfull",
                 reply_markup=telebot.types.ReplyKeyboardRemove())

    # esli polzovatel ne otpravil nam kontakt ne po knopke a napisal
    else:
        bot.send_message(user_id, "Send your number via button")
        # vozvrat na etap poluceniya nomera
        bot.register_next_step_handler(msg, get_number, user_name)

# zapusk bota

bot.polling()



