from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
import os

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def reply(update, context):
    update.message.reply_text(f'You said: {update.message.text}')

from telegram.ext import CallbackContext
dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

@app.route('/')
def home():
    return "Telegram Bot is running!"
