from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    pass


class Ball:
    pass


open_canvas()

while True:
    pass

close_canvas()
