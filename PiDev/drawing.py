#!/usr/bin/python
# very first simple drawing test

import pygame
import constants as con
import menuHandler as menu
from pygame.locals import *

# global variables 
lineWidth = 10
colour = con.BLACK
	
# instructions
print "ESC Key to exit, click to change colour."

# initialize the app
screen = menu.initialise_app()

# control variable for mouse
mouseDown = False

# control variable for line points
prevx = prevy = mousex = mousey = -1
colours = list(menu.colours)


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
				pygame.draw.line(screen, colour, (prevx, prevy), (mousex, mousey), lineWidth)
				(prevx, prevy) = (mousex, mousey)
				pygame.display.flip()
		
		#change of colour
		if event.type == MOUSEBUTTONDOWN:
			prevColour = colour
			for c in colours:
				if c.rect.collidepoint(event.pos):
					menu.update_colour(prevColour, c.rgb)
					colour = c.rgb
					break
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
			
