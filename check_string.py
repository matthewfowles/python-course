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
		return

	# Check they made the string uppercase
	if string.isupper() != True :
		print('This is not uppercase!')
		main()
		return

	# Check it has a period at the end......
	if string.endswith('.') != True :
		print('This does not end with a period!')
		main()
		return

	success()

def success() :

	# Print successs message

	print('Woohoo strong with the string you are!')

main()

