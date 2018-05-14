from os import path
from sys import exit, argv

MAX_X = 40
MAX_Y = 20

def display_map(map, code):
	"""
	Takes a list (map) of lists of integers describing 
	the 'contents' of the x and y coordinates, and displays
	the map value mapped from the code list (integer->char)
	"""
	print MAX_X*"="
	for row in map:
		print "|"
		for cell in row:
			print code[cell],
		print "|"
	return

def run(debug=True):
	print "You have started:\n", 
	print 10*'-', "Glowing Spoons", 10*'-'
	print "by Franco Quiroga \nWritten in python2"
	
	if debug:
		print "Currently, the debug option is Active"

	return

run()
