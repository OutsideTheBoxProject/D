import drawing as draw
import sys
import constants as con

sys.stdout = open(con.STDOUT, 'a')
sys.stderr = open(con.STDOUT, 'a')

draw.draw_mode()
