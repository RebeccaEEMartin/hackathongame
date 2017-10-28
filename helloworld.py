import pygame, sys
import math
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
arm_length = 80
left_should_x = body_top_left_x
left_should_y = body_top_left_y
left_elbow_x = left_should_x - 20
left_elbow_y = left_should_y + arm_length
left_hand_x = 50
left_hand_y = 250
arm_thiccness = 30

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
#left upper arm:
pygame.draw.line(DISPLAYSURF, BLACK, (left_should_x,left_should_y),(left_elbow_x,left_elbow_y),arm_thiccness)
#lower left arm:
pygame.draw.line(DISPLAYSURF, BLACK, (left_elbow_x, left_elbow_y),(left_hand_x,left_hand_y),arm_thiccness)

counter  = 0

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render(str(counter), 1, RED)
DISPLAYSURF.blit(label, (5, 5))

#timer
seconds = 0
start_ticks = pygame.time.get_ticks()

while True:
    #clear screen
    DISPLAYSURF.fill(WHITE)
    #redraw static images
    #body:
    pygame.draw.rect(DISPLAYSURF, RED, (body_top_left_x,body_top_left_y,body_width,body_height))
    #head:
    pygame.draw.circle(DISPLAYSURF, RED, (head_x, head_y),head_rad, 0)
    #left upper arm:
    pygame.draw.line(DISPLAYSURF, BLACK, (left_should_x,left_should_y),(left_elbow_x,left_elbow_y),arm_thiccness)
    #lower left arm:
    pygame.draw.line(DISPLAYSURF, BLACK, (left_elbow_x, left_elbow_y),(left_hand_x,left_hand_y),arm_thiccness)

    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    if seconds>30:
        break
    timer_label = myfont.render(str(seconds),1,RED)
    DISPLAYSURF.blit(timer_label, (screen_width-30,5))
    print seconds
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                counter+=1
                label = myfont.render(str(counter), 1, RED)
                DISPLAYSURF.blit(label, (5, 5))
                #raise left elbow
                print "q pressed"
                print "test"
                left_elbow_x = arm_length*math.cos(math.pi/120) + left_should_x
                left_elbow_y = arm_length*math.sin(math.pi/120) + left_should_y
    pygame.display.update()