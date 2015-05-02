#!/usr/bin/python3
#
#  A Truly Awesome Program
#       doggies.py
#
#  by: Matthew Fowles
#
#


dogs = []

class dog:

	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

	def output(self):
		return self.name, self.breed


if __name__ == "__main__":

	while True:

		name = input('Name: ')
		if not name: 
			break

		breed = input('Breed: ')

		dogs.append(dog(name, breed))


		print('DOGS')
		for index, d in enumerate(dogs):
			fmt = '{}. {}:{}'
			output = dog.output(d);
			print(fmt.format(index, output[0], output[1]))

		print('*' * 20)