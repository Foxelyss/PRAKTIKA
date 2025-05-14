import random

from PIL import Image

from image_utils import prepare_png


def add_fancy_nose(image: Image):
    image = image.convert("RGBA")
    fancy_nose = Image.open("images/clown_nose.png").convert("RGBA")

    x, y = image.size
    fancy_nose = fancy_nose.resize((int(x) // 2, int(y) // 2))

    image.alpha_composite(fancy_nose, (int(x) // 4, int(y) // 4))

    return prepare_png(image)


def add_magic_hat(image: Image):
    image = image.convert("RGBA")
    magic_hat = Image.open("images/magic_hat.png").convert("RGBA")

    x, y = image.size
    random_index = random.randrange(0, 4)
    magic_hat = magic_hat.crop((0 + random_index * 400, 0, 400 + random_index * 400, 305))
    magic_hat = magic_hat.resize((int(x) // 2, int(y) // 2))

    image.alpha_composite(magic_hat, (int(x) // 4, int(y) // 30))

    return prepare_png(image)
