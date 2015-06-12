import constants as con
import pygame
from pygame.locals import *
import random

colours = []
buttons = []
screen = None
new = None
group = None
undo = None
redo = None
eraser = None
save = None
#opacity = None
#opacitySlide = None
line = None
lineSlide = None

class colour:
	def __init__(self, irgb, icoords, ioff, ion):
		self.rgb = irgb
		self.coords = icoords
		self.off = ioff
		self.on = ion
		self.alpha = 100
		self.rect = None
		
class button:
	def __init__(self, icoords, iimg):
		self.coords = icoords
		self.img = iimg
		self.rect = None
		

# initialising all colours		
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
	
# setup non colour related buttons
def setup_buttons():
	global buttons, new, group, undo, redo, eraser, save, opacity, opacitySlide, line, lineSlide
	new = button(con.NEWCOORDS, con.NEW)
	buttons.append(new)
	group = button(con.GROUPCOORDS, con.GROUP)
	buttons.append(group)
	undo = button(con.UNDOCOORDS, con.OFFUNDO)
	buttons.append(undo)
	redo = button(con.REDOCOORDS, con.OFFREDO)
	buttons.append(redo)
	eraser = button(con.ERASERCOORDS, con.ERASER)
	buttons.append(eraser)
	save = button(con.SAVECOORDS, con.SAVE)
	buttons.append(save)
	#opacity = button(con.OPACITYCOORDS, con.OPACBLACK)
	#buttons.append(opacity)
	#opacitySlide = button(con.OPACITYSLIDELEFT, con.WHITEOFF)
	#buttons.append(opacitySlide)
	line = button(con.LINECOORDS, con.LINEBLACK)
	buttons.append(line)
	lineSlide = button(con.LINESLIDEMIDDLE, con.WHITEOFF)
	buttons.append(lineSlide)
		
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
	return buttonRect

# draws all menu buttons
def draw_menu_buttons():
	global colours, buttons
	# buttons
	setup_buttons()
	for button in buttons:
		button.rect = draw_button(button.img, button.coords)
	# colours
	setup_colours()
	for colour in colours:
		if not colour.rgb == con.BLACK:
			colour.rect = draw_button(colour.off, colour.coords)
		else:
			colour.rect = draw_button(colour.on, colour.coords)


# colour update for opacity slider
#def update_opacity_slider(newColour):
	#pygame.draw.rect(screen, con.MENUGRAY, opacity.rect)
	#pygame.draw.rect(screen, con.MENUGRAY, opacitySlide.rect)
	#if newColour == con.RED:
		#opacity.rect = draw_button(con.OPACRED, opacity.coords)
	#elif newColour == con.PURPLE:
		#opacity.rect = draw_button(con.OPACPURPLE, opacity.coords)
	#elif newColour == con.ORANGE:
		#opacity.rect = draw_button(con.OPACORANGE, opacity.coords)
	#elif newColour == con.PINK:
		#opacity.rect = draw_button(con.OPACPINK, opacity.coords)
	#elif newColour == con.DARKGREEN:
		#opacity.rect = draw_button(con.OPACDARKGREEN, opacity.coords)
	#elif newColour == con.GREEN:
		#opacity.rect = draw_button(con.OPACGREEN, opacity.coords)
	#elif newColour == con.CORNFLOWER:
		#opacity.rect = draw_button(con.OPACCORNFLOWER, opacity.coords)
	#elif newColour == con.DARKBLUE:
		#opacity.rect = draw_button(con.OPACDARKBLUE, opacity.coords)
	#elif newColour == con.BLACK:
		#opacity.rect = draw_button(con.OPACBLACK, opacity.coords)
	#elif newColour == con.GRAY:
		#opacity.rect = draw_button(con.OPACGRAY, opacity.coords)
	#elif newColour == con.WHITE:
		#opacity.rect = draw_button(con.OPACWHITE, opacity.coords)
	#elif newColour == con.BEIGE:
		#opacity.rect = draw_button(con.OPACBEIGE, opacity.coords)
	#opacitySlide.rect = draw_button(opacitySlide.img, opacitySlide.coords)

	
# colour update for line slider
def update_line_slider(newColour):
	pygame.draw.rect(screen, con.MENUGRAY, line.rect)
	pygame.draw.rect(screen, con.MENUGRAY, lineSlide.rect)
	if newColour == con.RED:
		line.rect = draw_button(con.LINERED, line.coords)
	elif newColour == con.PURPLE:
		line.rect = draw_button(con.LINEPURPLE, line.coords)
	elif newColour == con.ORANGE:
		line.rect = draw_button(con.LINEORANGE, line.coords)
	elif newColour == con.PINK:
		line.rect = draw_button(con.LINEPINK, line.coords)
	elif newColour == con.DARKGREEN:
		line.rect = draw_button(con.LINEDARKGREEN, line.coords)
	elif newColour == con.GREEN:
		line.rect = draw_button(con.LINEGREEN, line.coords)
	elif newColour == con.CORNFLOWER:
		line.rect = draw_button(con.LINECORNFLOWER, line.coords)
	elif newColour == con.DARKBLUE:
		line.rect = draw_button(con.LINEDARKBLUE, line.coords)
	elif newColour == con.BLACK:
		line.rect = draw_button(con.LINEBLACK, line.coords)
	elif newColour == con.GRAY:
		line.rect = draw_button(con.LINEGRAY, line.coords)
	elif newColour == con.WHITE:
		line.rect = draw_button(con.LINEWHITE, line.coords)
	elif newColour == con.BEIGE:
		line.rect = draw_button(con.LINEBEIGE, line.coords)
	lineSlide.rect = draw_button(lineSlide.img, lineSlide.coords)	


# updates the sliders according to colour
def update_sliders(newColour):
	#update_opacity_slider(newColour)
	update_line_slider(newColour)

# get a new colour and update the responding images
def update_colour(prev, newColour):
	global colours, screen
	for c in colours:
		if c.rgb == prev:
			pygame.draw.rect(screen, con.MENUGRAY, c.rect)
			c.rect = draw_button(c.off, c.coords)
		if c.rgb == newColour:
			c.rect = draw_button(c.on, c.coords)
			update_sliders(c.rgb)
			
	pygame.display.flip()	
	
# clear drawing area
def new_image():
	x = con.MENURIGHT + 0.7 * con.MENUBORDER
	pygame.draw.rect(screen, con.WHITE, (x, 0, con.SCREENWIDTH-x, con.SCREENHEIGHT))
	pygame.display.flip()

# imaging interaction
def update_lineslide(x, y, colour):
	lineSlide.coords = (x, y)
	update_line_slider(colour)
	pygame.display.flip()
	return 51 - int((x-8)/4.5) 
	
# imaging opacity interaction
#def update_opacslide(x, y, colour):
	#opacitySlide.coords = (x,y)
	#update_opacity_slider(colour)
	#pygame.display.flip()
	#return 100 - int((x-8)/2.2)
