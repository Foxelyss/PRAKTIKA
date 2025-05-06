import io
import math
import random

from PIL import Image


def prepare_gif(animation_frames: [Image]):
    image_buffer = io.BytesIO()
    image_buffer.name = "result.gif"
    animation_frames[0].save(image_buffer, append_images=animation_frames[1:], duration=32, loop=0, quality=65,
                             optimize=True, interlace=True)

    image_buffer.seek(0)
    return image_buffer


def prepare_png(image: Image):
    image_buffer = io.BytesIO()
    image_buffer.name = "result.png"
    image.save(image_buffer, quality=45, optimize=True, interlace=True)

    image_buffer.seek(0)
    return image_buffer


def rotate_image(image: Image):
    image.thumbnail((300, 300))

    animation_frames = []

    for x in range(45):
        animation_frames.append(image.rotate(x * 8))

    return prepare_gif(animation_frames)


def add_fancy_nose(image: Image):
    image = image.convert("RGBA")
    fancy_nose = Image.open("clown_nose.png").convert("RGBA")

    x, y = image.size
    fancy_nose = fancy_nose.resize((int(x // 2), int(y // 2)))

    image.alpha_composite(fancy_nose, (int(x // 4), int(y // 4)))

    return prepare_png(image)


def make_ha_ha_animation(image: Image):
    image = image.resize((300, 300)).convert("RGBA")
    cool_glasses = Image.open("cool_glasses.png").resize((300, 300), resample=Image.Resampling.BILINEAR)
    cool_glasses = cool_glasses.transpose(Image.Transpose.ROTATE_180)
    animation_frames = []

    for x in range(45):
        a: Image = image.copy()
        y = -math.cos(x / 14) * 150
        y_coordinate = min(300, int(y))
        a.alpha_composite(cool_glasses.convert('RGBA'), (0, -150 + y_coordinate))
        cool_glasses = cool_glasses.rotate(4, resample=Image.Resampling.BICUBIC)
        animation_frames.append(a)

    return prepare_gif(animation_frames)


def jail(image: Image):
    image = image.resize((300, 300)).convert("RGBA")
    jail_image = Image.open("jail.png").resize((300, 300)).convert('RGBA')

    animation_frames = []

    for x in range(45):
        a: Image = image.copy()
        y = -math.cos(x / 14) * 300
        y_coordinate = min(300, int(y))
        a.alpha_composite(jail_image, (0, -300 + y_coordinate))
        animation_frames.append(a)

    return prepare_gif(animation_frames)


def add_magic_hat(image: Image):
    image = image.convert("RGBA")
    magic_hat = Image.open("magic_hat.png").convert("RGBA")

    x, y = image.size
    random_index = random.randrange(0, 4)
    magic_hat = magic_hat.crop((0 + random_index * 400, 0, 400 + random_index * 400, 305))
    magic_hat = magic_hat.resize((int(x // 2), int(y // 2)))

    image.alpha_composite(magic_hat, (int(x // 4), int(y // 30)))

    return prepare_png(image)
