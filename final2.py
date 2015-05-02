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

import sys, string, re, math

def word_count(content):


	regex = re.compile('[%s]' % re.escape(string.punctuation))
	breakdown = regex.sub('', content).replace(string.punctuation, '').strip().split()

	count_lst = [0] * (len(max(breakdown, key=len)) + 1)

	for word in breakdown:
		count_lst[len(word)] += 1

	for index, amount in enumerate(count_lst):
		if not amount == 0:
			print(index, amount)

	#  Pass to histogram function

	histogram(count_lst)


def histogram(lst):

	lst.pop(0)

	start_num = closest_hundred(max(lst))
	numbers = get_multiples(start_num);

	fmt = '{0:>4} -|'
	
	for i in reversed(numbers):
		if i == 0:
			break
		for x in lst:
			if x >= i:
				fmt += '{0:>3}'.format('*')
			else:
				fmt += ' ' * 3 

		if i % 100 == 0:
			print(fmt.format(i))
		else :
			print(fmt.format('')) 
		fmt = "{0:>4} -|"


	bottom = ' ' * 6
	bar = ' ' * 3 + '{0:<3}'.format('0')

	for x in range(0, len(lst) + 1):
		if x != (len(lst)):
			bar += '+--'
		else: 
			bar += '+' 
		bottom += '{0:<3}'.format(x)

	print(bar)
	print(bottom)



def get_multiples(start_num):
	numbers = [];
	for i in range(0, start_num + 1):
		if(i % 20 == 0):
			numbers.append(i)
	return numbers;

	
def closest_hundred(num):
	return int(math.ceil(num / 100.0)) * 100


if __name__ == "__main__" and len(sys.argv) > 1:


	try:
		file = open(sys.argv[1], 'r')
		content = file.read()
		word_count(content)

	except  IOError:
		print('Your file cannot be found or does not exist!')

else: 
	print('You need to provide a file')