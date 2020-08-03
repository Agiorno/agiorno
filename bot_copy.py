# file - ~/Bot/bot.py
# venv - ~/Bot/bot

from __future__ import unicode_literals
from flask import Flask, request
import telebot
from monkey import TOKEN, URL

app = Flask(__name__)
app.debug = True


bot = telebot.TeleBot(TOKEN)	

a=[]


#WebHook
@app.route('/HOOK', methods=['POST', 'GET']) 
def webhook_handler():
    if request.method == "POST": 
        update = telebot.types.Update.de_json(request.get_json(force=True))
        bot.process_new_updates([update])
        a.append(str(update.message))
        # try:
        #     chat_id = update.message.chat.id 
        #     text = update.message.text
        #     userid = update.message.from_user.id
            # bot.send_message(chat_id=chat_id, text="hello")
        # except Exception as e:
        #     print(e)
#     return 'ok' 

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

#Set_webhook 
@app.route('/set_webhook', methods=['GET', 'POST']) 
def set_webhook(): 
    s = bot.set_webhook(url='https://%s:443/HOOK' % URL, certificate=open('/etc/ssl/istel/server.crt', 'rb')) 
    if s:
        print(s)
        return "webhook setup ok" 
    else: 
        return "webhook setup failed" 

@app.route('/') 
def index(): 
    return '%s' % str 


