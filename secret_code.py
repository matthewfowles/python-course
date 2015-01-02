



text =  raw_input("input your message: ");
message = ''


for char in text :
	message += chr(ord(char) + 1)

print message[::-1]