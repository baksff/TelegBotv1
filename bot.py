import telebot
import config
import urllib.request


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(message.chat.id, 'Привет! Введите /help для помощи')


@bot.message_handler(commands=['help'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Что это за бот?', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Кто разработчик?', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Как стать скриптером?', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='Тест', callback_data=6))
    bot.send_message(message.chat.id, text="Выберите один из вариантов: ", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == '3':
        answer = 'Этот бот предназначен для тестирования функций.'
    elif call.data == '4':
        answer = 'Разработчик данного бота: vk.com/idnlnety'
    elif call.data == '5':
        answer = 'Хотите стать скриптером данного бота? Пишите разработчику'
    elif call.data == '6':
    	answer = 'Тест'

    bot.send_message(call.message.chat.id, answer)


@bot.message_handler(content_types=["text"])
def text(message):
    print(message.text)


bot.polling()