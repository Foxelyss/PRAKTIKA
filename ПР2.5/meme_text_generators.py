import textwrap

from PIL import ImageFont, ImageDraw, Image

import image_utils


def suslik_meme(message_parts):
    image = Image.open("images/suslik.jpg")

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Arial.TTF", 38)

    question = wrap_words(message_parts[1])
    answer = wrap_words(message_parts[2])
    response = wrap_words(message_parts[3])

    draw.text((300, 0), question + "\n" + answer, (0, 0, 0), font=font,
              stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
    draw.text((300, 350), response, (0, 0, 0), font=font,
              stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")

    return image_utils.prepare_png(image)


def for_the_better_right_meme(message_parts):
    image = Image.open("images/for_the_better_right.jpg")

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("Arial.TTF", 38)

    question = wrap_words(message_parts[1])
    answer = wrap_words(message_parts[2])
    response = wrap_words(message_parts[3])

    draw.text((285, 0), question, (0, 0, 0), font=font,
              stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
    draw.text((855, 0), answer, (0, 0, 0), font=font,
              stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
    draw.text((855, 570), response, (0, 0, 0), font=font,
              stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")

    return image_utils.prepare_png(image)

def wrap_words(x):
    return "\n".join(textwrap.wrap(x, width=28))