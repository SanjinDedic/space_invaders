import pygame

class Ray:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = -25
        self.width = 3
        self.height = 25
        self.color = (255, 255, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.y_speed
