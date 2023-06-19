class Counter:
    def __init__(self, font, color, x_multiple):
        self.score = 0
        self.adding_value = 1
        self.font = font
        self.color = color
        self.y = 0
        self.x_multiple = x_multiple  # 0 is on the right, 1 is on the left

    def add_score(self):
        self.score += self.adding_value

    def check_did_win(self):
        if self.score == 5:
            return True
        return False

    def draw(self, win, screen_middle):
        text = self.font.render(str(self.score), False, self.color)
        text_x = screen_middle - (self.x_multiple * text.get_width())
        win.blit(text, (text_x, self.y))
