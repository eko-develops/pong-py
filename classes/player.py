from classes.paddle import Paddle


class Player:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = "Player"
        self.paddle = Paddle(x_pos, y_pos)
