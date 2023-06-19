
import pygame
import time


class Scene:
    def __init__(self, width, height, color, sound):
        self.width = width
        self.height = height
        self.color = color
        self.object_dict = {}
        self.counter_dict = {}
        self.input_keys = [pygame.K_q, pygame.K_a, pygame.K_o, pygame.K_l]
        self.running = True
        self.playing = True
        self.sound = sound
        self.play_paddle_sound = False
        self.play_point_sound = False
        self.p1_winning_screen = pygame.image.load("p1_winning_screen.png")
        self.p2_winning_screen = pygame.image.load("p2_winning_screen.png")
        self.winning_screen = None
        self.played_winning_sound = False

    def add_object(self, obj, name):
        self.object_dict[name] = obj

    def add_counter(self, counter, name):
        self.counter_dict[name] = counter

    def handle_keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        if self.playing:
            all_keys = pygame.key.get_pressed()
            for key in self.input_keys:
                if all_keys[key]:
                    for obj in list(self.object_dict.values()):
                        obj.handle_key(key)

    def next_frame(self):
        if self.playing:
            for obj in list(self.object_dict.values()):
                obj.move_to_next_frame()

    def next_frame_collision(self):
        if self.playing:
            # adjust objects so they don't fall off the scene
            for obj in list(self.object_dict.values()):
                if "paddle" in obj.type:
                    if obj.position.y <= 0:
                        obj.decide_position(obj.position.x, 0)
                        obj.update_variables()
                    if obj.position.y + obj.rect.height >= self.height:
                        obj.decide_position(obj.position.x, self.height - obj.rect.height)
                        obj.update_variables()
                elif obj.type == "ball":
                    if obj.position.x + obj.radius >= self.width:
                        self.counter_dict["player 1 score"].add_score()
                        self.object_dict["ball"].reset(self.width / 2, self.height / 2)
                        self.play_point_sound = True
                    elif obj.position.x - obj.radius <= 0:
                        self.counter_dict["player 2 score"].add_score()
                        self.object_dict["ball"].reset(self.width / 2, self.height / 2)
                        self.play_point_sound = True
                    if obj.position.y + obj.radius >= self.height or obj.position.y - obj.radius <= 0:
                        obj.bounce("y")

            # check whether the ball hit the paddle. If so, reverse x momentum
            if self.object_dict["ball"].position.x - self.object_dict["ball"].radius <= self.object_dict["left paddle"].right_side\
                    and self.object_dict["ball"].position.y - self.object_dict["ball"].radius <= self.object_dict["left paddle"].bottom_side\
                    and self.object_dict["ball"].position.y + self.object_dict["ball"].radius >= self.object_dict["left paddle"].top_side:
                self.object_dict["ball"].bounce("x")
                self.play_paddle_sound = True
            elif self.object_dict["ball"].position.x + self.object_dict["ball"].radius >= self.object_dict["right paddle"].left_side\
                    and self.object_dict["ball"].position.y - self.object_dict["ball"].radius <= self.object_dict["right paddle"].bottom_side\
                    and self.object_dict["ball"].position.y + self.object_dict["ball"].radius >= self.object_dict["right paddle"].top_side:
                self.object_dict["ball"].bounce("x")
                self.play_paddle_sound = True

    def play_sounds(self):
        if self.playing:
            if self.play_paddle_sound:
                self.sound.play_hit()
                self.play_paddle_sound = False
            if self.play_point_sound:
                self.sound.play_point()
                self.play_point_sound = False
                time.sleep(1)
        elif self.playing is False and self.played_winning_sound is False:
            self.sound.play_win()
            self.played_winning_sound = True

    def check_if_won(self):
        for counter in self.counter_dict:
            if self.counter_dict[counter].check_did_win() and counter == "player 1 score":
                self.winning_screen = self.p1_winning_screen
                self.playing = False
            elif self.counter_dict[counter].check_did_win() and counter == "player 2 score":
                self.winning_screen = self.p2_winning_screen
                self.playing = False

    def display_winner(self, win):
        win.blit(self.winning_screen, (0, 0))

    def draw(self, win, line_color):
        win.fill(self.color)
        if self.playing:
            pygame.draw.line(win, line_color, (self.width / 2, 0), (self.width / 2, self.height))
            for obj in list(self.object_dict.values()):
                obj.draw(win)
            for score in list(self.counter_dict.values()):
                score.draw(win, self.width / 2)
        if self.playing is False:
            self.display_winner(win)
        pygame.display.flip()
