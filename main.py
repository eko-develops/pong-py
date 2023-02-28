import sys

import pygame

from classes.pong import Pong


def main():
    pong = Pong()
    screen = pong.screen
    ball = pong.ball

    while True:
        screen.fill((10, 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

        ball.draw(screen)
        ball.update()

        pong.update()
        pong.tick()


main()
