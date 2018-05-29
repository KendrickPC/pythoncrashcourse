# Battery Upgrade: 
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it is not already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the cars range.


class Car(object):
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

class Battery(object):
    """A simple attempt to model a battery from an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attribute."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Describing range of battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self, battery_size=85):
        """upgrade the battery_size kWh if possible"""
        if self.battery_size == 70:
            self.battery_size = 85
            print("The battery has been upgraded to 85 kWh.")
        else:
            print("The battery has already been upgraded.")
class ElectricCar(Car):
    """Represent aspects of an electric car """
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
        """Print statement describing battery size"""
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
"""Upgrading the battery for the first time"""
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
"""Attempting to upgrade the battery a ssecond time"""
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
