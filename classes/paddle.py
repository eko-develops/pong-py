import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 100
        self.height = 20
        self.colour = (255, 255, 255)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.colour)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self, pong):
        x_mouse_pos = pygame.mouse.get_pos()[0]
        screen_max_width = pong.screen_rect.width
        self.x_pos = x_mouse_pos

        """Pad if paddle hitting right"""
        if (self.x_pos + self.width // 2) >= screen_max_width:
            self.x_pos = screen_max_width - (self.width // 2)

        """Pad if paddle hitting left"""
        if (self.x_pos - self.width // 2) <= 0:
            self.x_pos = 0 + (self.width // 2)

        self.rect.center = (self.x_pos, self.y_pos)

    def reset_update(self, pong):
        self.x_pos = pong.screen_rect.width // 2
        self.rect.center = (self.x_pos, self.y_pos)
