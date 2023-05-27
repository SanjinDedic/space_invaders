import pygame

class Enemy:
    def __init__(self, x, y, x_speed = 0, y_speed=1, w = 50, h = 50):
        """
        Initializes the enemy's position, speed, size, and color.
        """
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.width = w
        self.height = h
        self.color = (0, 255, 0)
        self.life = 5

    def draw(self, surface):
        """
        Draws the enemy on the screen.

        Args:
        surface (pygame.Surface): The surface to draw the enemy on.
        """
        enemy_image = pygame.image.load("assets/invader2.JPG")

        # Scale the hero image to the size of the hero object
        hero_image = pygame.transform.scale(enemy_image, (self.width, self.height))

        # Draw the hero image on the surface at the hero's position
        surface.blit(hero_image, (self.x, self.y))

    def move(self):
        """
        Updates the enemy's position by adding the y_speed to the y position.
        """
        self.y += self.y_speed
        self.x += self.x_speed




    def sense_collision(self, other):
        """
        Checks if the enemy has collided with an other.

        Args:
        other (other): The other to check for collision with.

        Returns:
        bool: True if the enemy has collided with the other, False otherwise.
        """
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        other_rect = pygame.Rect(other.x, other.y, other.width, other.height)
        if enemy_rect.colliderect(other_rect):
            return True
        return False