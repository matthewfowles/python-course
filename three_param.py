

def my_func(a, b = 'b was not entered', c = 'c was not entered') :
	print(a), print(b), print(c)


my_func('This is first param')
my_func('This is first param', 'This is second param')
my_func('This is first param', 'This is second param', 'This is third param')

print(my_func)