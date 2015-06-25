import constants as con
import pygame
from pygame.locals import *
import os, time, easygui, operator

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
firstSave = True
foldername = ""
templatefolder = None

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
	undo = button(con.UNDOCOORDS, con.ONUNDO)
	buttons.append(undo)
	redo = button(con.REDOCOORDS, con.ONREDO)
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
	
# just the procedure encapsulated
def delete_files_in_folder(folder):
	for f in os.listdir(folder):
		os.remove(folder + f)
	
# deleting undo and redo files, if present
def delete_temp_files():
	delete_files_in_folder(con.UNDO)
	delete_files_in_folder(con.REDO)
		
# paint the app interface
def initialise_app(withInit = True):
	if withInit:
		pygame.init()
		delete_temp_files()
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
	#elif newColourbutton == con.GREEN:
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
	update_sliders(newColour)
	pygame.display.flip()	
	
# clear drawing area
def new_image(save_toggle = True):
	if save_toggle:
		save_image()
	x = con.MENURIGHT + 0.7 * con.MENUBORDER
	pygame.draw.rect(screen, con.WHITE, (x, 0, con.SCREENWIDTH-x, con.SCREENHEIGHT))
	templatefolder = None
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

# to show whether undo and redo are an option
def update_undo_redo():
	global undo, redo, screen
	pygame.draw.rect(screen, con.MENUGRAY, undo.rect)
	pygame.draw.rect(screen, con.MENUGRAY, redo.rect)
	if len(os.listdir(con.UNDO)) > 0:
		undo.rect = draw_button(con.OFFUNDO, undo.coords)
	else: 
		undo.rect = draw_button(con.ONUNDO, undo.coords)
	if len(os.listdir(con.REDO)) > 0:
		redo.rect = draw_button(con.OFFREDO, redo.coords)
	else:
		redo.rect = draw_button(con.ONREDO, redo.coords)
	pygame.display.flip()
	
# get the correctly formatted timestamp for the local time	
def get_cur_timestamp():
	return time.strftime("%Y-%m-%d_%H:%M:%S")	

# get a sorted array of folder contents
def get_dir_content(filedir):
	contents = os.listdir(filedir)
	contents.sort()
	return contents	

# for not overwriting pictures	
def create_save_name():
	global firstSave, foldername, templatefolder
	if templatefolder: 
		return templatefolder + get_cur_timestamp() + ".png"
	if firstSave:
		dirs = os.listdir(con.PICS)
		if len(dirs) == 0:
			foldername = "1/"
		else:
			dirs.sort()
			foldername = str(int(dirs[-1])+1) + "/"
		os.makedirs(con.PICS + foldername)
	draw_menu_buttons()
	delete_temp_files()	
	firstSave = False
	return con.PICS + foldername + get_cur_timestamp() + ".png"

# getting the area that should be saved
def get_saving_area():
	global screen
	x = con.MENURIGHT + 0.8 * con.MENUBORDER
	rect = pygame.Rect(x, 0, con.SCREENWIDTH-x, con.SCREENHEIGHT)
	return screen.subsurface(rect)	

	
# saving an image
def save_image():
	pygame.image.save(get_saving_area(), create_save_name())
	
# returns a sorted number directory
def get_sorted_number_dir_contents(folder):
	dirs = os.listdir(folder)
	files = []
	numbers = {}
	for f in dirs:
		numbers[int(f.split(".")[0])] = f
	for num in sorted(numbers.keys()):
		files.append(numbers[num])
	return files

# for having stuff in order
def get_undo_counter():
	dirs = get_sorted_number_dir_contents(con.UNDO)
	if len(dirs) > 0: 
		if len(dirs) > con.MAXUNDO:
			os.remove(con.UNDO + dirs[0])
	else: 
		return con.UNDO + "1.png"
	return con.UNDO + str(int(dirs[-1].split(".")[0])+1) + ".png"
	
# for undo
def put_action_into_stack():
	delete_files_in_folder(con.REDO)
	pygame.image.save(get_saving_area(), get_undo_counter())
	update_undo_redo()
		
# actually undoing something
def undo_action():
	global screen
	undos = get_sorted_number_dir_contents(con.UNDO)
	if len(undos) > 1:
		os.rename(con.UNDO + undos[-1], con.REDO + undos[-1])
		img = pygame.image.load(con.UNDO + undos[-2])
		x = con.MENURIGHT + 0.7 * con.MENUBORDER
		screen.blit(img, (x,0))
		pygame.display.flip()
	elif len(undos) == 1:
		os.rename(con.UNDO + undos[-1], con.REDO + undos[-1])
		if undos[-1] == "1.png":
			new_image(False)
	update_undo_redo()
	
# for redos
def redo_action():
	global screen
	redos = get_sorted_number_dir_contents(con.REDO)
	if len(redos) > 0:
		img = pygame.image.load(con.REDO + redos[0])
		x = con.MENURIGHT + 0.7 * con.MENUBORDER
		screen.blit(img, (x,0))
		pygame.display.flip()
		os.rename(con.REDO + redos[0], con.UNDO + redos[0])
	update_undo_redo()
	
# for reworking from old images
def open_file():
	global screen, templatefolder
	pygame.display.set_mode((con.SCREENWIDTH, con.SCREENHEIGHT))
	file_path = easygui.fileopenbox(default=con.PICS)
	templatefolder = "/".join(file_path.split("/")[:-1]) + "/"
	screen = initialise_app(False)
	if file_path: 
		img = pygame.image.load(file_path)
		x = con.MENURIGHT + 0.7 * con.MENUBORDER
		screen.blit(img, (x,0))
		pygame.display.flip()
	else: 
		undos = get_sorted_number_dir_contents(con.UNDO)
		if len(undos) > 0:
			img = pygame.image.load(con.UNDO + undos[-1])
			x = con.MENURIGHT + 0.7 * con.MENUBORDER
			screen.blit(img, (x,0))
			pygame.display.flip()

