#
# This is a program that takes a string and checks it.
#
"""
This program takes raw string input. It will then check the string.
if the string is not all upper case and ends with a period. Then we ask you to try again.
"""

# declare our string variable
string = ''

# create our main function
def main() :
	global string
	print('Please enter a string all in uppercase that ends in a period')
	string = input('String: ')

	validate();

# create our validate function
def validate() : 

	# Check they entered something
	if string == '' :
		print('You need to enter something!')
		main()

	# Check whether the string has both not uppercase and has no period at the end.
	elif not string.isupper() and not string.endswith('.'):
		print('This is not uppercase and does not end with a period!')
		main()

	# Check they made the string uppercase
	elif not string.isupper():
		print('This is not uppercase!')
		main()

	# Check it has a period at the end......
	elif not string.endswith('.'):
		print('This does not end with a period!')
		main()

	else: 
		success()

def success() :

	# Print successs message

	print('Woohoo strong with the string you are!')

main()

