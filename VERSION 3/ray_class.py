
import pygame

class Ray:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = -10
        self.width = 3
        self.height = 20
        self.color = (255, 255, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed