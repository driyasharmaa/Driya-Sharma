import pygame
import sys
# Initialize pygame 
pygame.init()

# Set screen size 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game window 
pygame.display.set_caption("Game screen with Elements")

#Define rectangle colour and position
rect_colour = (255, 100, 100) #Light pink 
rect_x = 300
rect_y = 200
rect_width = 200
rect_height = 100

# Game loop
running = True 
while running: 
    # Event handling 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT(): 
            running = False

    # Update the display 
    pygame.display.flip()

# Quit pygame 
pygame.quit()
sys.exit() 