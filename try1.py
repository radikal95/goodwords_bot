import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types='text')
def default_answer(message):
    bot.send_message(message.chat.id, "You are not authorized")
pass

bot.polling(none_stop=True)