import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = 10
        self.size = size
        self.colour = (255, 255, 255)

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x_pos, self.y_pos), self.size)

    def update(self):
        self.x_pos += self.speed
