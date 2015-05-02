#
# This is a program that takes a tuple of tuples with two numbers and loops through and multiply's them.
#


tpls = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for tpl in tpls :
	fmt = '{0:>4} = {1:>2} x {2:>2}'
	print(fmt.format(tpl[0] * tpl[1], tpl[0], tpl[1]))