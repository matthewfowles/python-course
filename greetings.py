#
# This is a program that takes a first and last name and prints them out.
#
"""
This program takes raw string input's for first and last name. It will then print out each name.
If you fail to provide one of your names it will ask you for them again.
"""

from __future__ import print_function  

# declare our two variables

first_name = '' 
last_name = ''


# build our main function which will run on start
def main() : 
	get_first()
	get_last()
	valid()

def get_first() : 
	# get raw input for first name and bind to global variable
	global first_name
	first_name = raw_input('Hey whats your first name: ')

def get_last() :
	# get raw input for last name and bind to global variable
	global last_name
	last_name = raw_input('Hey whats your last name: ')

def valid() :
	# Check if first name has been provided!
	if not first_name:
		print('As Gandalf would say you shall not pass without a first name')
		get_first()
		# if provided loop back round
		valid()
		return
	# Check if last name has been provided!
	if not last_name:
		print('As Gandalf would say you shall not pass without a last name')
		get_last()
		# if provided loop back round
		valid()
		return

		# if everything has been provided then finish!
	if first_name and last_name :
		# send back the answer and make sure capatilise the name
		print("I am pleased to meet you,", first_name.title(), last_name.title())


# run our main function

main();