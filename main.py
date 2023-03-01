import sys

import pygame

from classes.pong import Pong
from classes.player import Player, Computer

pygame.init()


def main():
    pong = Pong()
    player = Player(pong)
    computer = Computer(pong)

    sprite_list = pygame.sprite.Group()
    sprite_list.add(player.paddle, computer.paddle)

    while True:
        pong.draw_bg()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    """Pause Game
                    When game is paused, we need to take into account how much
                    time has passed while paused.
                    """
                    if pong.paused is True:
                        pong.paused = False
                        pong.pause_time = pong.get_time() - pong.pause_time
                    else:
                        pong.paused = True
                        pong.pause_time = pong.get_time() - pong.pause_time
                if event.key == pygame.K_r:
                    """Reset game"""
                    pong.reset_game(sprite_list)
                    sprite_list.draw(pong.screen)

        if pong.paused is False:
            current_time = pong.get_time()
            if pong.scored is True:
                pong.reset_scored()
                sprite_list.draw(pong.screen)
            else:
                """Handle ball hitting paddles"""
                paddle_hit_list = pygame.sprite.spritecollide(
                    pong.ball, sprite_list, False
                )
                pong.ball.handle_paddle_hit(paddle_hit_list)

                """Level up every n seconds"""
                seconds = 10
                level_up_ms = seconds * 1000
                elapsed_time = current_time - pong.last_update - pong.pause_time
                print(elapsed_time)
                """Levels up ball"""
                if elapsed_time >= level_up_ms and pong.ball.speed <= 20:
                    pong.ball.speed += 1
                    pong.last_update = current_time
                    pong.pause_time = 0

                sprite_list.update(pong)
                pong.ball.update(pong, player, computer)

        else:
            """Game paused"""
            # pong.pause_time = pong.get_time() - pong.pause_time
            pong.draw_pause()

        sprite_list.draw(pong.screen)
        pong.ball.draw(pong.screen)
        for sprite in (player, computer):
            sprite.draw_player_board()
        pong.draw_level()

        pong.update()
        pong.tick()


main()
