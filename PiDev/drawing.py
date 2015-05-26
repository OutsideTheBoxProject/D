#!/usr/bin/python
# very first simple drawing test

import pygame, random
from pygame.locals import *

# instructions
print "ESC Key to exit, click to change colour."

# initialize screen
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.display.flip()

# initilize with some colour
r = 150
g = 200
b = 50

# Pygame Loop
while True:
	for event in pygame.event.get():
		
		#drawing
		if event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			pygame.draw.circle(screen, (r, g, b), (mousex, mousey), 5, 0)
			pygame.display.flip()
		
		#change of colour
		if event.type == MOUSEBUTTONDOWN:
			r = random.randint(0, 255)
			g = random.randint(0, 255)
			b = random.randint(0, 255)
			
		#exit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				print "Goodbye."
				exit()
			
