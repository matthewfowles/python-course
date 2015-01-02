
def main() :

	

	while True :
		text = raw_input("Please enter the text you wish to store: ");

		if text == '' :
			break;

		file = open('log.txt', 'a')
		file.write(text)
		file.close()

		file = open('log.txt', 'r')
		print file.read()
		file.close()
	

main()