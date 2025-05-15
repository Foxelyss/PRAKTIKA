import textwrap
from abc import ABC, abstractmethod

from PIL import ImageFont, ImageDraw, Image

import image_utils


class TextMemeGenerator(ABC):
    def __init__(self, message_parts):
        self.message_parts = message_parts

    @abstractmethod
    def check_strings_length(self):
        pass

    @abstractmethod
    def generate(self):
        pass

    @staticmethod
    @abstractmethod
    def get_phrases_quantity():
        return -1


class SuslikMeme(TextMemeGenerator):
    def check_strings_length(self):
        return len(self.message_parts[0]) + len(self.message_parts[1]) > 28 * 4 or len(self.message_parts[2]) > 28 * 4

    def generate(self):
        image = Image.open("images/suslik.jpg")

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Arial.TTF", 38)

        question = wrap_words(self.message_parts[0])
        answer = wrap_words(self.message_parts[1])
        response = wrap_words(self.message_parts[2])

        draw.text((300, 0), question + "\n" + answer, (0, 0, 0), font=font,
                  stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
        draw.text((300, 350), response, (0, 0, 0), font=font,
                  stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")

        return image_utils.prepare_png(image)

    @staticmethod
    def get_phrases_quantity():
        return 3

class ForTheBetterMeme(TextMemeGenerator):
    def check_strings_length(self):
        return len(self.message_parts[0]) > 28 * 5 or len(self.message_parts[1]) > 28 * 5 or len(self.message_parts[2]) > 28 * 5

    def generate(self):
        image = Image.open("images/for_the_better_right.jpg")

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Arial.TTF", 38)

        question = wrap_words(self.message_parts[0])
        answer = wrap_words(self.message_parts[1])
        response = wrap_words(self.message_parts[2])

        draw.text((285, 0), question, (0, 0, 0), font=font,
                  stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
        draw.text((855, 0), answer, (0, 0, 0), font=font,
                  stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")
        draw.text((855, 570), response, (0, 0, 0), font=font,
                  stroke_fill=(255, 255, 255), stroke_width=4, align='center', anchor="ma")

        return image_utils.prepare_png(image)

    @staticmethod
    def get_phrases_quantity():
        return 3


def wrap_words(x, width=28):
    return "\n".join(textwrap.wrap(x, width=width))
