import pygame, sys
import math
from pygame.locals import *
from random import randint
import randomdotorg

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
arm_thiccness = 30
game_over = False

pygame.init()
DISPLAYSURF = pygame.display.set_mode((screen_width,screen_height) ,0,24)
pygame.display.set_caption('dwab dwab revolution 2017')

#setting up colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,0)
myfont=pygame.font.SysFont("Britannic Bold", 40)
counter  = 0

class upload_image(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def left_dab():
    dab_label = myfont.render("LEFT DAB",1, RED)
    DISPLAYSURF.blit(dab_label, (300, 50))

def right_dab():
    dab_label = myfont.render("RIGHT DAB",1, RED)
    DISPLAYSURF.blit(dab_label, (300, 50))

def random_dab():
    r = randomdotorg.RandomDotOrg("shoob")
    random_int = r.randint(0, 9)
    if random_int > 4:
        return "right"
    else:
        return "left"

def intro():
	end_it=False
	BackGround = upload_image('Untitled.png', [0,0])
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
					print("here")
					end_it = True
				if quit.collidepoint(mouse_pos):
					pygame.quit()
					sys.exit()
			DISPLAYSURF.blit(title,(200,200))
			DISPLAYSURF.blit(starttext,(200,400))
			DISPLAYSURF.blit(quittext, (400,400))
			pygame.display.flip()

counter  = 0

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 30)


def outro(num):
	end_it=False
	BackGround = upload_image('Untitled2.png', [0,0])
	while (end_it==False):
		for event in pygame.event.get():
			DISPLAYSURF.fill([255, 255, 255])
			DISPLAYSURF.blit(BackGround.image, BackGround.rect)
			start = pygame.draw.rect(DISPLAYSURF, [0, 0, 0], (200, 400, 90, 30))
			quit = pygame.draw.rect(DISPLAYSURF, [0, 0, 0], (400, 400, 70, 30))
			myfont=pygame.font.SysFont("Britannic Bold", 40)
			title=myfont.render("HAHA UNLUCKY MATE", 1, (255, 0, 0))
			score=myfont.render("SCORE: " + str(num), 1, (255, 0, 0))
			quittext=myfont.render("QUIT", 1, (255, 0, 0))
			starttext=myfont.render("MENU", 1, (255, 0, 0))
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos() # gets mouse position
				if start.collidepoint(mouse_pos):
					end_it = True
				if quit.collidepoint(mouse_pos):
					pygame.quit()
					sys.exit()
			DISPLAYSURF.blit(title,(200,200))
			DISPLAYSURF.blit(score,(200,300))
			DISPLAYSURF.blit(starttext,(200,400))
			DISPLAYSURF.blit(quittext, (400,400))
			pygame.display.flip()

