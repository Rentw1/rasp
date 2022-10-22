import telebot

from telebot import types  # для указание типов

bot = telebot.TeleBot("5681453808:AAHZJMS0Md_LuyetyG08wGZzjG5ettBzkcg")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Уголовный процесс(Экзамен)")
    btn2 = types.KeyboardButton("СВТ(Экзамен)")
    btn3 = types.KeyboardButton("АДП(Зачет)")
    btn4 = types.KeyboardButton("Дискретная математика(Зачет)")
    btn5 = types.KeyboardButton("Огневая подготовка(Диф. зачет)")
    btn6 = types.KeyboardButton("ОПД(Зачет)")
    btn7 = types.KeyboardButton("СПФП(Диф. зачет)")
    btn8 = types.KeyboardButton("Физика(Зачет)")
    btn9 = types.KeyboardButton("Языки программирования(Экзамен)")
    btn10 = types.KeyboardButton("Первая помощь(Зачет)")
    btn11 = types.KeyboardButton("Мат. анализ(Зачет)")
    btn12 = types.KeyboardButton("Иностранный язык(Зачет)")
    btn13 = types.KeyboardButton("Полный список расписания зимней сессии")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для выведения расписания по зимней сессии".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Уголовный процесс(Экзамен)"):
        bot.send_message(message.chat.id, text="Среда - 21.12.2022")
        bot.send_document(message.chat.id, document=open('YG.pdf', 'rb'))
    elif (message.text == "СВТ(Экзамен)"):
        bot.send_message(message.chat.id, text="Суббота - 24.12.2022")
        bot.send_document(message.chat.id, document=open('SVT.pdf', 'rb'))
    elif (message.text == "АДП(Зачет)"):
        bot.send_message(message.chat.id, text="Среда - 23.11.2022")
        bot.send_document(message.chat.id, document=open('ADP.docx', 'rb'))
    elif (message.text == 'Дискретная математика(Зачет)'):
        bot.send_message(message.chat.id, text="Суббота - 17.12.2022")
    elif (message.text == 'Огневая подготовка(Диф. зачет)'):
        bot.send_message(message.chat.id, text="Среда - 30.11.2022")
    elif (message.text == 'ОПД(Зачет)'):
        bot.send_message(message.chat.id, text="Понедельник - 28.11.2022")
    elif (message.text == 'СПФП(Диф. зачет)'):
        bot.send_message(message.chat.id, text="Среда - 7.12.2022")
    elif (message.text == 'Физика(Зачет)'):
        bot.send_message(message.chat.id, text="Среда - 14.12.2022")
    elif (message.text == 'Языки программирования(Экзамен)'):
        bot.send_message(message.chat.id, text="Среда - 28.12.2022")
        bot.send_document(message.chat.id, document=open('YAP.pdf', 'rb'))
    elif (message.text == 'Первая помощь(Зачет)'):
        bot.send_message(message.chat.id, text="Суббота - 12.11.2022")
        bot.send_document(message.chat.id, document=open('PRV.pdf', 'rb'))
    elif (message.text == 'Мат. анализ(Зачет)'):
        bot.send_message(message.chat.id, text="Суббота - 03.12.2022")
    elif (message.text == 'Иностранный язык(Зачет)'):
        bot.send_message(message.chat.id, text="Вторник - 13.12.2022")
        bot.send_document(message.chat.id, document=open('NEM.pdf', 'rb'))
    elif (message.text == 'Полный список расписания зимней сессии'):
        bot.send_message(message.chat.id,
                         text="Полный список расписания зимней сессии: \n 1.	Уголовный процесс - Среда - 21.12.2022 \n 2.	СВТ - Суббота - 24.12.2022  \n 3.	АДП - Среда - 23.11.2022\n 4.	Дискретная математика - Суббота - 17.12.2022\n 5. Огневая подготовка - Суббота - 17.12.2022\n 6. ОПД - Понедельник - 28.11.2022\n 7.СПФП -Среда - 7.12.2022\n 8. Физика - Среда - 14.12.2022\n 9. Языки программирования - Среда - 28.12.2022\n 10. Первая помощь - Суббота - 12.11.2022\n 11. Мат. Анализ - Суббота - 03.12.2022\n 12. Иностранный язык - Вторник - 13.12.2022")
    else:
        bot.send_message(message.chat.id, text="Упс, вернитесь обратно, наюбрав команду /start")


bot.polling(none_stop=True)