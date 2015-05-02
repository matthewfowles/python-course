#!/usr/bin/python3
#
#  A Truly Awesome Program
#       caser.py
#
#  by: Matthew Fowles
#
#

def capital(e) :
	return e.capitalize();

def titilate(e) :
	return e.title()

def up(e) :
	return e.upper()

def down(e) :
	return e.lower()

def exit(e):
	return 'Goodbye for now!'
	

matrix = {
	"capitalize": capital,
	"title": titilate,
	"upper": up,
	"lower": down,
	"exit": exit
}


if __name__ == "__main__":

	while True:

		function = input('Enter a function name (capitalize, title, upper, lower, or exit): ')
		string = input('Enter a string: ')

		result = matrix[function](string)

		print(result)

		if function == 'exit':
			break