"""
Модуль для функций
"""
import time
import messege as msg
import answers as ans
import markup as mrk
from telegram.constants import CHATACTION_TYPING
from pars import *

def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.start_text.format(first_name)
    context.bot.send_message(chat_id=chat_id, text=text, reply_markup=mrk.button_1())


def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()
    if text == 'выбрать сеанс':
        context.bot.send_message(chat_id=chat_id,
                                 reply_markup=mrk.inline_button(),
                                 text='На какой день планируете посетить сеанс')
    else:
        send_text = ans.global_answers['rus'][text]
        context.bot.send_message(chat_id=chat_id,
                                 text=send_text,
                                 reply_markup=mrk.button())


def inline_reply(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    context.bot.send_message(chat_id=chat_id, text=qwe)
