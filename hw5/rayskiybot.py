from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Привет пользователь")
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Выберите язык : /rus, /eng, /uzb")


def adduser_function(update, context):
    user_name = update.message.from_user.username
    f = open(r'C:\Users\Windows 8\PycharmProjects\husan_prodect\usessers.txt', 'r')
    user_list = f.read().splitlines()
    f.close()
    if user_name in user_list:
        context.bot.send_message(chat_id=update.message.chat_id, text='Вы уже находитесь в наше базе данных')
    else:
        f = open(r'C:\Users\Windows 8\PycharmProjects\husan_prodect\usessers.txt', 'a')
        f.write(user_name + '\n')
        f.close()
        context.bot.send_message(chat_id=update.message.chat_id, text='вы были внесены в базу данных')
        print("Пользователь внесен файл")


def deluser_function(update, context):
    f = open(r'C:\Users\Windows 8\PycharmProjects\husan_prodect\usessers.txt')

    array_f = str(f.read()).split('\n')

    tmp_array = []
    for word in array_f:
        if word != update.message.from_user.username:
            tmp_array.append(word)
    f.close()
    f = open(r'C:\Users\Windows 8\PycharmProjects\husan_prodect\test_list', 'w')
    f.write(str('\n'.join(tmp_array)))
    context.bot.send_message(chat_id=update.message.chat_id, text='Данные успешно удалены!')


def rus_language(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Отлично, ты выбрал русский язык")


def eng_language(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="great you chose English")


def uzb_language(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="siz o'zbek tilini mukammal tanladingiz")

API_TOKEN = ''

updater = Updater(token=API_TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(CommandHandler("adduser", adduser_function))

dispatcher.add_handler(CommandHandler("deluser", deluser_function))

dispatcher.add_handler(CommandHandler("rus", rus_language))

dispatcher.add_handler(CommandHandler("eng", eng_language))

dispatcher.add_handler(CommandHandler("uzb", uzb_language))

updater.start_polling()

updater.idle()
