import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed

        # Keep player on screen
        self.rect.clamp_ip(screen.get_rect())

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        )

# Groups
player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create 7 enemies
for _ in range(7):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

# Score variable
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Check for collisions
    collided_enemies = pygame.sprite.spritecollide(player, enemies, dokill=True)
    score += len(collided_enemies)

    # Redraw enemies if needed
    for _ in collided_enemies:
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
