import logging

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from pytube import YouTube

from aiogram import Bot, Dispatcher, executor, types
from pytube.exceptions import VideoUnavailable

API_TOKEN = '5783967155:AAEkrfbdEUjyxzdxMFgFDhz8g-7htanbqh8'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ бот, который скачивает видео с ютуба\n\n"
                        "Есть 2 вида запросов:\n"
                        "/download video link\n"
                        "/download audio link\n"
                        "вместо link подставь ссылку.\n")


@dp.message_handler(commands=['download'])
async def download(message: types.Message):
    try:
        command, mode, link = message.text.split(' ')
        yt = YouTube(link)
        chosen_stream = yt.streams.filter(progressive=True, type="video").last()
        match mode:
            case "video":
                pass
            case "audio":
                chosen_stream = yt.streams.filter(only_audio=True).last()
        await message.answer("Ищу видео и начинаю скачивать, подожди")
        path = chosen_stream.download()
        await message.answer(f"Скачал и сохранил в {path}")
    except VideoUnavailable:
        await message.answer("Ссылка неверна, пробуй еще раз.\n"
                             "Введи /download video link\n"
                             "или /download audio link\n"
                             "вместо link подставь ссылку.")
    except ValueError:
        await message.answer("Ты не соблюдаешь формат запроса.\n"
                             "2 вида запросов:\n"
                             "/download video link\n"
                             "/download audio link\n"
                             "вместо link подставь ссылку.\n"
                             "например:\n"
                             r"/download audio https://www.youtube.com/watch?v=2lAe")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
