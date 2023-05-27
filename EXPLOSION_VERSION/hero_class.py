import pygame

import os

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.width = 60
        self.height = 20
        self.color = (255, 0, 255)
        self.score = 0

    def set_x_speed(self, speed):
        self.x_speed = speed


    def draw(self, surface):
        hero_image = pygame.image.load(os.path.join("assets", "hero2.JPG"))
        hero_image = pygame.transform.scale(hero_image, (self.width, self.height))
        surface.blit(hero_image, (self.x, self.y))

    def increase_score(self):
        self.score += 1

    def move(self):
        self.x += self.x_speed