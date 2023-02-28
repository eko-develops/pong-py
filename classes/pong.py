import pygame


from classes.ball import Ball


class Pong:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 850

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont("Arial Black", 20)
        self.font_colour = (255, 255, 255)
        self.bg_colour = (0, 0, 0)

        self.clock = pygame.time.Clock()
        self.framerate = 30

        self.ball = Ball(self.screen_width // 2, self.screen_height // 2, 20)

        self.paused = True

    def update(self):
        pygame.display.update()

    def tick(self):
        self.clock.tick(self.framerate)

    def draw_bg(self):
        self.screen.fill(self.bg_colour)

    def draw_pause(self):
        text = self.font.render("Press SPACE to START/PAUSE", True, self.font_colour)
        text_rect = text.get_rect()
        text_rect.center = (
            self.screen_rect.width // 2,
            (self.screen_rect.height // 2) - 50,
        )
        self.screen.blit(text, text_rect)
