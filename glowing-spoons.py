from os import path
from sys import exit, argv

def run(debug=True):
	print "You have started:\n", 
	print 10*'*', "Glowing Spoons", 10*'*'
	print "by Franco Quiroga \nWritten in python2"
	
	if debug:
		print "Currently, the debug option is Active"

	engine = Engine(debug)

	return

class Engine(object):

	def __init__(self, debug, tiles=False):
		self.options = {
		'debug': debug,
		}

		self.characters = {}
		pass

	def refresh(self):
		pass

run()
