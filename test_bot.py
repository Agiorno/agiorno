from flask import Flask, request
import telebot
from telebot import types
from monkey import TOKEN, URL
import time
import requests

bot = telebot.TeleBot('TOKEN', threaded=False)


# app = Flask(__name__)

# @app.route('/HOOK, methods=["POST"])
# def webhook():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     print("Message")
#     return "ok", 200
# #Set_webhook 
# @app.route('/set_webhook', methods=['GET', 'POST']) 
# def set_webhook(): 
#     s = bot.set_webhook(url='https://%s:443/HOOK' % URL, certificate=open('/etc/ssl/istel/server.crt', 'rb')) 
#     if s:
#         print(s)
#         return "webhook setup ok" 
#     else: 
#         return "webhook setup failed" 

# @app.route('/') 
# def index(): 
#     return '%s' % str(a)

# @bot.message_handler(commands=['start', 'help'])
# def startCommand(message):
#     bot.send_message(message.chat.id, 'Hi *' + message.chat.first_name + '*!' , parse_mode='Markdown')
file_id = 'AgACAgIAAxkBAAIBMV8obxRkwrv4rvUjYXFM-mgnwQY2AAKerzEbfkVJSVtW4F2YpE8PYXQblS4AAwEAAwIAA20AA3trAgABGgQ'
# downloaded_file = bot.download_file(file_id.file_path)

arr = requests.get('https://api.telegram.org/bot<bot_token>/getFile?file_id=AgACAgIAAxkBAAIBMV8obxRkwrv4rvUjYXFM-mgnwQY2AAKerzEbfkVJSVtW4F2YpE8PYXQblS4AAwEAAwIAA20AA3trAgABGgQ') 

# with open('new_file.jpeg', 'wb') as new_file:
#     new_file.write(dowloaded_file) 
print(arr)