from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

window.title = "Platformer"
window.color = rgb(100, 170, 208)
window.fullscreen = True

color_grass = rgb(43, 130, 0)
color_finish_1 = color.black
color_finish_2 = color.white
color_platforms_1 = rgb(181, 22, 22)
color_platforms_2 = rgb(91, 22, 181)

last_x = 0
pre_finish = 7
deaths = 0

player = PlatformerController2d(
    scale = (1, 1),
    position = (0, 5), 
    collision = True,
    color = rgb(255, 139, 0),
    )

control_help = Entity(
    position = (-8, 2),
    model = "quad",
    scale = (8,6),
    texture = "images/control"
    )

control_help = Entity(
    position = (-7.3, -1),
    model = "quad",
    scale = (6, 2),
    texture = "images/control2"
    )

gimp_easter_egg = Entity(
    position = (-10.5, -5.5),
    model = "quad",
    scale = (2, 2),
    texture = "images/gimp"
    )

test = Text(text = "Deaths: 0", x = -0.82, y = .4, scale = 1, origin = (0,0))

camera.add_script(SmoothFollow(target = player, offset = [0.5, -35], speed = 6))

music_game = Audio("audio/audio_fon", pitch = 1, loop = True, autoplay = True)

on_off_switch = ButtonGroup(("music off", "music on"), min_selection = 1, x = -0.8885, y = .5, default="music on", selected_color = color.red)


def on_value_changed():
    print("turn:", on_off_switch.value)
    if on_off_switch.value == ["music off"]:
        music_game.pause()
    elif on_off_switch.value == ["music on"]:
        music_game.resume()
on_off_switch.on_value_changed = on_value_changed


def input(key):
    if key == "enter":
        global deaths
        deaths += 1
        test.text = "Deaths: " + str(deaths)
        player.position = (0, 2)
    if key == "escape":
        sys.exit()


def world(x = 0, y = 0, columns = 0):
    def builder(amount_map_block,  color_map_up, times):
        global last_x
        if last_x > 0:
            block_map_x = last_x
        else:
            block_map_x = x
        for i in range(times):
            if amount_map_block == pre_finish:
                amount_map_block = pre_finish
            else:
                amount_map_block = random.randint(4, 6)
            block_map_y = y
            for i in range(amount_map_block):
                block = Entity(
                position = (block_map_x, block_map_y),
                model = "quad",
                collider = "box",
                scale = (1,1),
                color = rgb(89, 87, 86),
                )
                block_map_y += 1
            for i in range(2):
                block = Entity(
                    position = (block_map_x, block_map_y),
                    model = "quad",
                    collider = "box",
                    scale = (1,1),
                    color = rgb(89, 32, 3),
                )
                block_map_y += 1

            for i in range(1):
                block = Entity(
                    position = (block_map_x, block_map_y),
                    model = "quad",
                    collider = "box",
                    scale = (1,1),
                    color =  color_map_up,
                )
                block_map_y += 1
            block_map_x += 1
            last_x = block_map_x


    def finish():
        finish_flag = Entity(
        position = (last_x + 3.3 , 2.8),
        model = "quad",
        scale = (8, 4.8),
        texture = "images/finish_flag_img"
        )
        builder(pre_finish, color_finish_1, 1)
        builder(pre_finish, color_finish_2, 1)
        builder(pre_finish, color_finish_1, 1)
        builder(pre_finish, color_finish_2, 1)
        builder(pre_finish, color_finish_1, 1)
        builder(pre_finish, color_finish_2, 1)
        builder(pre_finish, color_finish_1, 1)


    def draw_platform(start_x_platform, start_y_platform, color_platform):
        platforms = columns // 20
        platform_block_x = x + start_x_platform
        platform_block_y = y + start_y_platform
        for i in range(platforms):
            amount_platform_block = random.randint(5, 8)
            for i in range(amount_platform_block):
                if last_x - platform_block_x > 10:
                    block = Entity(
                    position = (platform_block_x, platform_block_y),
                    model = "quad",
                    collider = "box",
                    scale = (1,1),
                    color = color_platform,
                    )
                else:
                    block = Entity(
                    position = (platform_block_x, platform_block_y),
                    model = "quad",
                    collider = "box",
                    collision = False,
                    scale = (1,1),
                    color = color.clear,
                    )
                platform_block_x += 1
            platform_block_x += random.randint(20, 22)


    builder(0, color_grass, columns)
    builder(pre_finish, color_grass, 3)
    finish()
    draw_platform(8, 11, color_platforms_1)
    draw_platform(16, 15, color_platforms_2)
world(0, -9, 90)

app.run()