import menuHandler as menu
import constants as con
import easygui
import pygame
import cwiid

pictures = []
currentIndex = -1
running = 0
waittime = con.BASEWAIT
wm = None

# just get the array of pictures according to path for a directory
def get_pictures_from_dir(directory): 
	pics = menu.get_dir_content(directory)
	returnpics = []
	for pic in pics:
		returnpics.append(directory + pic)
	return returnpics

# default starting setup for pictures - always show the most recent folder
def initialise_pictures(): 
	global pictures
	menu.setup_animation()
	picDirs = menu.get_sorted_number_dir_contents(con.PICS)
	picDir = picDirs[-1]
	pictures = get_pictures_from_dir(con.PICS + picDir + "/")

# looking for wiimote
def check_for_wiimote(): 
	global wm
	try: 
		wm = cwiid.Wiimote()
	except RuntimeError: 
		print "Error opening wiimote connection"
	if not wm == None:
		wm.rpt_mode = cwiid.RPT_ACC
		wm.led = 1
	

# updating the waittime
def update_waittime(): 
	global wm, waittime
	if wm == None: 
		check_for_wiimote()
	else: 
		fullacc = 0
		for element in wm.state['acc']:
			if element > 220:
				fullacc = con.BASEWAIT
				break
			fullacc = fullacc + element
		waittime = con.BASEWAIT - fullacc*7

# choosing the next picture
def next_pic():
	global pictures, currentIndex
	currentIndex = currentIndex + 1
	if currentIndex > (len(pictures) - 1):
		currentIndex = 0
	return pictures[currentIndex]
	
# reset picture folder for animation
def set_pictures():
	global pictures
	pygame.display.set_mode((con.SCREENWIDTH, con.SCREENHEIGHT))
	file_path = easygui.fileopenbox(default=con.PICS)
	picDir = "/".join(file_path.split("/")[:-1]) + "/"
	pictures = get_pictures_from_dir(picDir)
	menu.setup_animation()
