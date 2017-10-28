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
DISPLAYSURF = pygame.display.set_mode((800,600) ,0,24)
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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()