import game_framework
import time
import math
import random
from pico2d import *
from bullet import Bullet

import game_world

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# Event
JUMP, SHOOT, SLIDE_DOWN, SLIDE_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): JUMP,
    (SDL_KEYDOWN, SDLK_j): SHOOT,
    (SDL_KEYDOWN, SDLK_s): SLIDE_DOWN,
    (SDL_KEYUP, SDLK_s): SLIDE_UP,
}

# States


class RunState:

    @staticmethod
    def enter(megaman: object, event: object) -> object:
        if event == JUMP:
            pass
        elif event == SLIDE_DOWN:
            pass
        elif event == SLIDE_UP:
            pass

        megaman.dir = clamp(-1, megaman.velocity, 1)

    @staticmethod
    def exit(megaman, event):
        if event == SHOOT:
            megaman.shoot_bullet()

    @staticmethod
    def do(megaman):
        megaman.frame = (megaman.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        megaman.x += megaman.velocity * game_framework.frame_time
        megaman.x = clamp(25, megaman.x, 800 - 25)

    @staticmethod
    def draw(megaman):
        megaman.image.clip_draw(int(megaman.frame) * 35, 35, 35, 35, megaman.x, megaman.y)



next_state_table = {
    # RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState}
}


class MegaMan:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('run_animation.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def shoot_bullet(self):
        bullet = Bullet(self.x, self.y, self.dir*3)
        game_world.add_object(bullet, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

