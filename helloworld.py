import pygame, sys
import math
from pygame.locals import *


#global variables
screen_width = 800
screen_height = 600
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
game_over = False

pygame.init()
DISPLAYSURF = pygame.display.set_mode((screen_width,screen_height) ,0,24)
pygame.display.set_caption('dwab dwab revolution 2017')

#setting up colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


def intro():
	class Background(pygame.sprite.Sprite):
		def __init__(self, image_file, location):
			pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
			self.image = pygame.image.load(image_file)
			self.rect = self.image.get_rect()
			self.rect.left, self.rect.top = location

	end_it=False
	BackGround = Background('Untitled.png', [0,0])
	while (end_it==False):
		for event in pygame.event.get():
			DISPLAYSURF.fill([255, 255, 255])
			DISPLAYSURF.blit(BackGround.image, BackGround.rect)
			start = pygame.draw.rect(DISPLAYSURF, [0, 0, 0], (200, 400, 90, 30))
			quit = pygame.draw.rect(DISPLAYSURF, [0, 0, 0], (400, 400, 70, 30))
			myfont=pygame.font.SysFont("Britannic Bold", 40)
			title=myfont.render("DWABP DWABP REVOLUTION 2017", 1, (255, 0, 0))
			quittext=myfont.render("QUIT", 1, (255, 0, 0))
			starttext=myfont.render("START", 1, (255, 0, 0))
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos() # gets mouse position
				if start.collidepoint(mouse_pos):
					end_it = True
				if quit.collidepoint(mouse_pos):
					pygame.quit()
					sys.exit()
			DISPLAYSURF.blit(title,(200,200))
			DISPLAYSURF.blit(starttext,(200,400))
			DISPLAYSURF.blit(quittext, (400,400))
			pygame.display.flip()

#intro
intro()

#initialising surface
DISPLAYSURF.fill(WHITE)
#body:
pygame.draw.rect(DISPLAYSURF, RED, (body_top_left_x,body_top_left_y,body_width,body_height))
#head:
pygame.draw.circle(DISPLAYSURF, RED, (head_x, head_y),head_rad, 0)
#left upper arm:
pygame.draw.line(DISPLAYSURF, BLACK, (left_should_x,left_should_y),(left_elbow_x,left_elbow_y),arm_thiccness)
#lower left arm:
#pygame.draw.line(DISPLAYSURF, BLACK, (left_elbow_x, left_elbow_y),(left_hand_x,left_hand_y),arm_thiccness)

counter  = 0

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 30)

# render text
angle = 2*math.pi - (math.pi-math.acos((left_elbow_y-body_height)/arm_length))



#timer
seconds = 0
start_ticks = pygame.time.get_ticks()

while True:
    #clear screen
    DISPLAYSURF.fill(WHITE)
    counterLabel = myfont.render("SCORE: "+str(counter), 1, RED)
    DISPLAYSURF.blit(counterLabel, (5, 5))
    #redraw static images
    #body:
    pygame.draw.rect(DISPLAYSURF, RED, (body_top_left_x,body_top_left_y,body_width,body_height))
    #head:
    pygame.draw.circle(DISPLAYSURF, RED, (head_x, head_y),head_rad, 0)
    #left upper arm:
    pygame.draw.line(DISPLAYSURF, BLACK, (left_should_x,left_should_y),(left_elbow_x,left_elbow_y),arm_thiccness)
    #lower left arm:
    #pygame.draw.line(DISPLAYSURF, BLACK, (left_elbow_x, left_elbow_y),(left_hand_x,left_hand_y),arm_thiccness)

    if game_over == False:
        angle = max(math.pi/2,angle-0.001)
        left_elbow_x = arm_length*math.cos(angle) + left_should_x
        left_elbow_y = arm_length*math.sin(angle) + left_should_y

        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        #if seconds>30:
            #game_over = True
        timer_label = myfont.render("TIME REMAINING: "+str(30-seconds),1,RED)
        DISPLAYSURF.blit(timer_label, (screen_width-400,5))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    angle += 0.3
                    counter+=1
                    #raise left elbow
                    print "q pressed"
                    print "test"
                    left_elbow_x = arm_length*math.cos(angle) + left_should_x
                    left_elbow_y = arm_length*math.sin(angle) + left_should_y
    else:
        #display end screen
        break


    pygame.display.update()