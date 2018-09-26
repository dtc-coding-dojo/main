"""
This is where I put my program description. What goes in what goes out. How to use it on the command line and so on. Also probably you should state your name and where to email you with comments
"""
from __future__ import division
import sys
import argparse
import pandas as pd

# NEVER DO THIS
from numpy import *

#Always do this
from math import pi, ceil


"______________FUNCTION BODY___________________"


def get_dict_from_file( filename):
	# Describe what your function does here

	dict_file_line = {}
	
	# dont do this
	try:
		file = open( filename)
	except:
		print "this is not a string"


	# do this
	if type( filename) is str:
	
		with open( filename) as inf:	
			print "here is your file with the name {}".format( filename)		
			
			for i, line in enumerate( inf):
				dict_file_line[ i] = line
		
		with open( "output.txt", "w+") as outf:
			for key, item in dict_file_line.iteritems():
				outf.write( "{}\t{}\n".format( key, item) )

		return dict_file_line
	
	else:
		print "this is not a string I dont know what to do with this"
		return None






"""_________HERE COMES THE MAIN FUNCTION__________"""


if __name__ == "__main__":
	# We are going to read in a file and print the contents

	# kinda bad
	#string_filename = "example_file.txt"
	
	# kinda good
	#string_filename = sys.argv[1]

	# Best
	parser = argparse.ArgumentParser( description = 'This is the best way to read in stuff from the command line')
	parser.add_argument( '-f', type = str, help='this is your file')
	parser.add_argument( '-i', type = int, help='this is a number')
	parser.add_argument( '-flag',  action='store_true', help='this is a flag')
	args = parser.parse_args()

	string_filename = args.f

	dict_file_line = get_dict_from_file( string_filename)

	
	# Now lets do some list tricks	
	short_list = [ "", 4, 5, 10, 23, 84]

	short_list = filter( None, short_list)
	
	squares = []

	for i in short_list:
		square = i**2
		print square
		#short_list.append( i) #NEVER CHANGE A LIST YOURE ITERATING OVER

		squares.append( square)

	
	# Pretty good
	short_string_list = [ str(x) for x in short_list]
	
	# Amazing
	short_string_list = map(str, short_string_list)


	short_string_list_numbers_over_5 = [ str(x) for x in short_list if x > 5]

	print short_string_list_numbers_over_5

	
        
	



	


