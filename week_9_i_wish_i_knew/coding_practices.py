"""
This is where I put my program description. What goes in what goes out. How to use it on the command line and so on. Also probably you should state your name and where to email you with comments

This program is organised in a function body and a main function which is the advanced way to code in Python. The compartmental nature of the script makes it easier to add functions from other programs or export functions to different programs. The caveat is, that you can't read your script from top to bottom to figure out the succession of commands. You will need to start at the main function and then check what each function does individually
"""

# Here we're going to import some whole libraries
from __future__ import division # So python 2 has this annoying habit of spitting out integers when dividing two integers. For example 1 / 2 will result in 1 because it was rounded up. We combat this by importing the division module from python 3 where this was fixed. That's why it is called future. This import has to go on top
import sys
import argparse
import pandas as pd # This will import pandas with the abbreveation pd which makes it quicker to note down

# NEVER DO THIS. You will import a lot of functions buy you won't know where they come from. This is called namespace pollution and is considered bad practice
from numpy import *

#Always do this. This is what you should do instead if you want to import singular functions from a library
from math import pi, ceil


"______________FUNCTION BODY___________________"  # Ok here is where we define all the different functions in our program. If our script is a machine the functions are the cogs that fit neatly into each other to make everything run smoothly


def get_dict_from_file( filename): # Make your function name as descriptive as possible. Here we want to define a function that reads in a dictionary from a file
 	# Describe what your function does here

	dict_file_line = {} # Note the spacing before and after the equal sign this makes code easier to navigate. I do the same for paranthesis
	
	# Ok lets see if the input is actually a string so we can read it in. Its good practice to check whether you have the desired input at first

	try: # dont do this. This will try to do something and if it returns an error will continue to do the except statement. However this might make error handling impossible and will result in much confusion

		inf = open( filename) # this is the simple way of opening files you will see a better way down below
	except:
		print "this is not a string"


	
	if type( filename) is str: # do this instead where you check the type of you input
	
		with open( filename) as inf: # This is an advanced way of reading in files. The indentation marks actions that should be performed while the file is open
			print "here is your file with the name {}".format( filename) # This is a cool way to format strings. No need to convert numbers, objects etc into strings simply mark the space with {} and put it in between the paranthesis and it will incorporate it into the string		
			
			for i, line in enumerate( inf): # This is a cool way to loop through something but count at the same time. i of the first item will correspond to 0, i of the second item to 1 etc. Here we loop through lines of the file and count them at the same time. By looping through the file line by line we avoid reading the whole file into memory
				dict_file_line[ i] = line # make a dictionary where the line number is stored as key and the line itself as a value
		
		with open( "output.txt", "w+") as outf:  # Here we open an output file. w+ tells python to create the file if it didnt exist before
			for key, item in dict_file_line.iteritems(): # With iteritems you can loop through the keys and values of a dictionary at the same time
				outf.write( "{}\t{}\n".format( key, item) ) # Write the line count and the line into the output file. Seperate them by a tab and put a newline at the end

		return dict_file_line # This is what the function spits out
	
	else:
		print "this is not a string I dont know what to do with this"
		return None # return the function empty handed






"""_________HERE COMES THE MAIN FUNCTION__________"""  # Ok this is where we define the main function which is actually where the code starts


if __name__ == "__main__":
	# We are going to read in a file and print the contents

	# kinda bad. Specify the file you want to read into the code. That makes it very tedious to modify if you want to read in different files
	#string_filename = "example_file.txt"
	
	# kinda good. Instead read the file from the command line
	#string_filename = sys.argv[1]

	# Best. This is the professional way where you read in input from the command line using different flags. So the file to read in is preceded by a -f. This way you can specify help messages for the user and also what type the file should be. Python will complain if the wrong input is written. Don't forget to import argparse in the beginning
	parser = argparse.ArgumentParser( description = 'This is the best way to read in stuff from the command line') # here you put a little help message to print when you type -h after your program
	parser.add_argument( '-f', type = str, help='this is your file')
	parser.add_argument( '-i', type = int, help='this is a number')
	parser.add_argument( '-flag',  action='store_true', help='this is a flag')
	args = parser.parse_args()
	string_filename = args.f # no need to understand this just copy this block of code into your script if you want to use it

	dict_file_line = get_dict_from_file( string_filename) # Now use the function above to read out the file and print it back into an output file

	
	# Now lets do some list tricks just on the side
	short_list = [ "", 4, 5, 10, 23, 84] # just some regular list

	short_list = filter( None, short_list) # this way we can quickly filter out empty entries like the first "".
	
	squares = []

	for i in short_list:
		square = i**2
		print square
		#short_list.append( i) #NEVER CHANGE A LIST YOURE ITERATING OVER. This can lead to majour problems down the line. This line for example leads the program to run infinitely

		squares.append( square) # instead open a second list and put in there

	
	# Pretty good. This is called a list comprehension where you do a for loop in one line which is really quick. Here we turn all the numbers into strings
	short_string_list = [ str(x) for x in short_list]
	
	# Amazing
	short_string_list = map(str, short_string_list) # This is an even better way to "map" the string functions onto all entries of the list


	short_string_list_numbers_over_5 = [ str(x) for x in short_list if x > 5] # Here is a little list comprehension with an if clause. THis will only turn numbers into strings which are bigger than 5

	print short_string_list_numbers_over_5

	
        
	# This is the end of our little collection of tips and tricks in Python. Hope it helped!



	


