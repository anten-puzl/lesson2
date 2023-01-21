import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from copy import copy
from random import randint


BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0


pygame.init()

FPS = pygame.time.Clock()

screen = width, heigth = 800, 600

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
speed = 7


def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width-20, randint(0, heigth), *enemy.get_size())
    enemy_speed = randint(2,5)
    return [enemy, enemy_rect, enemy_speed]


def create_bonus():
    bonus = pygame.Surface((20, 20))
    bonus.fill(GREEN)
    bonus_rect = pygame.Rect(randint(0, width), 20, *bonus.get_size())
    bonus_speed = randint(2,5)
    return [bonus, bonus_rect, bonus_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 1600)


enemies = []
bonuses = []

is_working = True

while is_working:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
    main_surface.fill(BLACK)
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_DOWN]:
        if ball_rect.bottom <= heigth:
            ball_rect = ball_rect.move((0, speed))
    elif pressed_key[K_UP]:
        if ball_rect.top >= 0:
            ball_rect = ball_rect.move((0, -speed))
    elif pressed_key[K_LEFT]:
        if ball_rect.left >= 0:
            ball_rect = ball_rect.move((-speed, 0))
    elif pressed_key[K_RIGHT]:
        if ball_rect.right <= width:
            ball_rect = ball_rect.move((speed, 0))

    for enemy in copy(enemies):
        enemy[1] = enemy[1].move(-enemy[2],0)
        main_surface.blit(enemy[0], enemy[1])
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if ball_rect.colliderect(enemy[1]):
            enemies.pop(enemies.index(enemy))

    for bonus in copy(bonuses):
        bonus[1] = bonus[1].move(0,bonus[2])
        main_surface.blit(bonus[0], bonus[1])
        if bonus[1].bottom > heigth:
            bonuses.pop(bonuses.index(bonus))
        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))

    main_surface.blit(ball, ball_rect)

    pygame.display.flip()
