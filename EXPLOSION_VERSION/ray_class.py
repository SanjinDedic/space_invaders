import pygame

class Ray:
    def __init__(self, x, y):
        """
        Initializes the ray's position, speed, size, and color.

        Args:
        x (int): The x position of the ray on the screen.
        y (int): The y position of the ray on the screen.
        """
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = -25
        self.width = 3
        self.height = 25
        self.color = (255, 255, 255)

    def draw(self, surface):
        """
        Draws the ray on the given surface using Pygame.

        Args:
        surface (pygame.Surface): The surface to draw the ray on.
        """
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        """
        Updates the ray's position based on its y speed.
        """
        self.y += self.y_speed