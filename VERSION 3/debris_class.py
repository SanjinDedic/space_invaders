#in comments summarise the class below and list its attributes and methods
#this class is used to create debris objects that are used in the game
#the attributes are the x and y coordinates, the x and y speed, the life span and the color
#the methods are the draw and move methods
import pygame
import random

class Debris:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = random.uniform(-5, 5)
        self.y_speed = random.uniform(-5, 5)
        self.life_span = 60
        self.color = (255, 55, 55)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 3)

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.life_span -= 1

