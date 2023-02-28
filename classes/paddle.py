import pygame


class Paddle:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 100
        self.height = 20
        self.colour = (255, 255, 255)

        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.rect.center = (self.x_pos, self.y_pos)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
