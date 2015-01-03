


def capital(e) :
	return e.capitalize();

def titilate(e) :
	return e.title

def up(e) :
	return e.upper()

def down(e) :
	return e.lower()

def leave() :
	return 'See ya!'
	


matrix = {
	"capitalize": capital,
	"title": titilate,
	"upper": up,
	"lower": down,
	"exit": leave
}


function = raw_input('Enter a function name (capitalize, title, upper, lower, or exit): ')
string = raw_input('Enter a string: ')

result = matrix[function](string)

print result