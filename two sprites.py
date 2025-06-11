import pygame
import sys

# Initialize pygame 
pygame.init()

# Screen settings 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Two sprites Game")

# Colours
background_colour = (0,0,0)   # Black 
sprite1_colour = (0,255,0)    # Green - controllable 
sprite2_colour = (255,0,0)    #Red - static 

# Clock to control frame rate
clock = pygame.time.Click() 
FPS = 60

# Sprite dimension 
sprite_width = 50 
sprite_height = 50 

# Initial positions 
sprite1_x = 100 
sprite1_y = 100 

# Initial positions 
sprite2_x = 400
sprite2_y = 300 

# Speed of sprite1 
speed = 5

# Game loop 
running = True 
while running: 
    # Limit the loop to FPS
    clock.tick(FPS)

    # Handle events 
    for event in pygame.event.get() 
    if event.type == pygame.QUIT: 
        running = False 

    # Hndle key presses 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: 
        sprite1_x -= speed 
    if keys[pygame.K_RIGHT]: 
        sprite1_x += speed
    if keys[pygame.K_UP]: 
        sprite1_y -= speed 
    if keys[pygame.K_DOWN]: 
        sprite1_y += speed 

    # Draw sprites 
    pygame.draw.rect(screen, sprite1_colour, (sprite1_x, sprite1_y, sprite_height, sprite_width))
    pygame.draw.rect(screen, sprite1_colour, (sprite2_x, sprite2_y, sprite_height, sprite_width))

    # Update the display 
    pygame.displau.flip()

# Quit pygame 
pygame.quit() 
sys.exit()
