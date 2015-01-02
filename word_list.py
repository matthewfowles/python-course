#
# This program takes and sentence and splits the words into two tuples. Those starting with and without capitals.
#


# Get users text
text = raw_input('Please enter some text: ');

# strip whitespace and split words up
words = text.strip().split()

# declare our lists
upper = []
lower = []


# loop through and assign to a list
for word in words :
	if word.isupper() :
		upper.append(word)
	else :
		lower.append(word)

# Loop through bost list in one for statement. Log uppercase words first and lowercase words last!
for item in range(0, len(upper) + len(lower)) : 
	if item <= len(upper) :
		print upper.pop()
	else :
		print lower.pop()

