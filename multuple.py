#
# This is a program that takes a tuple of tuples with two numbers and loops through and multiply's them.
#


tuples = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for tuple in tuples :
	total = tuple[0] * tuple[1]
	print "{0:5}".format(total), '=', tuple[0], 'x', tuple[1]