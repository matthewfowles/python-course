#
# This is a guessing number game.
#
"""
This program takes makes a random number between 1 and 99 and asks the user to guess it. 
"""

from random import randint


number = randint(1,99)

# create main function
def main() :

	print('Try to guess the number between 0 and 99.')


	while True:


		guess = int(input("Please enter a guess: "))


		if guess > number :
			print('Too high! Try again.')
			continue
		elif guess < number :
			print('Too low! Try again.')
			continue
		elif guess == number :
			print('Congratulations you got it!')
			break

main()