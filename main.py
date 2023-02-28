import sys

import pygame

from classes.pong import Pong
from classes.player import Player, Computer


def main():
    pong = Pong()
    player = Player(pong.screen_rect.width // 2, pong.screen_rect.height - 100)
    computer = Computer(pong.screen_rect.width // 2, 0 + 100)

    while True:
        pong.screen.fill((10, 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

        player.paddle.update(pong)
        pong.ball.update()

        player.paddle.draw(pong.screen)
        computer.paddle.draw(pong.screen)
        pong.ball.draw(pong.screen)

        pong.update()
        pong.tick()


main()
