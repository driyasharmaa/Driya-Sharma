import pygame
import sys 

# Initialize pygame
pygame.init()

# Set screen size
screen_width = 800
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))

#Set the title of the game window 
pygame.display.set_caption("My first game screen")

# Game loop 
running = True 
while running: 
    # Handle events
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            runnning = False 

    # Update the display 
    pygame.display.flip()

# Quit pygame 
pygame.quit()
sys.exit()