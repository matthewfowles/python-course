#
# This program takes and sentence and splits the words into two tuples. Those starting with and without capitals.
#


# Get users text
text = input('Please enter some text: ');

# strip whitespace and split words up
words = text.strip().split()

# declare our lists
upper = []
lower = []


# loop through and assign to a list
for word in words :
	if any(i.isupper() for i in word) :
		upper.append(word)
	else :
		lower.append(word)

all_words = upper + lower

for word in all_words:
	print(word) 

