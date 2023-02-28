import pygame


from classes.ball import Ball


class Pong:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 850

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.framerate = 30

        self.ball = Ball(self.screen_width // 2, self.screen_height // 2, 20)

    def update(self):
        pygame.display.update()

    def tick(self):
        self.clock.tick(self.framerate)
