from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

window.title = "Platformer"
window.color = color.gold
window.fullscreen = True

player = PlatformerController2d(
    model = "cube",
    position = (0, 4), 
    collider = "box",
    collision = True,
    color = color.red,
)

camera.add_script(SmoothFollow(target=player, offset=[0.5, -30], speed=40))

def update():
    player.x += held_keys["d"] * time.dt * 2
    player.x -= held_keys["a"] * time.dt * 2

def input(key):
    if key == "enter":
        player.position = (0, 2)


def draw_world(x = 0, y = -8, columns = 50):
    tile_shift_x = x
    for i in range(columns):
        tile_shift_y = y
        amount = random.randint(4, 6)
        for i in range(amount):
            tile = Entity(
            position = (tile_shift_x, tile_shift_y),
            model = "cube",
            collider = "box",
            scale=(1,1),
            texture="images/ground"
            )
            tile_shift_y += 1
        for i in range(2):
            tile = Entity(
                position = (tile_shift_x, tile_shift_y),
                model = "cube",
                collider = "box",
                scale=(1,1),
                texture="images/rock"
            )
            tile_shift_y += 1
        for i in range(2):
            tile = Entity(
                position = (tile_shift_x, tile_shift_y),
                model = "cube",
                collider = "box",
                scale=(1,1),
                texture="grass"
            )
            tile_shift_y += 1
        tile_shift_x += 1
draw_world()


app.run()