import pygame
from math import pi
import numpy as np
 
# Initialize the game engine
pygame.init()
def draw_map(listPoint, size):
    screen.fill(WHITE)
    for i in range(0, len(listPoint)):
        for j in range(0, len(listPoint[i])):
            if listPoint[i][j] == 0:
                pygame.draw.rect(screen, BLACK, [i*size, j*size, size, size], 2)
            else:
                pygame.draw.rect(screen, BLACK, [i*size, j*size, size, size])
            j += 1
        i += 1

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [22*50, 18*50]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
    # Clear the screen, set the screen background, and drawmap
    map = np.full((23, 18),0)
    map[5][5]=1
    print(map)
    draw_map(map, 50)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
