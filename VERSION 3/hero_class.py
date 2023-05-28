import pygame
#in comments summarise the class below and list its attributes and methods
#this class is used to create hero objects that are used in the game
#the attributes are the x and y coordinates, the x and y speed, the width and height, the score and the color
#the methods are the draw, move and increase_score methods

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.width = 50
        self.height = 20
        self.score = 0
        self.color = (255, 0, 255)
        self.image = pygame.image.load('assets/hero2.JPG')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def set_x_speed(self, speed):
        self.x_speed = speed

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def increase_score(self):
        self.score += 1