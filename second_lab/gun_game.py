import math
from random import randint, choice

import pygame


FPS = 30


RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME (сделано)
        if self.y + self.r >= 600:
            self.vy = abs(self.vy)/3
            self.vx *= 9/10
        if self.x + self.r >= 800:
            self.vx *= -1
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        """Рисуем шарик"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME (сделано)
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (obj.r + self.r)**2:
            return True
        return False


class Gun:
    def __init__(self, screen):
        """Этот класс отвечает за орудие
        screen : объект, задающий поле
        Args:
        
       x - координата орудия по горизонтали слева направо
       y - координата орудия по вертикали сверху вниз
       vx - добавка ("скорость") орудия по горизонтали
       vy - добавка ("скорость") орудия по вертикали
       targ - насколько сильно заряжено орудие, чтобы отрисовать это на экране
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.targ = 0
        self.color = GREY
        self.vx = 5
        self.vy = 5
        self.x = 20
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.targ = 0


    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        tank_surf = pygame.image.load('tank.jpg')
        tank_surf.set_colorkey((255, 255, 255))
        self.screen.blit(tank_surf, (self.x - 15, self.y - 20))
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + (20+self.targ)*math.cos(self.an), self.y + (20+self.targ)*math.sin(self.an)), 5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.targ += 1
            self.color = RED
        else:
            self.color = GREY

    def move(self, event_type):
        """Движение орудия
        event_type - какая клавиша нажата
        """
        if event_type == 'up':
            self.y -= self.vy
        elif event_type == 'down':
            self.y += self.vy
        elif event_type == 'right':
            self.x += self.vx
        elif event_type == 'left':
            self.x -= self.vx


class Target:
    def new_target(self, screen, type_of_target):
        """ Инициализация новой цели.
        Args:
        x - координата по горизонтали
        y - координата по вертикали
        r - радиус мишени
        vx - скорость мишени по х
        vy- скорость мишени по y
        live - жизнь мишени
        points - очки
        """
        self.points = 0
        self.live = 1
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        if type_of_target == 1:
            '''
            Первый тип мишени - маленький радиус, одна жизнь, маленькая скорость
            '''
            r = self.r = randint(5, 10)
            self.vx = randint(-5, 5)
            self.vy = randint(-5, 5)
        elif type_of_target == 2:
            '''
            Второй тип мишени - большой радиус, 3 жизни, большая скорость
            '''
            self.live = 3
            r = self.r = randint(30, 40)
            self.vx = randint(15, 20)
            self.vy = randint(15, 20)
        color = self.color = RED
        self.screen = screen

    def draw(self):
        """Рисую мишень"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        self.move()
    
    def draw_score(self, points):
        """Рисую очки"""
        pygame.draw.circle(self.screen, WHITE, [50, 25], 25)
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(str(points), False, (0, 0, 0))
        # print(self.points)
        self.screen.blit(text_surface, (50,0))

    def move(self):
        '''
        Движение с отскоком от всех стен
        '''
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx *= -1
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vy *= -1
        self.x += self.vx
        self.y -= self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
type_of_target = randint(1, 2)
target.new_target(screen, type_of_target)
finished = False
points = 0


while not finished:
    screen.fill(WHITE)
    type_of_target = randint(1, 2)
    target.draw_score(points)
    gun.draw()
    target.draw()
    for b in balls:
        if abs(b.vx) >= 0.2:
            b.draw()
        else:
            pygame.draw.circle(screen, WHITE, (b.x, b.y), b.r)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # print(123123123)
                gun.move('up')
                gun.draw()
            elif event.key == pygame.K_DOWN:
                gun.move('down')
                gun.draw()
            elif event.key == pygame.K_RIGHT:
                gun.move('right')
                gun.draw()
            elif event.key == pygame.K_LEFT:
                gun.move('left')
                gun.draw()

    for b in balls:
        if abs(b.vx) >= 0.1:
            b.move()
            b.vy -= 1
            # counter = 0.3
            if b.hittest(target) and target.live:
                target.live = 0
                points += 1
                target.new_target(screen, type_of_target)

    gun.power_up()

pygame.quit()
