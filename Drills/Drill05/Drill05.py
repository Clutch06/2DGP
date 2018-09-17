from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_to_coordinate_01():
    x, y = 203, 535
    frame = 0
    while x > 132:
        while y > 243:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 2
            y -= 5
            delay(0.05)
            get_events()


def move_to_coordinate_02():
    pass


def move_to_coordinate_03():
    pass


def move_to_coordinate_04():
    pass


def move_to_coordinate_05():
    pass


def move_to_coordinate_06():
    pass


def move_to_coordinate_07():
    pass


def move_to_coordinate_08():
    pass


def move_to_coordinate_09():
    pass


def move_to_coordinate_10():
    pass


def move():
    move_to_coordinate_01()
    move_to_coordinate_02()
    move_to_coordinate_03()
    move_to_coordinate_04()
    move_to_coordinate_05()
    move_to_coordinate_06()
    move_to_coordinate_07()
    move_to_coordinate_08()
    move_to_coordinate_09()
    move_to_coordinate_10()


while True:
    move()


close_canvas()