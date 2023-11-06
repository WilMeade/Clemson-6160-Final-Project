# -*- coding: utf-8 -*-

import pygame
import player
#import enemy
#import coin

pygame.init()

screen_width    = 800
screen_height   = 500
posx = 10
posy = 10
FPS = 60

SKY = [50, 100 , 255]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("6160 Game")
enemy = pygame.image.load("enemy.png").convert_alpha()
coin = pygame.image.load("coin.png").convert_alpha()

#set up refresh rate
clock = pygame.time.Clock()

#character position
player = player.Character((posx, posy))

#game loop boolean
game_over = False

#define game variables
scroll = 0

#draw ground image
ground_image = pygame.image.load("ground.png").convert_alpha()
width = ground_image.get_rect().width
height = ground_image.get_rect().height
ground_image = pygame.transform.scale(ground_image, (int(width*0.5), int(height*0.5)))

#files = ["IMG_0.png", "IMG_1.png", "IMG_2.png", "IMG_3.png"]
#sky = pygame.image.load(files[0]).convert_alpha()

#load images
bg_images = []

#load image sequences
#for i in range(1,4):
	#bg_image = pygame.image.load(files[i]).convert_alpha()
	#bg_images.append(bg_image)

#draw background images 

#def draw_bg(scroll):
#	speed = 1
#	posx = 0 - (scroll*speed)
#	posy = 90
#	for x in range(len(bg_images)):
#		screen.blit(bg_images[x],(posx,posy))
#		posx = 0 - (scroll*speed)
#		posy += 60
#		speed += 2

while game_over == False:
	clock.tick(FPS)


	for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            game_over = True
	player.handle_event(event)
	#screen.blit(sky, (0,0))
	#draw_bg(scroll)
	screen.blit(ground_image, (0,0))
	
	#input data. Left and right keys to create the parallax effect
	key = pygame.key.get_pressed()	
	if key[pygame.K_LEFT]and scroll>0:
		scroll -=5
		#draw_bg(scroll)
		screen.blit(ground_image, (0,0))

	if key[pygame.K_RIGHT]and scroll<100:
		scroll +=5
		#draw_bg(scroll)
		screen.blit(ground_image, (0,0))
	
	screen.blit(player.image,(100,300))
	screen.blit(enemy,(200,300))
	screen.blit(coin,(300,300))
	
	pygame.display.flip()
	clock.tick(20)

pygame.quit ()

