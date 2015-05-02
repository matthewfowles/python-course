#!/usr/bin/python3
#
#  A Truly Awesome Program
#       final.py
#
#  by: Matthew Fowles
#
#
""" Takes a file as a command line argument. Prints out a list 
	of word lengths and how many times that word length appears.
"""

import sys, string, re

def word_count(content):


	regex = re.compile('[%s]' % re.escape(string.punctuation))
	breakdown = regex.sub('', content).replace(string.punctuation, '').strip().split()

	count_lst = [0] * (len(max(breakdown, key=len)) + 1)

	for word in breakdown:
		count_lst[len(word)] += 1

	for index, amount in enumerate(count_lst):
		if not amount == 0:
			print(index, amount)



if __name__ == "__main__" and len(sys.argv) > 1:


	try:
		file = open(sys.argv[1], 'r')
		content = file.read()
		word_count(content)

	except  IOError:
		print('Your file cannot be found or does not exist!')

else: 
	print('You need to provide a file')

	