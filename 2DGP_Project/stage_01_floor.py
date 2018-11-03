from pico2d import *


class Stage01Floor:
    def __init__(self):
        self.image = load_image('stage_01_floor.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(300, 35)