import pygame

import os

class Hero:
    def __init__(self, x, y):
        """
        Initializes the hero's position, speed, size, and color.
        Args:
        x (int): The x position of the hero on the screen.
        y (int): The y position of the hero on the screen.
        """
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.width = 60
        self.height = 20
        self.color = (255, 0, 255)
        self.score = 0

    def set_x_speed(self, speed):
        """
        Sets the hero's x speed to the given speed.

        Args:
        speed (int): The new x speed of the hero.
        """
        self.x_speed = speed


    def draw(self, surface):
        """
        Draws the hero on the given surface using Pygame.

        Args:
        surface (pygame.Surface): The surface on which to draw the hero.
        """
        # Load the hero image from the file
        hero_image = pygame.image.load(os.path.join("assets", "hero2.JPG"))

        # Scale the hero image to the size of the hero object
        hero_image = pygame.transform.scale(hero_image, (self.width, self.height))

        # Draw the hero image on the surface at the hero's position
        surface.blit(hero_image, (self.x, self.y))

    def increase_score(self):
        """
        Increases the hero's score by 1.
        """
        self.score += 1

    def move(self):
        """
        Updates the hero's position based on its x speed.
        """
        self.x += self.x_speed