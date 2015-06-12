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
lineProcess = False

# control variable for line points
prevx = prevy = mousex = mousey = -1
colours = list(menu.colours)
buttons = list(menu.buttons)



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
		
		#Menu Interaction
		if event.type == MOUSEBUTTONDOWN:
			#colours
			prevColour = colour
			for c in colours:
				if c.rect.collidepoint(event.pos):
					menu.update_colour(prevColour, c.rgb)
					colour = c.rgb
					break
			x, y = event.pos
			if x > con.MENURIGHT + .5 * (lineWidth + con.MENUBORDER):
				mouseDown = True
			#functional interaction		
			for button in buttons:
				if button.rect.collidepoint(event.pos):
					#new image
					if button.img == con.NEW:
						#first save it (coming soon)
						menu.new_image()
					# line width
					if button == menu.lineSlide:
						lineProcess = True
						prevx = button.coords[0]
			
			
		#toggle mouse button
		if event.type == MOUSEBUTTONUP:
			# for toggling line width
			if lineProcess:
				x, y = event.pos
				if x > con.LINESLIDERIGHT[0]:
					x = con.LINESLIDERIGHT[0]
				elif x < con.LINESLIDELEFT[0]:
					x = con.LINESLIDELEFT[0]
				y = con.LINESLIDELEFT[1]
				lineWidth = menu.update_lineslide(x, y, colour)
				lineProcess = False	
			# for drawing
			prevx = prevy = -1
			mouseDown = False
			
		#exit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				print "Goodbye."
				exit()
			
