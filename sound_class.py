
import pygame.mixer


pygame.mixer.init()

paddle_hit = pygame.mixer.Sound("paddle_hit.mp3")
beep = pygame.mixer.Sound("Beep Short .mp3")
win = pygame.mixer.Sound("Puppy Love (Sting) - Twin Musicom.mp3")


class Sound:
    def play_hit(self):
        paddle_hit.play()

    def play_point(self):
        beep.play()

    def play_win(self):
        win.play()
