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
    frame = 0
    count = 0
    x = 535
    y = 470
    move_shortest_x = (477 - 535) / 100
    move_shortest_y = (203 - 470) / 100
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


def move_to_coordinate_04():
    frame = 0
    count = 0
    x = 477
    y = 203
    move_shortest_x = (715 - 477) / 100
    move_shortest_y = (136 - 203) / 100
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


def move_to_coordinate_05():
    frame = 0
    count = 0
    x = 715
    y = 136
    move_shortest_x = (316 - 715) / 100
    move_shortest_y = (225 - 136) / 100
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


def move_to_coordinate_06():
    frame = 0
    count = 0
    x = 316
    y = 225
    move_shortest_x = (510 - 316) / 100
    move_shortest_y = (92 - 225) / 100
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


def move_to_coordinate_07():
    frame = 0
    count = 0
    x = 510
    y = 92
    move_shortest_x = (692 - 510) / 100
    move_shortest_y = (518 - 92) / 100
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


def move_to_coordinate_08():
    frame = 0
    count = 0
    x = 692
    y = 518
    move_shortest_x = (682 - 692) / 100
    move_shortest_y = (336 - 518) / 100
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


def move_to_coordinate_09():
    frame = 0
    count = 0
    x = 682
    y = 336
    move_shortest_x = (712 - 682) / 100
    move_shortest_y = (349 - 336) / 100
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


def move_to_coordinate_10():
    frame = 0
    count = 0
    x = 712
    y = 349
    move_shortest_x = (203 - 712) / 100
    move_shortest_y = (535 - 349) / 100
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