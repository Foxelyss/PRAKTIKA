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
