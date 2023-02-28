import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, pong, x_pos, y_pos, size):
        self.pong = pong
        self.x_pos = x_pos
        self.x_dir = 1
        self.y_pos = y_pos
        self.y_dir = 1
        self.speed = 10
        self.size = size
        self.colour = (255, 255, 255)
        self.just_spawned = True

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x_pos, self.y_pos), self.size)

    def update(self):
        max_height = self.pong.screen_rect.height
        max_width = self.pong.screen_rect.width
        print((self.x_pos, self.y_pos))
        if self.just_spawned is True:
            self.y_pos = self.y_pos + (self.y_dir * self.speed)
            self.x_pos = self.x_pos + (self.x_dir * self.speed)
            self.just_spawned = False
        elif self.x_pos + self.size >= max_width:
            self.x_dir = -1
        elif self.x_pos - self.size <= 0:
            self.x_dir = 1
        elif self.y_pos + self.size >= max_height:
            self.y_dir = -1
        elif self.y_pos - self.size <= 0:
            self.y_dir = 1

        self.x_pos = self.x_pos + (self.x_dir * self.speed)
        self.y_pos = self.y_pos + (self.y_dir * self.speed)
