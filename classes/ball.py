import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = 10
        self.size = size
        self.colour = (255, 255, 255)
        self.just_spawned = True

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x_pos, self.y_pos), self.size)

    def update(self):
        if self.just_spawned is True:
            self.y_pos += self.speed
            self.just_spawned = False
