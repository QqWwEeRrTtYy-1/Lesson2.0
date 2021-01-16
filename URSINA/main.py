import objects
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()


player = PlatformerController2d(
    position = (0, 0), 
    collision = True,
    color = color.red
)


camera.add_script(SmoothFollow(target=player, offset=[0.5, -30], speed=40))

def update():
    player.x += held_keys['d'] * time.dt * 2
    player.x -= held_keys['a'] * time.dt * 2

app.run()
