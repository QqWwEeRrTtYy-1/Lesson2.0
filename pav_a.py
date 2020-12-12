# https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie
# https://younglinux.info/pygame/draw
# https://pygame.readthedocs.io/en/latest/2_draw/draw.html

# Pygame шаблон - скелет для нового проекта Pygame
import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    
    # Рендеринг
    screen.fill(RED)
    pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()