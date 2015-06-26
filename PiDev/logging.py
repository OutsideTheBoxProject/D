import constants as con
import os, time

# this is just a collection of logging functions in order to have them
# not clogging the main file
# most of them are only used during evaluation anyway 

# append a single line at the end of a text file
def append_line(filename, line):
	with open(filename, "a") as f:
		f.write(line + "\n")

# get the contents of a file as an array of lines
def get_lines(filename):
	with open(filename) as f:
		return f.readlines()
			
# get the correctly formatted timestamp for the local time	
def get_cur_timestamp():
	return time.strftime("%Y-%m-%d %H:%M:%S")

# returns the correctly formatted timestamp for the day
def get_date_timestamp():
	return time.strftime("%Y-%m-%d")
	
# formats the info with timestamp and delimiter
def get_line(info, detail=""):
	line = []
	line.append(get_cur_timestamp())
	line.append(info)
	line.append(detail)
	return ",".join(line)
	
# default logging because I'm getting lazy
def log(msg, detail=""):
	append_line(con.LOG, get_line(msg, detail))

# logging station starting
def log_start_application():
	log("starting application")
	
# logging new file
def log_new_file():
	log("starting new drawing")
	
# opening a file
def log_open_file(filepath):
	log("opening file", filepath)
	
# undo
def log_undo():
	log("undo")
	
# redo
def log_redo():
	log("redo")
	
# eraser
def log_erasing(): 
	log("started erasing")
	
# stopping to erase
def log_stopped_erasing():
	log("finished erasing")
	
# line width
def log_linewidth(lineWidth):
	log("changed lineWidth", str(lineWidth))
	
# colour change
def log_colour(rgb):
	log("changed colour", str(rgb))
	
# changing to animation mode
def log_animation():
	log("started animation")

# changing to drawing mode
def log_drawing():
	log("started drawing")

# log opening a new folder in animation
def log_new_animation(folder): 
	log("started new animation", folder)
	
# log accelerator data and waittime
def log_waittime(acc, waittime):
	log("acceleration at", str(acc))
	log("waittime at", str(waittime))
	
# saving an image
def log_save_image(where):
	log("saved image", where)



