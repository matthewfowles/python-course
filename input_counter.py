#
# This program takes a sentence and splits the words into a tuple and dict. We then lst those words out against the number they are in the tuple.
#


from sets import Set

all_words = set([])
words_map = {}

text = ''

count = 0


def main() :
	global text
	text = raw_input("Please enter some text: ")

	if text  == '' :
		return
	else :
		sort()

def sort() : 

	words = text.strip().split()

	for word in words :

		if word not in all_words :
			global count
			all_words.add(word)
			words_map[word] = count
			count += 1;

	results()
	main()



def results() :


	for item in all_words : 
		print item, words_map[item]


main()