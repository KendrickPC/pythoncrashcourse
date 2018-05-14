# Making an object from a class is called instantiation,
# and you work with instances of a class.

# The self parameter is required in the method definition, and 
# it must come first before the other parameters. It must be included
# in the definition because when Python calls this __init__() method 
# later (to create an instance of Dog), the method call will 
# automatically pass the self argument.

# When you create a class in Python 2.7, you need to make one minor 
# change. You include the term object in parentheses when you create
# a class:
# class ClassName(object): 
# This makes Python 2.7 classes behave more like Python 3 classes,
# which makes your work easier overall. The Dog class would be defined
# like this in Python 2.7: class Dog(object):


class Dog(object):
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")


my_dog = Dog('Abigail', 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Perkins', 8)
your_dog.sit()
your_dog.roll_over()

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Stopped at Creating Multiple Instances