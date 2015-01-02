#
# This is a guessing number game.
#
"""
This program takes makes a random number between 0 and 20 and asks the user to guess it. 
Rules are below:

Each guess should be checked against a number stored in the "secret" variable, to which a value between 1 and 20 should be assigned at the start. 
Otherwise it should report whether the guess was higher or lower than the secret. 
If the user guesses correctly, the loop should terminate. 
The loop should also keep a count of the user's guesses, and should terminate if the user makes five incorrect guesses. 
After the loop is over, the program should print the secret if the user didn't guess it, or a congratulatory message if the user guessed correctly.

"""

from random import randint


number = randint(0,20)
count = 5;

# create main function
def main() :

	print 'Try to guess the number between 0 and 20. You have five lives'
	global count


	while True:

		if count == 0 : 
			print 'You have lost all your lives!'
			print 'The number was:', number
			break

		guess = int(raw_input("Please enter a guess: "))

		count -= 1

		if guess != number :
			print 'Sorry you did not guess correct!'
			print count, 'Lives left!'
			continue

		if guess == number :
			print 'Congratulations you win!'
			break


main()
