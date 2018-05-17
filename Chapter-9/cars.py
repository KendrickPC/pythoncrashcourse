# You can use methods like this to control how users of your program update
# values such as an odometer reading, but anyone with access to the program
# can set the odometer reading to any value by accessing the attribute
# directly. Effective security takes extreme attention to detail in addition
# to basic checks like those shown here.

# You can easily modify this method to reject negative increments so no one
# uses this function to roll back an odometer.

# Working with Classes and Instances


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        car_info = str(self.year) + ' ' + self.make + ' ' + self.model
        return car_info.title()

    def read_odometer(self):
        """Print statement showing mileage of car"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer silly!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

ken_new_car = Car('infiniti', 'g37', '2016')
print(ken_new_car.get_descriptive_name())

ken_new_car.update_odometer(27)
# Testing rollback odometer method below
# ken_new_car.update_odometer(22)
ken_new_car.read_odometer()


ken_used_car = Car('toyota', 'camry', '2013')
print(ken_used_car.get_descriptive_name())

ken_used_car.update_odometer(56000)
ken_used_car.read_odometer()
ken_used_car.increment_odometer(100)
ken_used_car.read_odometer()
