from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup as BS


def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'/hi - приветствует вас\n'
                              f'/help\n'
                              f'/get - принимает аргумент - название города на русском, и возвращает текукщую погоду\n')


async def get_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    city = msg.split()[1]  # вычленяет из команды название города
    r = requests.get('https://sinoptik.ua/погода-' + city)
    html = BS(r.content, 'html.parser')

    s = ''
    for day in range(3):
        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[day].text
            t_max = el.select('.temperature .max')[day].text

            s += ("Сегодня: ", "Завтра: ", "Послезавтра: ")[day]
            s += str('\t' + t_min + ', ' + t_max + '\n')

    print(s)
    await update.message.reply_text(s)
