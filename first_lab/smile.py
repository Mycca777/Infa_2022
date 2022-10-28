import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

pygame.draw.circle(screen, YELLOW, (200, 175), 100)
pygame.draw.circle(screen, RED, (150, 175), 20)
pygame.draw.circle(screen, RED, (250, 175), 20)
pygame.draw.circle(screen, BLACK, (150, 175), 5)
pygame.draw.circle(screen, BLACK, (250, 175), 5)
pygame.draw.line(screen, BLACK, (140, 150),(170, 160), 5)
pygame.draw.line(screen, BLACK, (400 - 140, 150),(400 - 170, 160), 5)
pygame.draw.line(screen, BLACK, (150, 225),(250, 225), 10)



pygame.display.update()
FINISHED = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
