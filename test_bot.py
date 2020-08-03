from flask import Flask, request
import telebot
from telebot import types
from monkey import TOKEN, URL
import time

bot = telebot.TeleBot('TOKEN', threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url='https://%s:443/HOOK' % URL, certificate=open('/etc/ssl/istel/server.crt', 'rb'))

app = Flask(__name__)

@app.route('/HOOK, methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


@bot.message_handler(commands=['start', 'help'])
def startCommand(message):
    bot.send_message(message.chat.id, 'Hi *' + message.chat.first_name + '*!' , parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())