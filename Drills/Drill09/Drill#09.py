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
        self.x, self.y = random.randint(100, 700), 600
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y >= 60:
            self.y -= random.randint(1, 10)

    def draw(self):
        self.image.draw(self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 600
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y >= 60:
            self.y -= random.randint(1, 10)

    def draw(self):
        self.image.draw(self.x, self.y)


open_canvas()

num = 20
BigBall = [BigBall() for i in range(random.randint(5, 15))]
num = num - len(BigBall)
SmallBall = [SmallBall() for j in range(num)]

team = [Boy() for k in range(11)]
grass = Grass()

while True:
    for boy in team:
        boy.update()
    for ball in SmallBall:
        ball.update()
    for ball in BigBall:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in SmallBall:
        ball.draw()
    for ball in BigBall:
        ball.draw()
    update_canvas()

    delay(0.05)

close_canvas()
