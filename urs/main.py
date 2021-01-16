from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

window.title = 'Platformer'
window.color = color.gold   
window.fullscreen = True

player = PlatformerController2d(
    position = (-8, 0), 
    collider = 'box',
    collision = True,
    color = color.white,
    texture='brick'
)

camera.add_script(SmoothFollow(target=player, offset=[0.5, -30], speed=40))

def update():
    player.x += held_keys['d'] * time.dt * 2
    player.x -= held_keys['a'] * time.dt * 2

def input(key):
    if key == 'enter':
        player.position = (0, -1)
"""
def draw_world(x = 0, y = 0, columns = 0):
    def draw_column(height = 5):
        for i in range(height + 1):
            tile = Entity(
                position(x, y)
                model = "quad",
                collider = 'box',
                scale = (1, 1, 1),
                collision = True,
                )

draw_world()

"""
counter_2 = -10
for i in range(10):
    counter_1 = -11
    for i in range(5):
        tile = Entity(
            model = "quad",
            collider = "box",
            collision = True,
            x = counter_2,
            y = counter_1,
            )
        counter_1 += 1
    counter_2 += 1



app.run()
