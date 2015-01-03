

print 'Please enter a number to divide by 10'

while True :

	number = raw_input('Please enter a number: ')

	try:
		print (float(10) / int(number))
		continue

	except ValueError :
		print 'This is not a valid value!'
		continue

	except ZeroDivisionError :
		print 'You cannot divide by zero!'
		continue
