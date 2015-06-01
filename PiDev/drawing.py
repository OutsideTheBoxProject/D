#!/usr/bin/python
# very first simple drawing test

import pygame, random
import constants as con
from pygame.locals import *

# global variables 
lineWidth = 10

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
screen = pygame.display.set_mode((con.SCREENWIDTH, con.SCREENHEIGHT), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
# draw menu area left
pygame.draw.line(screen, (200, 200, 200), (con.MENURIGHT, 0), (con.MENURIGHT,con.SCREENHEIGHT), con.MENUBORDER)
pygame.draw.rect(screen, (232, 232, 232), ((0,0), (con.MENURIGHT, con.SCREENHEIGHT)))
# draw buttons
screen.blit(pygame.image.load(con.NEW), (36,8))
screen.blit(pygame.image.load(con.GROUP), (130,8))
screen.blit(pygame.image.load(con.OFFUNDO), (28,98))
screen.blit(pygame.image.load(con.OFFREDO), (130,98))
screen.blit(pygame.image.load(con.ERASER), (28,158))
screen.blit(pygame.image.load(con.SAVE), (130,184))
# opacity slider
screen.blit(pygame.image.load(con.OPACBLACK), (10,263))
screen.blit(pygame.image.load(con.WHITEOFF), (95,253))

# show it on the display
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
				if not (prevx > con.MENURIGHT + .5 * (lineWidth + con.MENUBORDER)):
					prevx = con.MENURIGHT + .5 * (lineWidth + con.MENUBORDER)
				if not (mousex > con.MENURIGHT + .5 * (lineWidth + con.MENUBORDER)):
					mousex = con.MENURIGHT + .5 * (lineWidth + con.MENUBORDER)
				pygame.draw.line(screen, (r, g, b), (prevx, prevy), (mousex, mousey), lineWidth)
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
			
