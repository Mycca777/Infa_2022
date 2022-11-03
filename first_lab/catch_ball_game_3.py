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
COLORS_FILLED = [BLACK]*6


def new_ball(colors):
    '''рисует новый шарик '''
    circle_x = randint(100, 1100)
    circle_y = randint(100, 900)
    circle_r = randint(10, 100)
    color = colors[randint(0, 5)]
    pygame.draw.circle(screen, color, (circle_x, circle_y), circle_r)
    return circle_x, circle_y, circle_r


def scores(circle_cords, mouse_x, mouse_y):
    '''Эта функция анализирует, попал ли игрок по шарику'''
    for circle_x, circle_y, circle_r in circle_cords:
        if (mouse_x - circle_x)**2 + (mouse_y - circle_y)**2 <= circle_r**2:
            return True
    return False


def create_balls(n):
    '''Эта функция создает n шаров'''
    circle_cords = []
    for _ in range(n):
        circle_cords.append((new_ball(COLORS)))
    return circle_cords


pygame.display.update()
clock = pygame.time.Clock()
FINISHED = False
score = 0

while not FINISHED:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if scores(circle_cords, mouse_x, mouse_y):
                score += 1
                print(score)
            print('Click!')
    circle_cords = create_balls(12)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
