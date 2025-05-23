import io
import json
import random
import os
import telebot
import asyncio

from telebot.async_telebot import AsyncTeleBot
from PIL import Image
from dotenv import load_dotenv

import image_generators
import video_generators
from image_operation import ImageOperation
import reddit_meme_fetcher
from meme_text_generators import SuslikMeme, ForTheBetterMeme
from sync_in_async.sync_in_async import SyncInAsync
import gc

load_dotenv()

API = os.getenv("TELEGRAM_API_KEY")
bot = AsyncTeleBot(API)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

gc.set_threshold(1024,512,256)

image_commands = [
    ImageOperation("magic_hat", False, image_generators.add_magic_hat),
    ImageOperation("jail", True, video_generators.jail),
    ImageOperation("MEGA_ROTATION", True, video_generators.rotate_image),
    ImageOperation("ha_ha", True, video_generators.cool_glasses),
    ImageOperation("bonk", False, image_generators.add_fancy_nose)
]
image_commands_names = list(map(lambda x: x.name, image_commands))

users_tasks = dict()


def build_keyboard(column_quantity=2):
    button_rows = []
    row = []

    for x in range(len(image_commands_names)):
        button = telebot.types.KeyboardButton(text="/" + image_commands_names[x])
        row.append(button)
        if (x + 1) % column_quantity == 0:
            button_rows.append(row)
            row = []

    if len(row) != 0:
        button_rows.append(row)

    for x in button_rows:
        keyboard.add(*x)

    keyboard.add(telebot.types.KeyboardButton(text="/cancel"))


build_keyboard(3)

with open("motivational_quotes.json", "r") as a:
    quotes = json.load(a)


async def make_operation_async(func):
    async_manager = SyncInAsync()
    return await async_manager.Call(func=func)


@bot.message_handler(commands=['start'])
async def handle_start(message):
    await bot.send_message(message.chat.id,
                           r"*Приветики\!* Приветствую вас в [моём](https://t.me/foxehub) ТГ БОТЕ для _создания_ мемов",
                           reply_markup=keyboard, parse_mode="MarkdownV2")


@bot.message_handler(commands=image_commands_names)
async def send_task(message: telebot.types.Message):
    await bot.send_message(message.chat.id, r"_Ожидаю фотографию\.\.\._", parse_mode="MarkdownV2")
    users_tasks[message.from_user.id] = message.text.split(maxsplit=1)[0]


@bot.message_handler(content_types=['photo'])
async def modify_photo(message: telebot.types.Message):
    file_id = message.photo[-1].file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)

    downloaded_image = io.BytesIO(downloaded_file)
    downloaded_image.name = "user_image.jpg"

    user_task = users_tasks.pop(message.from_user.id, "")

    if user_task == "":
        if message.caption is None:
            await bot.send_message(message.chat.id, "Команда не может быть пустой!")
            return

        words = message.caption.split(maxsplit=1)

        if not words[0].startswith("/"):
            await bot.send_message(message.chat.id, "Команда не найдена!")
            return

        user_task = words[0]

    image = Image.open(downloaded_image)

    try:
        command_name_index = image_commands_names.index(user_task[1:])

        command = image_commands[command_name_index]
        resulting_file = await make_operation_async(func=lambda: command.processing_func(image))

        if command.is_gif:
            await bot.send_video(message.chat.id, resulting_file)
        else:
            await bot.send_photo(message.chat.id, resulting_file)

        del resulting_file
    except ValueError:
        await bot.send_message(message.chat.id, "Команда не найдена!")

    del downloaded_image

@bot.message_handler(commands=["cancel"])
async def send_task(message: telebot.types.Message):
    await bot.send_message(message.chat.id, "Галя отмена!")
    users_tasks.pop(message.from_user.id, "")


@bot.message_handler(commands=['code'])
async def send_code_from_user(message: telebot.types.Message):
    code = message.text.replace("/code ", "", 1).replace("\\", "\\\\").replace("`", r"\`")

    if len(code.split()) < 2:
        await bot.reply_to(message, "Нужно указать не только язык программирования!")
        return

    message_body = "```"
    message_body += code
    message_body += "\n```"

    await bot.send_message(message.chat.id, message_body, parse_mode="MarkdownV2")


@bot.message_handler(commands=['motivate'])
async def send_motivational_quote(message: telebot.types.Message):
    await bot.send_message(message.chat.id, random.choice(quotes))


@bot.message_handler(commands=['suslik'])
async def make_suslik_meme(message: telebot.types.Message):
    message_parts = message.text.split("\n")

    if len(message_parts) != SuslikMeme.get_phrases_quantity() + 1:
        await bot.reply_to(message, "Нужно 3 строки с текстом")
        return

    phrases = message_parts[1:4]

    meme_text_generator = SuslikMeme(phrases)

    if meme_text_generator.check_strings_length():
        await bot.reply_to(message, "Строки чересчур длинные")
        return

    image_buffer = await make_operation_async(func=lambda: meme_text_generator.generate())

    await bot.send_photo(message.chat.id, image_buffer)

    del image_buffer


@bot.message_handler(commands=['for_better'])
async def make_for_the_better_right_meme(message: telebot.types.Message):
    message_parts = message.text.split("\n")

    if len(message_parts) != ForTheBetterMeme.get_phrases_quantity() + 1:
        await bot.reply_to(message, "Нужно 3 строки с текстом")
        return

    phrases = message_parts[1:4]

    meme_text_generator = ForTheBetterMeme(phrases)

    if meme_text_generator.check_strings_length():
        await bot.reply_to(message, "Строки чересчур длинные")
        return

    image_buffer = await make_operation_async(func=lambda: meme_text_generator.generate())

    await bot.send_photo(message.chat.id, image_buffer)

    del image_buffer


@bot.message_handler(commands=['programming_meme'])
async def make_for_the_better_right_meme(message: telebot.types.Message):
    image = reddit_meme_fetcher.get_meme_image()
    image_title = image["title"].replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")

    await bot.send_photo(message.chat.id, image["url"],
                         caption=f"{image_title}\nАвтор: {image["author"]}\n<a href=\"{image["postLink"]}\">Клик на пост!</a>",
                         parse_mode="HTML")


asyncio.run(bot.polling())
