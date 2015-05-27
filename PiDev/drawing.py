#!/usr/bin/python
# very first simple drawing test

import pygame, random
from pygame.locals import *

# random colour picker
def pick_colour():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r, g, b)
	
# instructions
print "ESC Key to exit, click to change colour."

# initialize screen
pygame.init()
screen = pygame.display.set_mode((1024, 592), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
pygame.display.flip()

# initilize with some colour
(r, g, b) = pick_colour()

# control variable for mouse
mouseDown = False

# control variable for line points
prevx = prevy = mousex = mousey = -1


# Pygame Loop
while True:
	for event in pygame.event.get():
		
		#drawing
		if event.type == MOUSEMOTION and mouseDown:
			if prevx == -1:
				prevx, prevy = event.pos
			else:
				mousex, mousey = event.pos
				pygame.draw.line(screen, (r, g, b), (prevx, prevy), (mousex, mousey), 1)
				(prevx, prevy) = (mousex, mousey)
				pygame.display.flip()
		
		#change of colour
		if event.type == MOUSEBUTTONDOWN:
			(r, g, b) = pick_colour()
			mouseDown = True
			
		#toggle mouse button
		if event.type == MOUSEBUTTONUP:
			prevx = prevy = -1
			mouseDown = False
			
		#exit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				print "Goodbye."
				exit()
			
