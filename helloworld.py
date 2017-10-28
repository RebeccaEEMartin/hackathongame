import pygame, sys
from pygame.locals import *

#global variables
screen_width = 400
screen_height = 300
body_top_left_x = screen_width/3
body_top_left_y = screen_height/2
body_width = screen_width/3
body_height = screen_height/2
head_rad = 30
head_x = screen_width/2
head_y = screen_height/2 - head_rad

pygame.init()
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('dwab dwab revolution 2017')

#setting up colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#initialising surface
DISPLAYSURF.fill(WHITE)
#body:
pygame.draw.rect(DISPLAYSURF, RED, (body_top_left_x,body_top_left_y,body_width,body_height))
#head:
pygame.draw.circle(DISPLAYSURF, RED, (head_x, head_y),head_rad, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()