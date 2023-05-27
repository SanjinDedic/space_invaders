import pygame
import random

class Debris:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = random.randint(-5, 5)
        self.y_speed = random.randint(-5, 5)
        self.life_span = 30  # Lasts for 1 second if your game runs at 30FPS
        self.color = (255, 0, 0)  # Red color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, 5, 5))

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
