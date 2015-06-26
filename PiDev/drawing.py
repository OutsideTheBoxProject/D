#!/usr/bin/python
# very first simple drawing test

import pygame
import constants as con
import menuHandler as menu
from pygame.locals import *
import animate as anim 


# put it all in a function, so that it is callable for later

def draw_mode():
	# global variables 
	lineWidth = 25
	#alpha = 100
	colour = con.BLACK
	
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
		if menu.animating and (anim.running == 0 or (pygame.time.get_ticks() - anim.running) > anim.waittime):
			screen.blit(pygame.image.load(anim.next_pic()), (con.MENURIGHT + 0.8 * con.MENUBORDER, 0))
			pygame.display.flip()
			anim.running = pygame.time.get_ticks()
			anim.update_waittime()
		
		for event in pygame.event.get():
			#drawing
			if event.type == MOUSEMOTION and mouseDown and not menu.animating:
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
				if menu.animating:
					if menu.animdraw.rect.collidepoint(event.pos):
						menu.setup_drawing()
					if menu.animload.rect.collidepoint(event.pos):
						anim.set_pictures()
				else: 
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
									menu.update_colour(colour, con.WHITE)
									colour = con.WHITE
									erasing = True
								else:
									lineWidth = prevLineWidth
									menu.update_colour(colour, prevColour)
									colour = prevColour
									erasing = False
							#saving
							if button == menu.save:
								menu.save_image()
							#undo
							if button == menu.undo:
								menu.undo_action()
							#redo
							if button == menu.redo:
								menu.redo_action()
							#load file
							if button == menu.group:
								menu.open_file()
							#animation mode
							if button == menu.animate:
								anim.initialise_pictures()
						
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
				if drawing:
					menu.put_action_into_stack()
					drawing = False
			
			#exit
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					print "Goodbye."
					exit()
