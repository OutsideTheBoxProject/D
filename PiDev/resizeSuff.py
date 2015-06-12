# global imports
import PIL
from PIL import Image
import sys
import os

# local imports
import constants as con


# main function
def resize_images(filedir):
	files = os.listdir(filedir)
	for f in files:
		if ".png" in f:
			print "dealing with " + filedir + f
			img = Image.open(filedir + f)
			# hpercent = (.8 * float(img.size[1])/float(img.size[1]))
			# wsize = int((float(img.size[0]) * float(hpercent)))
			img = img.resize((int(img.size[0]), int(.8 * float(img.size[1])) ), PIL.Image.ANTIALIAS)
			img.save(con.TESTGRAPHICS + f)
	print "done."
		
	

# main call
resize_images(con.GRAPHICS)
