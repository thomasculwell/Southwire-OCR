# classes.py

class Dog:

	species = 'mammal'

	def __init__(self, name, age):
		self.name = name
		self.age = age

class Bulldog(Dog):

	def run(self, speed):
		return "{} runs {} and is {} years old".format(self.name, speed, self.age)

lucy = Bulldog('Indie', 4)

print(lucy.run('fast'))