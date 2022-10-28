'''Эта игра про шарики.
Шары рандомно двигаются по полю
Выигрыш: смог кликнуть на шар'''
from random import randint
import pygame


pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новый шарик '''
    circle_x = randint(100, 1100)
    circle_y = randint(100, 900)
    circle_r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (circle_x, circle_y), circle_r)


pygame.display.update()
clock = pygame.time.Clock()
FINISHED = False

while not FINISHED:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
