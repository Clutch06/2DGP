from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(1, 10)
        if self.y == 90:
            self.y -= 0

    def draw(self):
        self.image.draw(self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 0
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= random.randint(1, 10)
        if self.y == 90:
            self.y -= 0

    def draw(self):
        self.image.draw(self.x, self.y)


open_canvas()

while True:
    pass

close_canvas()
