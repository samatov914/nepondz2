from django.shortcuts import render
from telebot import TeleBot, types

from .models import TelegramUser

# Create your views here.
TELEGRAM_BOT_TOKEN = '6491966579:AAH6NK7owPxYDeMPxoZzKyc2ujtT95yahKw'
bot = TeleBot(TELEGRAM_BOT_TOKEN, threaded=True)
admin_id = 5703794977

@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_telegram=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    # bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()


def get_message(message:types.Message):
    mail.description = message.text 
    users = TelegramUser.objects.all()
    for user in users:
        bot.send_message(user.id_telegram, mail.description)
    bot.send_message(message.chat.id, "Рассылка окончена")

@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    if message.chat.id != admin_id:
        bot.send_message(message.chat.id, "Эта команда доступна только админу")
        return
    msg = bot.send_message(message.chat.id, "Введите текст для рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_text(message):
    bot.send_message(admin_id, message)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Я вас не понял")

