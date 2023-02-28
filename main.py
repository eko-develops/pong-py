import sys

import pygame

from classes.pong import Pong
from classes.player import Player


def main():
    pong = Pong()
    player = Player(pong.screen_rect.width // 2, pong.screen_rect.height - 100)

    screen = pong.screen
    ball = pong.ball

    while True:
        screen.fill((10, 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

        player.paddle.draw(screen)

        ball.draw(screen)
        ball.update()

        pong.update()
        pong.tick()


main()
