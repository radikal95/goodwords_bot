import requests
import config
import telebot
import compliments
from telebot import types
from db_tool import DbQuery

# db_query = DbQuery()
bot = telebot.TeleBot(config.token)


# def process(message):
#     query = """SELECT full_name,status,id
#     	        FROM public."user"
#                 WHERE id={};"""
#     query_result = db_query.execute_query(query.format(message.chat.id))
#     if len(query_result.value)<1:
#         return [False]
#     else:
#         return [True, query_result.value[0][1]]
#
# #status:
# #0 - send comp
# #1 - wait for user's comp
#
# @bot.message_handler(commands=['start'])
# def insert_into_a_db(message):
#     bot.send_message(message.chat.id, 'Test')
#     query = """SELECT full_name,status,id
# 	        FROM public."user"
#             WHERE id={};"""
#     query_result=db_query.execute_query(query.format(message.chat.id))
#     if len(query_result.value)<1:
#         query ="""INSERT INTO public."user"(full_name,
#                                         status,
#                                         id)
# 	                                    VALUES ('{}', 0, {});"""
#         name = 'Unknown user'
#         if message.chat.first_name:
#             name = str(message.chat.first_name)
#         if message.chat.last_name:
#             name = name + ' ' + str(message.chat.last_name)
#         query_result=db_query.execute_query(query.format(name,message.chat.id),is_dml=True)
#         if (query_result.success):
#             bot.send_message(message.chat.id, "Теперь ты среди нас! Добро пожаловать!")
#     else:
#         bot.send_message(message.chat.id, "C возвращением!")
#     pass
#
#
# @bot.message_handler(regexp='Предложить свой комплимент')
# def change_status(message):
#     query =  """UPDATE public."user"
# 	            SET status=1
# 	            WHERE id={};"""
#     query_result = db_query.execute_query(query.format(message.chat.id), is_dml=True)
#     if (query_result.success):
#         bot.send_message(message.chat.id, "Я тебя слушаю")
#     else:
#         bot.send_message(message.chat.id, "Я тебя не слушаю")
#
#
#
# @bot.message_handler(func=lambda message: process(message)[0])
# def dialog(message):
#     if process(message)[1] == 0:
#          keyboard = types.ReplyKeyboardMarkup()
#          ask_button = types.KeyboardButton(text="Скажи что-то хорошее")
#          send_button = types.KeyboardButton(text="Предложить свой комплимент")
#          keyboard.add(ask_button, send_button)
#          bot.send_message(message.chat.id, compliments.random_compliment(), reply_markup=keyboard)
#     elif process(message)[1] == 1:
#         query = """UPDATE public."user"
#          	            SET status=0
#          	            WHERE id={};"""
#         query_result = db_query.execute_query(query.format(message.chat.id), is_dml=True)
#         query = """INSERT INTO public.temp
#                     (value, "user")
# 	                VALUES ('{}',{});"""
#         query_result = db_query.execute_query(query.format(message.text,message.chat.id), is_dml=True)
#         query = """SELECT id
#              	        FROM public."temp"
#                          WHERE "user"={} AND value = '{}'
#                          LIMIT 1;"""
#         query_search = db_query.execute_query(query.format(message.chat.id,message.text))
#         if (query_result.success):
#             bot.send_message(message.chat.id, "Записал")
#             bot.send_message(config.admin_id, "Новый комплимент!")
#             keyboard = types.InlineKeyboardMarkup()
#             bump_button = types.InlineKeyboardButton(text="BUMP", callback_data='B'+str(query_search.value[0][0]))
#             sage_button = types.InlineKeyboardButton(text="SAGE", callback_data='S'+str(query_search.value[0][0]))
#             keyboard.add(bump_button,sage_button)
#             bot.forward_message(config.admin_id,message.chat.id,message.message_id)
#             bot.send_message(config.admin_id, 'Choose', reply_markup=keyboard)
#         else:
#             bot.send_message(message.chat.id, "Не записал")
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if 'B' in call.data:
#         id = call.data.replace('B','')
#         query = """SELECT value,"user" FROM public."temp"
#                                  WHERE id={};"""
#         query_search = db_query.execute_query(query.format(id))
#         compliments.compliment.append(query_search.value[0][0])
#         query = """DELETE FROM public."temp"
#                                          WHERE id={};"""
#         query_delete = db_query.execute_query(query.format(id),is_dml=True)
#         bot.send_message(query_search.value[0][1],'Ваш комплимент добавлен, спасибо!')
#         bot.send_message(config.admin_id,'Успешно добавлено')
#
#     else:
#         id = call.data.replace('S', '')
#         query = """SELECT "user" FROM public."temp"
#                                          WHERE id={};"""
#         query_search = db_query.execute_query(query.format(id))
#         query = """DELETE FROM public."temp"
#                                          WHERE id={};"""
#         query_delete = db_query.execute_query(query.format(id),is_dml=True)
#         bot.send_message(query_search.value[0][0], 'Ваш комплимент удалён, сожалеем!')
#         bot.send_message(config.admin_id,'Успешно удалено')
#


@bot.message_handler(content_types='text')
def handle_message(message):
    bot.send_message(message.chat.id, compliments.random_compliment())
pass

print('Start')
while True:
    try:
        bot.polling(none_stop=True)
    except:
        continue