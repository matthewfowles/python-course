#
# This program takes a sentence and splits the words into a tuple and dict. We then lst those words out against the number they are in the tuple.
#


all_words = set()
words_map = {}

def sort(text) : 
	words = text.strip().split()
	for word in words :
		current = len(all_words)
		all_words.add(word)
		new = len(all_words)

		if new > current :
			words_map[word] = len(all_words)
			
	results()



def results() :
	for key, value in sorted(words_map.items()): 
		print(key, value)


while True:
	text = input("Please enter some text: ")

	if text:
		sort(text)
	else :
		print('finished')
		break
