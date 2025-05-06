
class ImageOperation:
    def __init__(self, name, is_gif, processing_func):
        self.name = name
        self.is_gif = is_gif
        self.processing_func = processing_func