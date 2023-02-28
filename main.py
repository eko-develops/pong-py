import sys

import pygame

from classes.ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAMERATE = 30


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball(100, 100, 20)

    while True:
        screen.fill((10, 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

        ball.draw(screen)
        ball.update()

        pygame.display.update()
        clock.tick(FRAMERATE)


main()
