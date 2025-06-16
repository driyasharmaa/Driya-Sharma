import pygame
import sys 
import random 

# Initialize pygame 
pygame.init() 

# Screen setup 
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption("Sprites with Colour change event")
clock = pygame.display.Clock() 
FPS = 60 

# Custom event 
CHANGE_COLOUR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOUR_EVENT, 1500) # every 2 seconds 

# Define a Sprite class 
class ColourChangingSprite(pygame.sprite.Sprite): 
    def __init__(self, x, y, width, height, colour): 
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.colour = colour 
        self.image = fill(self.colour)
        self.rect = self.image.get_rect(topleft = (x, y))

    def change_colour(self): 
        self.colour = (
            random.randit(0,255),
            random.randit(0,255),
            random.randit(0,255)
        )
    self.image.fill(self,colour)

# Create two sprite instances 
sprite1 = ColourChangingSprite(200, 250, 60, 60, (255, 0, 0)) # Red 
sprite2 = ColourChangingSprite(200, 250, 60, 60, (0, 0, 255)) # Blue

# Group sprites for easy drawing
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop 
running = True 
while running: 
    clock.tick(FPS)

    for evet in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == CHANGE_COLOUR_EVENT: 
            sprite1.change_colour()
            sprite2.change_colour()

    screen.fill((30,30,30)) # Background
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit() 
sys.exit()