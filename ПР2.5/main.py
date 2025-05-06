import io
import json
import random
import textwrap
import os

import telebot
from PIL import Image, ImageFont, ImageDraw

import image_manipulation
from image_operation import ImageOperation

image_commands = [
    ImageOperation("magic_hat", False, image_manipulation.add_magic_hat),
    ImageOperation("jail", True, image_manipulation.jail),
    ImageOperation("MEGA_ROTATION", True, image_manipulation.rotate_image),
    ImageOperation("ha_ha", True, image_manipulation.make_ha_ha_animation),
    ImageOperation("bonk", False, image_manipulation.add_fancy_nose)
]
image_commands_names = list(map(lambda x: x.name, image_commands))

users_tasks = dict()

API = os.getenv("TELEGRAM_API_KEY")
bot = telebot.TeleBot(API)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)


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


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     r"*Приветики\!* Приветствую вас в [моём](https://t.me/foxehub) ТГ БОТЕ для _создания_ мемов",
                     reply_markup=keyboard, parse_mode="MarkdownV2")


@bot.message_handler(commands=image_commands_names)
def send_task(message: telebot.types.Message):
    bot.send_message(message.chat.id, r"_Ожидаю фотографию\.\.\._", parse_mode="MarkdownV2")
    users_tasks[message.from_user.id] = message.text.split(maxsplit=1)[0]


@bot.message_handler(content_types=['photo'])
def modify_photo(message: telebot.types.Message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    downloaded_image = io.BytesIO(downloaded_file)
    downloaded_image.name = "user_image.jpg"

    user_task = users_tasks.pop(message.from_user.id, "")

    if user_task == "":
        if message.caption is None:
            bot.send_message(message.chat.id, "Команда не может быть пустой!")
            return

        words = message.caption.split()

        if not words[0].startswith("/"):
            bot.send_message(message.chat.id, "Команда не найдена!")
            return

        user_task = words[0]

    image = Image.open(downloaded_image)

    for x in image_commands:
        if user_task == "/" + x.name:
            super_file = x.processing_func(image)

            if x.is_gif:
                bot.send_video(message.chat.id, super_file)
            else:
                bot.send_photo(message.chat.id, super_file)

            return

    bot.send_message(message.chat.id, "Команда не найдена!")


@bot.message_handler(commands=["cancel"])
def send_task(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Галя отмена!")
    users_tasks.pop(message.from_user.id, "")


@bot.message_handler(commands=['code'])
def send_code_from_user(message: telebot.types.Message):
    code = message.text.replace("/code ", "", 1).replace("\\", "\\\\").replace("`", r"\`")
    if len(code.split()) < 2:
        bot.reply_to(message, "Нужно указать не только язык программирования!")

    message_body = "```"
    message_body += code
    message_body += "\n```"

    bot.send_message(message.chat.id, message_body, parse_mode="MarkdownV2")


@bot.message_handler(commands=['motivate'])
def send_motivational_quote(message: telebot.types.Message):
    with open("motivational_quotes.json", "r") as a:
        quotes = json.load(a)
        bot.send_message(message.chat.id, random.choice(quotes))


@bot.message_handler(commands=['suslik'])
def make_suslik_meme(message: telebot.types.Message):
    message_parts = message.text.split("\n")

    if len(message_parts) != 4:
        bot.reply_to(message, "Нужно 3 строки с текстом")
    image = Image.open("suslik.jpg")

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("pt-astra-sans_bold.ttf", 46)

    draw.multiline_text((300, 0), message_parts[1] + "\n" + message_parts[2], (0, 0, 0), font=font,
                        stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
    draw.text((300, 350), "\n".join(textwrap.wrap(message_parts[3], width=27)), (0, 0, 0), font=font,
              stroke_fill=(255, 255, 255), stroke_width=4, anchor="mt")

    image_buffer = image_manipulation.prepare_png(image)

    bot.send_photo(message.chat.id, image_buffer)


bot.infinity_polling()
