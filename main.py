import pygame
from pygame.constants import QUIT
import time
from random import randint

BLACK = 0, 0, 0


def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


pygame.init()
screen = width, heigth = 800, 600

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))

ball.fill(rand_color())
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working:
    time.sleep(0.001)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
    main_surface.fill(BLACK)
    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.bottom >= heigth or ball_rect.top <= 0:
        ball_speed[1] = - ball_speed[1]
        ball.fill(rand_color())
    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_speed[0] = - ball_speed[0]
        ball.fill(rand_color())
    main_surface.blit(ball, ball_rect)
    pygame.display.flip()
