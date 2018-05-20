# 9-6 Ice Cream Stand
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


from restaurant import *


class IceCreamStand(Restaurant):
	"""Represent IceCreamStand"""
	def __init__(self, restaurant_name, cuisine_type='Dessert'):
		super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def display_flavors(self):
		"""Display flavors"""
		print("The following flavors are available:")
		for flavor in self.flavors:
			print(flavor.title())

cold_stone = IceCreamStand('Cold Stone Creamery')
cold_stone.flavors = ['rocky road', 'rainbow sherbet', 'mint chocolate chip']

cold_stone.describe_restaurant()
cold_stone.display_flavors()