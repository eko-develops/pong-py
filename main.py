import sys

import pygame

from classes.pong import Pong
from classes.player import Player, Computer

pygame.init()


def main():
    pong = Pong()
    player = Player(pong.screen_rect.width // 2, pong.screen_rect.height - 100)
    computer = Computer(pong.screen_rect.width // 2, 0 + 100)

    sprite_list = pygame.sprite.Group()
    sprite_list.add(player.paddle, computer.paddle, pong.ball)

    while True:
        pong.draw_bg()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pong.paused is True:
                        pong.paused = False
                    else:
                        pong.paused = True

        if pong.paused is True:
            pong.draw_pause()
        else:
            sprite_list.update(pong)

        sprite_list.draw(pong.screen)
        pong.ball.draw(pong.screen)

        pong.update()
        pong.tick()


main()
