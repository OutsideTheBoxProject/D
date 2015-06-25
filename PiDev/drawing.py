#!/usr/bin/python
# very first simple drawing test

import pygame
import constants as con
import menuHandler as menu
from pygame.locals import *

# global variables 
lineWidth = 25
#alpha = 100
colour = con.BLACK

	
# instructions
print "ESC Key to exit, click to change colour."

# initialize the app
screen = menu.initialise_app()

# control variable for mouse
mouseDown = False
lineProcess = False
#opacProcess = False
erasing = False
drawing = False

# control variable for line points
prevx = prevy = mousex = mousey = -1
colours = list(menu.colours)
buttons = list(menu.buttons)
prevLineWidth = lineWidth
prevColour = colour



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
				# pygame.draw.line(screen, colour, (prevx, prevy), (mousex, mousey), lineWidth)
				pygame.draw.circle(screen, colour, (int(mousex), int(mousey)), int(lineWidth/2))
				(prevx, prevy) = (mousex, mousey)
				drawing = True
				pygame.display.flip()
		
		#Menu Interaction
		if event.type == MOUSEBUTTONDOWN:
			#colours
			for c in colours:
				if c.rect.collidepoint(event.pos):
					menu.update_colour(colour, c.rgb)
					colour = c.rgb
					if erasing:
						linewidth = prevLineWidth
						erasing = False
					break
			x, y = event.pos
			if x > con.MENURIGHT + .5 * (lineWidth + con.MENUBORDER):
				mouseDown = True
			#functional interaction		
			for button in buttons:
				if button.rect.collidepoint(event.pos):
					#new image
					if button.img == con.NEW:
						menu.new_image()
					# line width
					if button == menu.lineSlide:
						lineProcess = True
					# opacity
					#if button == menu.opacitySlide:
						#opacProcess = True
					if button == menu.eraser:
						if not erasing:
							prevLineWidth = lineWidth
							prevColour = colour
							lineWidth = 100
							colour = con.WHITE
							erasing = True
						else:
							print "erasing"
							lineWidth = prevLineWidth
							colour = prevColour
							erasing = False
					#saving
					if button == menu.save:
						menu.save_image()
						
						
			
			
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
			# for toggling opacity
			#if opacProcess:
				#x, y = event.pos
				#if x > con.OPACITYSLIDERIGHT[0]:
					#x = con.OPACITYSLIDERIGHT[0]
				#elif x < con.OPACITYSLIDELEFT[0]:
					#x = con.OPACITYSLIDELEFT[0]
				#y = con.OPACITYSLIDELEFT[1]
				#alpha = menu.update_opacslide(x, y, colour)
				#opacProcess = False
			# for drawing
			prevx = prevy = -1
			mouseDown = False
			
		#exit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				print "Goodbye."
				exit()
			
