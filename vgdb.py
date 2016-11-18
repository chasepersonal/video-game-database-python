#!user/bin/env python

# Moderatley Complex Python Program - Video Game List Program
#
# vgdb.py
#
# Chase Weyer
#
# This program will take standard inputs to create a list of video games and
# print them to an output file. If the user enters an inccorect value, or leaves
# a field blank, they will be prompted to re-enter until correct information is
# entered. If there is already a saved file, the user will be asked if they would
# like to view the file, then if they would like to overwirte or append it.
# Otherwise, a new file will be created. If there are any errors in opening the
# file, the program will terminate.

# import modules

import sys
import os.path

# function print welcome greeting

def greeting():
	
	# greeting to welcome user to the program

	print '\nWelcome to the Video Game List Program\n'
	
	print '\nThis program will allow you to enter any number of video games for organizing and listing purposes.\n'

# existing_file funtion

def existing_file():

	# list to store values for reading, writing, or appending a file depending
	# on user input
	
	mode = []
	
	# if 'file.txt' exists, file willl be opened and user will be asked
	# for input values.
	# if there is an error in opening the file, the program will quit and
	# perform an error message
	
	if os.path.isfile('vgdb.txt'):
		try:
			game_file = open("vgdb.txt", "r")
			print 'Saved file exists!\n'
		except IOError as e:
			sys.exit('\nUnalbe to open file')
		
		# end try-except
			
		# user inputs will run through while true loops to ensure invalid input
		# continuously occurs until correct input is entered
		# inputs will be converted to upper case to make error checking easier
	
		while True:
			answer = raw_input("Would you like to read the file? ").upper()
		
			# if correct value entered, existing file will print to the user
			# and loop will break
		
			if answer in ('Y', 'YES'):
			
			# blank newline will be printed before and during
			# the reading of the file to view contents of file easier
			
				print '\n'
			
				for x in game_file:
					print x
					print '\n'
				
				break
			
			elif answer not in ('N', 'NO', 'Y', 'YES'):
				print '\nInvalid Entry, Please indicate if you would like to view the file.\n'
		
		# end while true loop
			
		# during the following while true loop, if correct value is inputted,
		# mode value will be saved for later use and loop will break.
		# loop will continue if incorrect value is entered
	
		while True:
			edit_answer = raw_input("\nWould you like to append or overwrite the file? ").upper()
			if edit_answer in ('OVERWRITE', 'O'):
				mode = "w"
				break
			elif edit_answer in ('APPEND', 'A'):
				mode = "a"
				break
			else:
				print '\nInvalid Entry. Please indicate whether you would like to append or overwrite the file.\n'
			
		# end while true loop
		
		# will ensure exiting file closes
	
		game_file.close()
	
		# if file does not exist, mode will be saved as overwrite for use later
		# in the program	
			
	elif not os.path.isfile('vgdb.txt'):
		mode = "w"
	
	# mode value will be returned to main function
	
def num_input():
	
	# user will be asked to input number of games to process
	# input number is less than 2, error message will print until a number
	# above 2 is inputted
	
	while True:
		num = input("\nPlease enter the number of games you would like to process: ")
		if num < 2:
			print '\nInvalid number of games to process. Please enter 2 or more games.\n'
		else:
			break
	
	# end while true loop
	
	# message to be printed to user indicating the number they inputted
	
	print '\nYou will now be asked to input information for ',num,' games'
	
	# input value will be returned to main function

# main function

def main(num):
	
	num = num_input()
	
	games = []
	
	# loop for user input depending on num value entered
	# initializer for loop set to zero
	
	x = 0
	while x < n:
		
		# while true loops will repeat user input for console name,
		# game title, and game type if null value is entered.
		# otherwise, list for games will be appened with user input and
		# loop will break.
		
		while True:
			console= raw_input("\nPlease enter a console name: ")
			if console == '':
				print '\nInvalid Entry. Please enter a console name\n.'
			else:
				games.append(console)
				break
				
		# end while true loop
		
		while True:
			title = raw_input("Please enter the title of the game: ")
			if title == '':
				print '\nInvalid Entry. Please enter the title of the game\n.'
			else:
				games.append(title)
				break
				
		# end while true loop
		
		while True:
			typ = raw_input("Please enter the type of the game: ")
			if typ == '':
				print '\nInvalid Entry. Please enter the type of the game\n.'
			else:
				games.append(typ)
				break
		
		# end while true loop
				
		# counter initializer for while loop to make sure it doesn't run
		# continuously.
		
		x += 1
		
	# end while loop
	
	info_output(mode,games)


# function to print out saved information

def info_output(m, g):
	
	# file will be opened for overwrite or appending depending on saved
	# mode value.
	# if there is an error opening the file, the program will be terminated.
	
	try:
		game_file = open("vgdb.txt", m)
	except IOError as e:
		sys.exit('\nERROR: Unalbe to open file')
	
	# end try-except
	
	# list to hold header for printing purposes
	
	header = ["Console Name", "Game Title", "Game Type"]
	
	# message to tell user that results will be saved to an outside file
	
	print '\nThe following results displayed will be saved to file.txt.\n'
	
	# loop for print output initaized to zero
	
	x = 0
	
	# header will print in column format for easier viewing of the files
	# and write the contents to a new file if the user wanted to overwrite to an
	# existing file or if a new file is being created
	
	# if user wanted to append the file, program will header for viewing, but 
	# will only write game content to vgdb.txt
	
	if m == "w":
		print '\t'.join(header[:3])
		game_file.write('\t'.join(header[:3]))
		header = header[:3]
	elif m == "a":
		print '\t'.join(header[:3])
		header = header[:3]
	
	# loop will continue until all values of g are printed.
	# will print in column format with spaces for easier viewing
	
	while g:
		print '\n'
		game_file.write('\n')
		print '\t'.join(g[:3])
		game_file.write('\t'.join(g[:3]))
		g= g[3:]
		
		# loop counter to ensure all values of g are cycled through
		
		x += 1
		
	# end while loop
	
	# to ensure 'vgdb.txt' closes
	
	game_file.close()
	
	sys.exit()
# ensures execution of main program and subsequent functions

if __name__ == '__main__':
	greeting()
	existing_file()
	num_input()
	main(num)
	info_output(m, g)
