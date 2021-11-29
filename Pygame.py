# shyan huff, 11/29/21

import pygame, sys 
from pygame.locals import *

# start PyGame 
pygame.init() 
# Create Game Window
windowSurface = pygame.display.set_mode( (500,400)0, 32)
pygame.display.set_caption("Hello, world!")

# Set Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup Fonts 
basicFont = pygame.font.SysFont(None, 48)

# Setup Text
text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centerx = windowSurface.get_rect().centerx

# Draw background into window surface. 
windowSurface.fill(WHITE)

# Draw a green polygon into the surface =. 
pygame.draw.polygame(windowSurface, RED, ((146, 0),(291, 106),(236, 277), (0, 106)))

# Draw red lines on the windowSurface
pygame.draw.line(windowSurface, RED, (60, 60), (120, 60), 4 )
pygame.draw.line(windowSurface, RED, (120, 60), (60, 120))
pygame.draw.line(windowSurface, RED, (60, 120), (120, 120), 4)

# Draw a circle 

