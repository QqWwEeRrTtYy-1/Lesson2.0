# https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie
# https://younglinux.info/pygame/draw
# https://pygame.readthedocs.io/en/latest/2_draw/draw.html

import pygame

#Параметры(глобальная константа)
WIDTH = 550
HEIGHT = 450
FPS = 30

#Параметры фигур
WIDTH_RECT = 100
HEIGHT_RECT = 100
WIDTH_DOOR = WIDTH_RECT / 4
HEIGHT_DOOR = WIDTH_RECT / 2
WIDTH_FOUND = WIDTH_RECT + WIDTH_RECT / 4
HEIGHT_FOUND = HEIGHT_RECT / 5
ROOF_POINTS = [[WIDTH / 3 - WIDTH_RECT / 1.5, HEIGHT / 2 - HEIGHT_RECT / 2], [WIDTH / 3 + WIDTH_RECT / 1.5, HEIGHT / 2 - HEIGHT_RECT / 2], [WIDTH / 3, HEIGHT / 4]]
ROCK_POINTS = [[WIDTH / 1.4 + 85, HEIGHT / 2 + 50], [WIDTH / 1.4 + 100, HEIGHT / 2 + 100], [WIDTH / 1.4 + 70, HEIGHT / 2 + 100]]
ROCK_POINTS_1 = [[WIDTH / 1.4 + 55, HEIGHT / 2 + 20], [WIDTH / 1.4 + 80, HEIGHT / 2 + 80], [WIDTH / 1.4 + 50, HEIGHT / 2 + 90]]
ROCK_POINTS_2 = [[WIDTH / 20 , HEIGHT / 1.2 + 50], [WIDTH / 15, HEIGHT / 1.2], [WIDTH / 10 , HEIGHT / 1.2 + 50]]
ROCK_POINTS_3 = [[WIDTH / 8 , HEIGHT / 1.01 ], [WIDTH / 6, HEIGHT / 1.2], [WIDTH / 5 , HEIGHT / 1.01]]


#Задаем цвета(глобальная константа)
WHITE = (255, 255, 255)
YELLOW = (255, 186, 0)
BLACK = (0, 0, 0)
BLUE = (31,110,166)
RED = (255, 0, 0)
BETON = (104, 108, 94)
WOOD = (101, 67, 33)
SAND = (198, 166, 100)
ROOF_COLOR = (166, 47, 32)
WATER = (0, 149, 182)
ROCK_COLOR = (161, 35, 18)

#Создаем игру и окно
pygame.init() #Инициализация игры
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Создание экрана
pygame.display.set_caption(("Первая игра"))
clock = pygame.time.Clock()

#Цикл игры
run = True
while run:
    #Держим цикл на правильно скорости
    clock.tick(FPS)
    #Ввод процесса(событие)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            run = False

    #Обновление
    

    #Рендеринг
    screen.fill(SAND)
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, HEIGHT_RECT * 2.5))
    pygame.draw.circle(screen, YELLOW, (380, 100), 50)
    pygame.draw.circle(screen, BLUE, (360, 80), 50)
    pygame.draw.ellipse(screen, WATER, (WIDTH / 1.8, HEIGHT / 1.4, WIDTH_RECT * 2, HEIGHT_RECT / 1.5))
    pygame.draw.rect(screen, WOOD, (WIDTH / 3 - WIDTH_RECT / 2, HEIGHT / 2 - HEIGHT_RECT / 2, WIDTH_RECT, HEIGHT_RECT)) #Параметры: 1)где рисовать 2) какого цвета 3)в каких координатах(x левый верхний, y левый верхний, ширина прямоугольника, высота прямоугольника)
    pygame.draw.rect(screen, BETON, (WIDTH / 3 - WIDTH_RECT / 1.62, HEIGHT / 2 + HEIGHT_RECT / 2 ,WIDTH_FOUND, HEIGHT_FOUND))
    pygame.draw.rect(screen, WHITE, (WIDTH / 3 - WIDTH_DOOR / 2, HEIGHT / 2 + HEIGHT_RECT  / 2 - HEIGHT_DOOR, WIDTH_DOOR, HEIGHT_DOOR))
    pygame.draw.polygon(screen, ROOF_COLOR, ROOF_POINTS, width=0)
    pygame.draw.polygon(screen, ROCK_COLOR, ROCK_POINTS, width=0)
    pygame.draw.polygon(screen, ROCK_COLOR, ROCK_POINTS_1, width=0)
    pygame.draw.polygon(screen, ROCK_COLOR, ROCK_POINTS_2, width=0)
    pygame.draw.polygon(screen, ROCK_COLOR, ROCK_POINTS_3, width=0)
    pygame.display.flip()

pygame.quit()
