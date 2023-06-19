import vector_class
import pygame
import random


class Base_Object:
    def __init__(self, position, color, type):
        self.position = position
        self.color = color
        self.type = type

    def get_type(self):
        return self.type

    def handle_key(self, key):
        pass

    def move_to_next_frame(self):
        pass

    def collision_rules(self, width_limit, height_limit):
        pass

    def decide_position(self, new_x, new_y):
        self.position.x = new_x
        self.position.y = new_y

    def draw(self, win):
        pass


class Ball(Base_Object):
    def __init__(self, position, color, radius):
        super().__init__(position, color, "ball")
        self.vector = vector_class.Vector(5, 5)
        self.radius = radius

    def reset(self, new_x, new_y):
        self.decide_position(new_x, new_y)
        self.vector.x_momentum = random.choice([-5, 5])
        self.vector.y_momentum = random.choice([-5, 5])

    def move_to_next_frame(self):
        self.position.x += self.vector.x_momentum
        self.position.y += self.vector.y_momentum

    def bounce(self, flip_direction):
        if flip_direction == "x":
            self.vector.x_momentum *= random.uniform(-1.2, -1)
        if flip_direction == "y":
            self.vector.y_momentum *= random.uniform(-1.2, -0.8)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.position.x, self.position.y), self.radius, 5)


class Paddle(Base_Object):
    def __init__(self, position, color, type, width, height, keys_list):
        super().__init__(position, color, type)
        self.rect = pygame.Rect(position.x, position.y, width, height)
        self.left_side = position.x
        self.right_side = position.x + width
        self.top_side = position.y
        self.bottom_side = position.y + height
        self.keys_list = keys_list

    def update_variables(self):
        self.rect.x, self.rect.y = self.position.x, self.position.y
        self.left_side = self.position.x
        self.right_side = self.position.x + self.rect.width
        self.top_side = self.position.y
        self.bottom_side = self.position.y + self.rect.height

    def handle_key(self, key):
        if key == self.keys_list[0]:
            self.rect.move_ip(0, -10)
            self.position.y -= 10
            self.update_variables()
        if key == self.keys_list[1]:
            self.rect.move_ip(0, 10)
            self.position.y += 10
            self.update_variables()

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect, 5)
