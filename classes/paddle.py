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

    def update(self, pong):
        x_mouse_pos = pygame.mouse.get_pos()[0]
        max_width = pong.screen_rect.width
        self.x_pos = x_mouse_pos

        if (self.x_pos + self.width // 2) >= max_width:
            self.x_pos = max_width - (self.width // 2)

        if (self.x_pos - self.width // 2) <= 0:
            self.x_pos = 0 + (self.width // 2)

        self.rect.center = (self.x_pos, self.y_pos)
