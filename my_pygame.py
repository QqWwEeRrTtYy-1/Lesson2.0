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

#Задаем цвета(глобальная константа)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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
    screen.fill(BLUE)
    pygame.draw.rect(screen, RED, (WIDTH / 2 - WIDTH_RECT / 2, HEIGHT / 2 - HEIGHT_RECT / 2, WIDTH_RECT, HEIGHT_RECT)) #Параметры: 1)где рисовать 2) какого цвета 3)в каких координатах(x левый верхний, y левый верхний, ширина прямоугольника, высота прямоугольника)
    pygame.draw.rect(screen, BLACK, (WIDTH / 2 - WIDTH_RECT / 1.62, HEIGHT / 2 + HEIGHT_RECT / 2 ,WIDTH_FOUND, HEIGHT_FOUND))
    pygame.draw.rect(screen, WHITE, (WIDTH / 2 - WIDTH_DOOR / 2, HEIGHT / 2 + HEIGHT_RECT  / 2 - HEIGHT_DOOR, WIDTH_DOOR, HEIGHT_DOOR))
    pygame.draw.lines(screen, BLACK, True, [[WIDTH / 2 - WIDTH_RECT / 1.5, HEIGHT / 2 - HEIGHT_RECT / 2], [WIDTH / 2 + WIDTH_RECT / 1.5, HEIGHT / 2 - HEIGHT_RECT / 2], [WIDTH / 2, HEIGHT / 4]]) #Параметры: 1)где рисовать 2) какого цвета, 3)замыкать точки или нет(True/False)

    pygame.display.flip()

pygame.quit()