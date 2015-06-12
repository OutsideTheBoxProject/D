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

# draw a button on the right position with the right picture
def draw_button(image, coords):
	global screen
	button = pygame.image.load(image)
	buttonRect = button.get_rect()
	buttonRect.x = coords[0]
	buttonRect.y = coords[1]
	screen.blit(button, buttonRect)
	return button, buttonRect
	
	
# draw buttons
new, newRect = draw_button(con.NEW, con.NEWCOORDS)
group, groupRect = draw_button(con.GROUP, con.GROUPCOORDS) 
undo, undoRect = draw_button(con.OFFUNDO, con.UNDOCOORDS)
redo, redoRect = draw_button(con.OFFREDO, con.REDOCOORDS) 
eraser, eraserRect = draw_button(con.ERASER, con.ERASERCOORDS)
save, saveRect = draw_button(con.SAVE, con.SAVECOORDS)
# opacity slider
opacity, opacityRect = draw_button(con.OPACBLACK, con.OPACITYCOORDS)
opacitySlide, opacitySlideRect = draw_button(con.WHITEOFF, con.OPACITYSLIDEMIDDLE)
# line thickness slider
line, lineRect = draw_button(con.LINEBLACK, con.LINECOORDS)
lineSlide, lineSlideRect = draw_button(con.WHITEOFF, con.LINESLIDEMIDDLE)
# colours
red, redRect = draw_button(con.REDOFF, con.REDCOORDS)
purple, purpleRect = draw_button(con.PURPLEOFF, con.PURPLECOORDS)
orange, orangeRect = draw_button(con.ORANGEOFF, con.ORANGECOORDS) 
pink, pinkRect = draw_button(con.PINKOFF, con.PINKCOORDS) 
darkGreen, darkGreenRect = draw_button(con.DARKGREENOFF, con.DARKGREENCOORDS)
green, greenRect = draw_button(con.GREENOFF, con.GREENCOORDS)
cornflower, cornflowerRect = draw_button(con.CORNFLOWEROFF, con.CORNFLOWERCOORDS)
darkBlue, darkBlueRect = draw_button(con.DARKBLUEOFF, con.DARKBLUECOORDS) 
black, blackRect = draw_button(con.BLACKON, con.BLACKCOORDS)
gray, grayRect = draw_button(con.GRAYOFF, con.GRAYCOORDS)
white, whiteRect = draw_button(con.WHITEOFF, con.WHITECOORDS)
beige, beigeRect = draw_button(con.BEIGEOFF, con.BEIGECOORDS)
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
			x,y = event.pos

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
			
