#!/usr/bin/python3
#
#  A Truly Awesome Program
#       secret_code.py
#
#  by: Matthew Fowles
#
#
"A project to compile secret codes"



text =  input("input your message: ");
message = ''


for char in text :
	message += chr(ord(char) + 1)

print(message[::-1])