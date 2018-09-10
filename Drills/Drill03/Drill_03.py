from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (True):
    x = 20;
    y = 90;
    
    while (x < 800-20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while (y < 600-40):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while (x > 0+20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while (y > 0+90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)   
    
close_canvas()
