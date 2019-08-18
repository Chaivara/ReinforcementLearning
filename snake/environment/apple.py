
# https://www.youtube.com/watch?v=AaGK-fj-BAM&t=630s
import pygame
import random

# ToDo:
# check if there is already a snake


class Apple:

    def __init__(self, screen, s_width, s_height, color, scale):

        self.screen = screen
        self.s_width = s_width
        self.s_height = s_height
        self.color = color
        self.scale = scale

        self.place_apple(None)

    def draw(self):
        rect = pygame.rect.Rect(self.x, self.y, self.scale, self.scale)
        pygame.draw.rect(self.screen, self.color, rect)

    def eat(self, snake_x, snake_y, tail):
        if self.x == snake_x and self.y == snake_y:
            self.place_apple(tail)
            return True
        return False

    def place_apple(self, tail):

        cols = (self.s_width - self.scale) / self.scale
        rows = (self.s_height - self.scale) / self.scale

        rand_x = 0
        rand_y = 0

        bad_position = True

        if tail is None:
            bad_position = False
            rand_x = random.randint(0, cols)
            rand_y = random.randint(0, rows)

        while bad_position:
            bad_position = False

            rand_x = random.randint(0, cols)
            rand_y = random.randint(0, rows)

            for i in tail:
                if rand_x == i.x and rand_y == i.y:
                    bad_position = True
                    break

        self.x = rand_x * self.scale
        self.y = rand_y * self.scale
