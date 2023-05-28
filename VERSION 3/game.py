import pygame
import random
import time

from hero_class import Hero
from ray_class import Ray
from enemy_class import Enemy
from debris_class import Debris



# Define constants for the game window size and enemy speed
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game:
    def __init__(self):
        pygame.init()
        self.rays = []
        self.enemies = []
        self.debris_list = []
        self.score = 0
        self.game_on = True
        self.game_won = False
        self.game_over = False
        self.enemy_timer = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()
        self.game_over_font = pygame.font.Font(None, 100)


        # Set up the game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Game")

        # Create the hero object
        self.hero = Hero(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hero.set_x_speed(-10)
                elif event.key == pygame.K_RIGHT:
                    self.hero.set_x_speed(10)
                elif event.key == pygame.K_SPACE:
                    # Create a new ray object and add it to the list
                    ray = Ray(self.hero.x + self.hero.width // 2, self.hero.y)
                    self.rays.append(ray)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.hero.x_speed < 0:
                    self.hero.set_x_speed(0)
                elif event.key == pygame.K_RIGHT and self.hero.x_speed > 0:
                    self.hero.set_x_speed(0)


    def check_win(self):
        if self.score >= 20:
            self.game_won = True

    def update_hero_and_rays(self):
        # Update the hero's position
        self.hero.move()

        # Update all rays
        for ray in self.rays:
            ray.update()

            # Remove the ray if it goes off the screen
            if ray.y < 0:
                self.rays.remove(ray)

    def update_debris(self):
        for debris in self.debris_list:
            debris.update()

    def update_enemies_and_check_collisions(self):
        # Spawn a new enemy every 2 seconds
        if pygame.time.get_ticks() - self.enemy_timer > 2000:
            self.enemies.append(Enemy( x = random.randint(0, SCREEN_WIDTH), y = 0))
            self.enemy_timer = pygame.time.get_ticks()
        
        # Update all enemies
        for enemy in self.enemies:
            enemy.move(1 + self.score/10)
            if enemy.y > SCREEN_HEIGHT:
                self.game_over = True
            for ray in self.rays:
                if enemy.sense_collision(ray):
                    self.rays.remove(ray)
                if enemy.is_dead():
                    self.enemies.remove(enemy)
                    for i in range(0, 20):
                        self.debris_list.append(Debris(enemy.x, enemy.y))
                    self.score += 1 
                    break


    def draw_everything(self):
        # Draw the background
        self.screen.fill((0, 0, 0))

        # Draw the hero
        self.hero.draw(self.screen)

        # Draw the rays
        for ray in self.rays:
            ray.draw(self.screen)

        # Draw the debris
        for debris in self.debris_list:
            debris.draw(self.screen)
        
        # Draw the enemies
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Draw the score
        self.draw_score()
        if self.game_over:
            game_over_text = self.game_over_font.render("GAME OVER", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(game_over_text, game_over_rect)
            pygame.display.update()
            time.sleep(5)
            self.game_on = False
        if self.game_won:
            game_over_text = self.game_over_font.render("YOU WIN", True, (0, 0, 255))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(game_over_text, game_over_rect)
            pygame.display.update()
            time.sleep(5)
            self.game_on = False

        # Update the display
        pygame.display.update()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def run(self):
        while self.game_on:
            self.handle_events()
            self.update_hero_and_rays()
            self.update_debris()
            self.update_enemies_and_check_collisions()
            self.draw_everything()
            self.check_win()
            self.clock.tick(60)

        pygame.quit()


game = Game()
game.run()