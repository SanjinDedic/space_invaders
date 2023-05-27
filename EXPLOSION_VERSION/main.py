import pygame
import random
import time
from hero_class import Hero
from enemy_class import Enemy
from ray_class import Ray
from debris_class import Debris


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

class Game:
    def __init__(self):
        self.rays = []
        self.enemies = []
        self.debris_list = []
        self.score = 0
        self.game_on = True
        self.game_won = False
        self.game_over = False
        self.enemy_timer = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.set_x_speed(-10)
                elif event.key == pygame.K_RIGHT:
                    hero.set_x_speed(10)
                elif event.key == pygame.K_SPACE:
                    # Create a new ray object and add it to the list
                    ray = Ray(hero.x + hero.width // 2, hero.y)
                    self.rays.append(ray)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and hero.x_speed < 0:
                    hero.set_x_speed(0)
                elif event.key == pygame.K_RIGHT and hero.x_speed > 0:
                    hero.set_x_speed(0)

    def spawn_enemy(self):
        if pygame.time.get_ticks() - self.enemy_timer > 2000:
            enemy = Enemy(random.randint(0, SCREEN_WIDTH), 0, y_speed=ENEMY_SPEED)
            self.enemies.append(enemy)
            self.enemy_timer = pygame.time.get_ticks()

    def update_hero_and_rays(self):
        hero.move()
        for ray in self.rays:
            ray.move()

    def update_debris(self):
        for debris in self.debris_list:
            debris.move()
            debris.life_span -= 1
            if debris.life_span <= 0:
                self.debris_list.remove(debris)

    def update_enemies_and_check_collisions(self):
        for enemy in self.enemies:
            enemy.move()
            if enemy.y > SCREEN_HEIGHT:
                self.enemies.remove(enemy)
                if self.score < 20:
                    self.game_over = True
                else:
                    self.game_won = True
            for ray in self.rays:
                if enemy.sense_collision(ray):
                    self.rays.remove(ray)
                if enemy.is_dead():
                    self.enemies.remove(enemy)
                    self.score += 1
                    for i in range(10):
                        debris = Debris(enemy.x, enemy.y)
                        self.debris_list.append(debris)
        if self.score > 10:
            self.game_won = True
            self.game_on = False

    def draw_everything(self, screen):
        screen.fill((0, 0, 0))
        hero.draw(screen)
        for ray in self.rays:
            ray.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen )
        for debris in self.debris_list:
            debris.draw(screen)
        self.draw_score(screen, self.score)
        if self.game_over:
            self.draw_text(screen, "GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100, (255, 0, 0))
            pygame.display.flip()
            time.sleep(5)
        elif self.game_won:
            self.draw_text(screen, "YOU WIN", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100, (0, 255, 0))
            pygame.display.flip()
            time.sleep(5)
        pygame.display.flip()

    def draw_score(self, screen, score):
        """Draw the score on the screen."""
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def draw_text(self, surface, text, x, y, size, color):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def run(self, screen):
        while self.game_on:
            self.handle_events()
            self.spawn_enemy()
            self.update_hero_and_rays()
            self.update_debris()
            self.update_enemies_and_check_collisions()
            self.draw_everything(screen)
            if self.game_over:
                print("Game over!")
                self.game_on = False
            elif self.game_won:
                print("You won!")
                self.game_on = False
            self.clock.tick(60)


game = Game()
game.run(screen)