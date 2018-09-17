from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_to_coordinate_01():
    frame = 0
    count = 0
    x = 203
    y = 535
    move_shortest_x = (132 - 203) / 100
    move_shortest_y = (243 - 535) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += move_shortest_x
        y += move_shortest_y
        frame = (frame + 1) % 8
        delay(0.05)


def move_to_coordinate_02():
    frame = 0
    count = 0
    x = 132
    y = 243
    move_shortest_x = (535 - 132) / 100
    move_shortest_y = (470 - 243) / 100
    while count <= 100:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += move_shortest_x
        y += move_shortest_y
        frame = (frame + 1) % 8
        delay(0.05)


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
    # move_to_coordinate_01()
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