import sys

import pygame

from classes.pong import Pong
from classes.player import Player, Computer


def main():
    pong = Pong()
    player = Player(pong.screen_rect.width // 2, pong.screen_rect.height - 100)
    computer = Computer(pong.screen_rect.width // 2, 0 + 100)

    while True:
        pong.draw_bg()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.paddle.update(pong)
        pong.ball.update()

        player.paddle.draw(pong.screen)
        computer.paddle.draw(pong.screen)
        pong.ball.draw(pong.screen)

        pong.update()
        pong.tick()


main()
