import pygame
import sys

vernum = pygame.version.vernum
if vernum.major < 2:
    print("Sorry, please update your pygame version")
    sys.exit()
elif vernum.major == 2:
    if vernum.minor < 4:
        print("Sorry, please update your pygame version")
        sys.exit()


import scene_class
import base_object_class
import position_class
import score_counter_class
import sound_class

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode([WIDTH, HEIGHT])
SCORE_FONT = pygame.font.SysFont('Comic Sans MS', 60)
c = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ------------------------------------------------
sound = sound_class.Sound()
scene = scene_class.Scene(WIDTH, HEIGHT, WHITE, sound)

ball_position = position_class.Position(200, 120)
ball = base_object_class.Ball(ball_position,BLACK, 20)

paddle1_position = position_class.Position(20, 0)
paddle1 = base_object_class.Paddle(paddle1_position, BLACK, "left paddle", 20, 70, [pygame.K_q, pygame.K_a])

paddle2_position = position_class.Position(760, 0)
paddle2 = base_object_class.Paddle(paddle2_position, BLACK, "right paddle", 20, 70, [pygame.K_o, pygame.K_l])

player1_score = score_counter_class.Counter(SCORE_FONT, BLACK, 1)
player2_score = score_counter_class.Counter(SCORE_FONT, BLACK, 0)
# ---------------------------------------
scene.add_object(ball, "ball")

scene.add_object(paddle1, "left paddle")

scene.add_object(paddle2, "right paddle")

scene.add_counter(player1_score, "player 1 score")

scene.add_counter(player2_score, "player 2 score")
# ---------------------------------------
def check_user_input():
    scene.handle_keyboard()


def run_ai():
    pass


def move_everything():
    scene.next_frame()


def resolve_collisions():
    scene.next_frame_collision()


def check_who_won():
    scene.check_if_won()


def play_sounds():
    scene.play_sounds()


def gameloop():
    check_user_input()
    run_ai()
    move_everything()
    resolve_collisions()
    play_sounds()
    check_who_won()
    scene.draw(window, BLACK)

# -------------------------------------------
while scene.running:
    gameloop()
    c.tick(30)
