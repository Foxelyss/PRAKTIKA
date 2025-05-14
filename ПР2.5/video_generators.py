import math

from PIL import Image

from image_utils import prepare_gif


def rotate_image(image: Image):
    image.thumbnail((300, 300))

    animation_frames = []

    for x in range(45):
        animation_frames.append(image.rotate(x * 8))

    return prepare_gif(animation_frames)


def cool_glasses(image: Image):
    image = image.resize((300, 300)).convert("RGBA")
    cool_glasses = Image.open("images/cool_glasses.png").resize((300, 300), resample=Image.Resampling.BILINEAR)
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
    jail_image = Image.open("images/jail.png").resize((300, 300)).convert('RGBA')

    animation_frames = []

    for x in range(45):
        a: Image = image.copy()
        y = -math.cos(x / 14) * 300
        y_coordinate = min(300, int(y))
        a.alpha_composite(jail_image, (0, -300 + y_coordinate))
        animation_frames.append(a)

    return prepare_gif(animation_frames)
