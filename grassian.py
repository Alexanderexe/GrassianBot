import telebot
import codecs
import random

bot = telebot.TeleBot()



fileObj = codecs.open( "grassian.txt", "r", "utf_8_sig" )
text = fileObj.read()

book = text.split("\r\n")
book = list(filter(lambda x : len(x) > 2, book))



upd = bot.get_updates()
last_update = upd[-1]
msg = last_update.message
@bot.message_handler(commands=['start'])
def handle_text(message):
    page = random.randint(0, 300)
    bot.send_message(message.chat.id, book[page])

bot.polling(none_stop=True)




