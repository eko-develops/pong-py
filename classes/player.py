from classes.paddle import Paddle


class Player:
    def __init__(self, pong):
        self.pong = pong
        self.x_pos = self.pong.screen_rect.width - 200
        self.y_pos = self.pong.screen_rect.height - 100
        self.name = "Player"
        self.paddle = Paddle(self.pong.screen_rect.width // 2, self.y_pos)
        self.score = 0

    def draw_player_board(self):
        player_name_text = self.pong.font.render(
            f"{self.name}: {self.score}", True, self.pong.font_colour
        )
        board_y = self.get_board_y()
        self.pong.screen.blit(player_name_text, (self.x_pos, board_y))

    def get_board_y(self):
        return self.y_pos + 25

    def add_point(self):
        self.score += 1


class Computer(Player):
    def __init__(self, pong):
        super().__init__(pong)

        self.y_pos = 100
        self.name = "Computer"
        self.paddle = Paddle(self.pong.screen_rect.width // 2, self.y_pos)

    def get_board_y(self):
        return self.y_pos - 50
