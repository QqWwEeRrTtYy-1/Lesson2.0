from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

surface_1 = Entity(
    position = (-8, 3),
    model = "cube",
    color=color.dark_gray  ,
    collider = 'box',
    scale = (1, 11, 1),
    collision = True,
)

def draw_world(x = 0, y = 0, columns = 0):


draw_world()

surface = Entity(
    position = (0, -2),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (15, 1),
    collision = True,
)
surface = Entity(
    position = (20, 0),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (15, 1),
    collision = True,
)
surface = Entity(
    position = (32, 4),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (2, 1),
    collision = True,
)
surface = Entity(
    position = (40, 3),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (7, 1),
    collision = True,
)
surface = Entity(
    position = (48, 2),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (1, 1),
    collision = True,
)
surface = Entity(
    position = (56, 3),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (2, 1)
)
surface = Entity(
    position = (60, 3),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (1, 1)
)
surface = Entity(
    position = (69, 1),
    model = "cube",
    color=color.dark_gray,
    collider = "box",
    scale = (10, 1)
)