
file_name = 'log.txt'


def print_contents():

	try: 
		file = open(file_name, 'r')
		print(file.read())
		file.close()
	except IOError:
		open(file_name, 'w')


def main() :

	print_contents();

	while True :
		text = input("Please enter the text you wish to store: ");

		if text == '':
			break

		file = open(file_name, 'a')
		file.write(text)
		file.close()

		print_contents();


main()