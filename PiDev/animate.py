import menuHandler as menu
import constants as con

pictures = []
currentIndex = -1
running = 0
waittime = 3000

# default starting setup for pictures - always show the most recent folder
def initialise_pictures(): 
	global pictures
	menu.setup_animation()
	picDirs = menu.get_sorted_number_dir_contents(con.PICS)
	picDir = picDirs[-1]
	pics = menu.get_dir_content(con.PICS + picDir)
	for pic in pics:
		pictures.append(con.PICS + picDir + "/" + pic)

# choosing the next picture
def next_pic():
	global pictures, currentIndex
	currentIndex = currentIndex + 1
	if currentIndex > (len(pictures) - 1):
		currentIndex = 0
	return pictures[currentIndex]
