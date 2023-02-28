import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.x_dir = 1
        self.y_pos = y_pos
        self.y_dir = 1
        self.speed = 10
        self.size = size
        self.colour = (255, 255, 255)

        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.colour)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

        self.just_spawned = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x_pos, self.y_pos), self.size)

    def update(self, pong):
        max_height = pong.screen_rect.height
        max_width = pong.screen_rect.width

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

        self.rect.center = (self.x_pos, self.y_pos)

    def reset_update(self, pong):
        self.x_pos = pong.screen_rect.width // 2
        self.y_pos = pong.screen_rect.height // 2

    def handle_paddle_hit(self, paddle_hit_list):
        for _ in paddle_hit_list:
            self.y_dir = self.y_dir * -1
