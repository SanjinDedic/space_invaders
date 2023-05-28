import pygame
#in comments summarise the class below and list its attributes and methods
#this class is used to create enemy objects that are used in the game
#the attributes are the x and y coordinates, the x and y speed, the width and height, the life and the color
#the methods are the draw, move and sense_collision methods

import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 1
        self.width = 50
        self.height = 50
        self.life = 5
        self.color = (0, 255, 0)
        self.image = pygame.image.load('assets/invader2.JPG')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self,speed):
        self.x += self.x_speed
        self.y += speed

    def sense_collision(self, other_ray):
        self_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        other_rect = pygame.Rect(other_ray.x, other_ray.y, other_ray.width, other_ray.height)
        if self_rect.colliderect(other_rect):
            self.life -= 1
            return True
        return False
    
    def is_dead(self):
        return self.life <= 0
