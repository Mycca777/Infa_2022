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
    return circle_x, circle_y, circle_r


def click_event(circle_x, circle_y, circle_r, mouse_x, mouse_y):
    '''Эта функция анализирует, попал ли игрок по шарику'''
    if (mouse_x - circle_x)**2 + (mouse_y - circle_y)**2 <= circle_r**2:
        return True
    return False


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
            if click_event(circle_x, circle_y, circle_r, mouse_x, mouse_y):
                score += 1
            print('Click!')
    circle_x, circle_y, circle_r = new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
