import constants as con
import pygame
from pygame.locals import *
import random

colours = []
buttons = {}
screen = None

class colour:
	def __init__(self, irgb, icoords, ioff, ion):
		self.rgb = irgb
		self.coords = icoords
		self.off = ioff
		self.on = ion
		self.rect = None
		
def setup_colours():
	global colours
	red = colour(con.RED, con.REDCOORDS, con.REDOFF, con.REDON)
	colours.append(red)
	purple = colour(con.PURPLE, con.PURPLECOORDS, con.PURPLEOFF, con.PURPLEON)
	colours.append(purple)
	orange = colour(con.ORANGE, con.ORANGECOORDS, con.ORANGEOFF, con.ORANGEON)
	colours.append(orange)
	pink = colour(con.PINK, con.PINKCOORDS, con.PINKOFF, con.PINKON)
	colours.append(pink)
	darkGreen = colour(con.DARKGREEN, con.DARKGREENCOORDS, con.DARKGREENOFF, con.DARKGREENON)
	colours.append(darkGreen)
	green = colour(con.GREEN, con.GREENCOORDS, con.GREENOFF, con.GREENON)
	colours.append(green)
	cornflower = colour(con.CORNFLOWER, con.CORNFLOWERCOORDS, con.CORNFLOWEROFF, con.CORNFLOWERON)
	colours.append(cornflower)
	darkBlue = colour(con.DARKBLUE, con.DARKBLUECOORDS, con.DARKBLUEOFF, con.DARKBLUEON)
	colours.append(darkBlue)
	black = colour(con.BLACK, con.BLACKCOORDS, con.BLACKOFF, con.BLACKON)
	colours.append(black)
	gray = colour(con.GRAY, con.GRAYCOORDS, con.GRAYOFF, con.GRAYON)
	colours.append(gray)
	white = colour(con.WHITE, con.WHITECOORDS, con.WHITEOFF, con.WHITEON)
	colours.append(white)
	beige = colour(con.BEIGE, con.BEIGECOORDS, con.BEIGEOFF, con.BEIGEON)
	colours.append(beige)
		
# paint the app interface
def initialise_app():
	pygame.init()
	screen = draw_screen()
	draw_menu_buttons()
	pygame.display.flip()
	return screen

#initialises the basic screen setup
def draw_screen():
	global screen
	screen = pygame.display.set_mode((con.SCREENWIDTH, con.SCREENHEIGHT), pygame.FULLSCREEN)
	screen.fill((con.WHITE))
	# draw menu area left
	pygame.draw.line(screen, (200,200,200), (con.MENURIGHT, 0), (con.MENURIGHT,con.SCREENHEIGHT), con.MENUBORDER)
	pygame.draw.rect(screen, con.MENUGRAY, ((0,0), (con.MENURIGHT, con.SCREENHEIGHT)))
	return screen

# colour picker for random colours
def pick_colour():
	r = random.randint(0, 255)
	g = random.randint(0, 255)	
	b = random.randint(0, 255)
	return (r, g, b)


# draw a button on the right position with the right picture
def draw_button(image, coords):
	global screen
	button = pygame.image.load(image)
	buttonRect = button.get_rect()
	buttonRect.x = coords[0]
	buttonRect.y = coords[1]
	screen.blit(button, buttonRect)
	return button, buttonRect

# draws all menu buttons
def draw_menu_buttons():
	global colours, buttons
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
	setup_colours()
	for colour in colours:
		if not colour.rgb == con.BLACK:
			temp, colour.rect = draw_button(colour.off, colour.coords)
		else:
			temp, colour.rect = draw_button(colour.on, colour.coords)
	buttons = {new:newRect, group:groupRect, undo:undoRect, redo:redoRect, eraser:eraserRect, save:saveRect, opacity:opacityRect, opacitySlide:opacitySlideRect, line:lineRect, lineSlide:lineSlideRect}


#get a new colour and update the responding images
def update_colour(prev, newColour):
	global colours, screen
	for c in colours:
		if c.rgb == prev:
			pygame.draw.rect(screen, con.MENUGRAY, c.rect)
			temp, c.rect = draw_button(c.off, c.coords)
		if c.rgb == newColour:
			temp, c.rect = draw_button(c.on, c.coords)
	pygame.display.flip()		
	