def main_game():
    arm_length = 120
    start_ticks = pygame.time.get_ticks()
    left_elbow_x = left_should_x - 20
    left_elbow_y = left_should_y + arm_length
    left_hand_x = left_elbow_x
    left_hand_y = left_elbow_y + arm_length

    #right arm
    right_should_x = body_top_left_x + body_width
    right_should_y = body_top_left_y
    right_elbow_x = right_should_x
    right_elbow_y = right_should_y + arm_length
    right_hand_x = right_elbow_x
    right_hand_y = right_elbow_y + arm_length

    #initialising surface
    DISPLAYSURF.fill(WHITE)
    #body:
    doug = upload_image('doug.png', [body_top_left_x,body_top_left_y-200])
    DISPLAYSURF.blit(doug.image, doug.rect)
    #head:
    pygame.draw.circle(DISPLAYSURF, RED, (head_x, head_y),head_rad, 0)
    #left upper arm:
    #leftbicep = upload_image('dabbicepleft.png', [left_should_x,left_should_y])
    #DISPLAYSURF.blit(leftbicep.image, leftbicep.rect)
    pygame.draw.line(DISPLAYSURF, BLACK, (left_should_x,left_should_y),(left_elbow_x,left_elbow_y),arm_thiccness)
    #lower left arm:
    pygame.draw.line(DISPLAYSURF, BLUE, (left_elbow_x, left_elbow_y),(left_hand_x,left_hand_y),arm_thiccness)

    #angles
    left_shoulder_angle = math.pi/2
    left_elbow_angle = math.pi/2
    right_shoulder_angle = math.pi/2
    right_elbow_angle = math.pi/2

    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 30)

    #timer
    seconds = 0
    foundNumbers = []

    counter = 0
    direction_of_dab = "right"
    #doug = upload_image('doug.png', [body_top_left_x,body_top_left_y-100])
    while seconds<30:
        #clear screen
        DISPLAYSURF.fill(WHITE)
        counterLabel = myfont.render("SCORE: "+str(counter), 1, RED)
        DISPLAYSURF.blit(counterLabel, (5, 5))
        #redraw static images
        #body:
        DISPLAYSURF.blit(doug.image, doug.rect)
        #head
       	#tbc
        #left upper arm:
        #DISPLAYSURF.blit(leftbicep.image, leftbicep.rect)
        pygame.draw.line(DISPLAYSURF, BLACK, (left_should_x,left_should_y),(left_elbow_x,left_elbow_y),arm_thiccness)
        #lower left arm:
        pygame.draw.line(DISPLAYSURF, BLUE, (left_elbow_x, left_elbow_y),(left_hand_x,left_hand_y),arm_thiccness)
        #upper right arm:
        pygame.draw.line(DISPLAYSURF,BLACK, (right_should_x, right_should_y),(right_elbow_x,right_elbow_y),arm_thiccness)
        #lower right arm:
        pygame.draw.line(DISPLAYSURF, BLUE, (right_elbow_x, right_elbow_y),(right_hand_x,right_hand_y),arm_thiccness)

        left_elbow_x = arm_length*math.cos(left_shoulder_angle) + left_should_x
        left_elbow_y = arm_length*math.sin(left_shoulder_angle) + left_should_y
        left_hand_x = arm_length*math.cos(left_elbow_angle) + left_elbow_x
        left_hand_y = arm_length*math.sin(left_elbow_angle) + left_elbow_y
        right_elbow_x = arm_length*math.cos(right_shoulder_angle) + right_should_x
        right_elbow_y = arm_length*math.sin(right_shoulder_angle) + right_should_y
        right_hand_x = arm_length*math.cos(right_elbow_angle) + right_elbow_x
        right_hand_y = arm_length*math.sin(right_elbow_angle) + right_elbow_y

        if left_shoulder_angle > (math.pi*5)/2:
            left_shoulder_angle = math.pi/2

        if left_shoulder_angle < (math.pi*3)/2:
            left_shoulder_angle = max(math.pi/2,left_shoulder_angle-0.003)
        else:
            left_shoulder_angle = left_shoulder_angle+0.003

        if left_elbow_angle > (math.pi*5)/2:
            left_elbow_angle = math.pi/2
        
        if left_elbow_angle < (math.pi*3)/2:
            left_elbow_angle = max(math.pi/2,left_elbow_angle-0.003)
        else:
            left_elbow_angle +=0.003

        if right_shoulder_angle > (math.pi*5)/2:
            right_shoulder_angle = math.pi/2

        if right_shoulder_angle < (math.pi*3)/2:
            right_shoulder_angle = max(math.pi/2,right_shoulder_angle-0.003)
        else:
            right_shoulder_angle = right_shoulder_angle+0.003

        if right_elbow_angle > (math.pi*5)/2:
            right_elbow_angle = math.pi/2
        
        if right_elbow_angle < (math.pi*3)/2:
            right_elbow_angle = max(math.pi/2,right_elbow_angle-0.003)
        else:
            right_elbow_angle +=0.003

        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if seconds>29:
            game_over = True
        if seconds%3==0 and seconds not in foundNumbers:
            direction_of_dab = random_dab()
            foundNumbers.append(seconds)

        if direction_of_dab == "left":
            dab_label = myfont.render("LEFT DAB",1, RED)
            DISPLAYSURF.blit(dab_label, (300, 50))
        else:
            dab_label = myfont.render("RIGHT DAB",1, RED)
            DISPLAYSURF.blit(dab_label, (300, 50))

        timer_label = myfont.render("TIME REMAINING: "+str(30-seconds),1,RED)
        DISPLAYSURF.blit(timer_label, (screen_width-400,5))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    counter+=1
                    #raise left elbow
                    print "q pressed"
                    left_shoulder_angle = left_shoulder_angle+0.3
                elif event.key == K_w:
                    if left_shoulder_angle-0.3 < math.pi/2:
                        left_shoulder_angle += 2*math.pi - 0.3
                    else:
                        left_shoulder_angle = left_shoulder_angle - 0.3
                elif event.key == K_a:
                    left_elbow_angle = left_elbow_angle + 0.3
                elif event.key == K_s:
                    if left_elbow_angle-0.3 < math.pi/2:
                        left_elbow_angle += 2*math.pi - 0.3
                    else:
                        left_elbow_angle = left_elbow_angle - 0.3
                elif event.key == K_i:
                    right_shoulder_angle += 0.3
                elif event.key == K_o:
                    if right_shoulder_angle-0.3 < math.pi/2:
                        right_shoulder_angle += 2*math.pi - 0.3
                    else:
                        right_shoulder_angle = right_shoulder_angle - 0.3
                elif event.key == K_k:
                    right_elbow_angle = right_elbow_angle + 0.3
                elif event.key == K_l:
                    if right_elbow_angle-0.3 < math.pi/2:
                        right_elbow_angle += 2*math.pi - 0.3
                    else:
                        right_elbow_angle = right_elbow_angle - 0.3

        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if seconds%3==0 and seconds not in foundNumbers:
            direction_of_dab = random_dab()
            foundNumbers.append(seconds)

        if direction_of_dab == "left":
            dab_label = myfont.render("LEFT DAB",1, RED)
            DISPLAYSURF.blit(dab_label, (300, 50))
        else:
            dab_label = myfont.render("RIGHT DAB",1, RED)
            DISPLAYSURF.blit(dab_label, (300, 50))

        timer_label = myfont.render("TIME REMAINING: "+str(30-seconds),1,RED)
        DISPLAYSURF.blit(timer_label, (screen_width-400,5))

        pygame.display.update()
    return counter


while True:

	intro()
	num = main_game()
	outro(num)