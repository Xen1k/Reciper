from flask import Flask, request
from telebot import telebot, types
from telebot.apihelper import ApiTelegramException
import time

BOT_TOKEN = ''
URL = 'https://1af3-95-24-223-21.ngrok-free.app'

INGREDIENTS_LIST_REQ_CAPTION = 'Введите список используемых продуктов'

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
app = Flask(__name__,  static_url_path='', static_folder='static')

# Установка вебхука
bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url=URL + '/' + BOT_TOKEN)

def perform_ai_requests(message):
    user_caption = message.text
    # запрос на получение рецепта
    # убрать надписи-обращения (ex: "Конечно! Вот мой предложенный рецепт...") запросом к gpt
    # обработка запроса для генерации изобрадения
    # запрос к api генерации изображения
    bot.send_message(message.chat.id, "Результат генерации...", reply_markup=None)
    bot.send_message(message.chat.id, INGREDIENTS_LIST_REQ_CAPTION)
    bot.register_next_step_handler(message, get_ingredients_from_user_message)

def get_ingredients_from_user_message(message):
    perform_ai_requests(message)

@bot.message_handler(content_types=['text'])
def handle_first_message(message):
    if(message.text == "/start"):
        bot.send_message(message.chat.id, INGREDIENTS_LIST_REQ_CAPTION)
        bot.register_next_step_handler(message, get_ingredients_from_user_message)
    else:
        bot.send_message(message.from_user.id, 'Введите /start', reply_markup=None)

# bot.polling()

@app.route('/{}'.format(BOT_TOKEN), methods=['POST'])
def get_message():
    try:
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    except ApiTelegramException as e:
        print(e)
    return "Connected", 200

if __name__ == '__main__':
    app.run(debug=True, port=80)
