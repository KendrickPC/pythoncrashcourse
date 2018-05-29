# Has not been checeked with PEP8 standardization
from car import *

my_tesla = ElectricCar('tesla', 'model s', 2018)

""" Importing get_descriptive_name function from class Car """
print(my_tesla.get_descriptive_name())
# TypeError: super() argument 1 must be type, not classobj
# From class ElectricCar __init__ function. 

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# TypeError: super() argument 1 must be type, not instance
