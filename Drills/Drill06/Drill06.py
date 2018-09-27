from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mouse_x, mouse_y
    global character_x, character_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            character_x, character_y = event.x - 25, KPU_HEIGHT - 1 - event.y + 26
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_cursor = load_image('hand_arrow.png')
stop_character = load_image('character.png')

running = True
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse_cursor.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)
    stop_character.clip_draw(0, 0, 42, 92, character_x, character_y)
    update_canvas()

    delay(0.02)
    handle_events()

close_canvas()




