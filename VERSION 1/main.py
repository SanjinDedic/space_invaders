import pygame
import random
from hero_class import Hero
from enemy_class import Enemy
from ray_class import Ray

# Define constants for the game window size and enemy speed
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
ENEMY_SPEED = 1

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Create a hero object
hero = Hero(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)

# Create an empty list for rays and enemies
rays = []
enemies = []
game_on = True

# Set up the event loop
# game_on = True
clock = pygame.time.Clock()
enemy_timer = pygame.time.get_ticks()
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.set_x_speed(-10)
            elif event.key == pygame.K_RIGHT:
                hero.set_x_speed(10)
            elif event.key == pygame.K_SPACE:
                # Create a new ray object and add it to the list
                ray = Ray(hero.x + hero.width // 2, hero.y)
                rays.append(ray)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and hero.x_speed < 0:
                hero.set_x_speed(0)
            elif event.key == pygame.K_RIGHT and hero.x_speed > 0:
                hero.set_x_speed(0)

    # Move the hero
    hero.move()

    # Create a new enemy every 3 seconds and add it to the enemies list
    current_time = pygame.time.get_ticks()
    if current_time - enemy_timer >= 2000:
        enemy_x = random.randint(0, SCREEN_WIDTH - 20)
        enemy = Enemy(enemy_x, 0, y_speed = ENEMY_SPEED)
        enemies.append(enemy)
        enemy_timer = current_time

    # Move and draw the rays, enemies, and hero, and update the display
    enemies_to_remove = []
    screen.fill((0, 0, 0))
    hero.draw(screen)
    for enemy in enemies:
        print(enemy.x_speed, enemy.y_speed)
        enemy.move()
        enemy.draw(screen)
    for ray in rays:
        ray.move()
        ray.draw(screen)
        for enemy in enemies:
            if enemy.sense_collision(ray):
                rays.remove(ray)
                enemy.life -= 1
                if enemy.life <= 0:
                    enemy.y = 0
                    enemy.x = random.randint(0, SCREEN_WIDTH - 20)
                    enemies.remove(enemy)
                    hero.increase_score()
                    break
    pygame.display.update()

    # Limit the fps to 30
    clock.tick(30)

# Quit Pygame
pygame.quit()