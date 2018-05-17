# 9-4. Number Served: 
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the number
# of customers the restaurant has served, and then change this value and
# print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who have been served. Call this method with any
# number you like that could represent how many customers were served in,
# say, a day of business.


class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes the restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 1

    def describe_restaurant(self):
        """Displays a summary of the restaurant"""
        msg = self.restaurant_name + " is a restaurant that serves " \
            + self.cuisine_type + " food."
        print(msg)

    def open_restaurant(self):
        """Displays a message that the restaurant is open"""
        msg = self.restaurant_name.title() + " is now open."
        print(msg)

    def set_number_served(self, number_served):
        """
        Allow user to set the number_served
        """
        self.number_served = number_served

    def increment_number_served(self, new_number_served):
        # add the given amount to the number_served reading
        self.number_served += new_number_served

restaurant = Restaurant('woo doo food lab', 'all natural fusion')
restaurant.describe_restaurant()

print("Number served: " + str(restaurant.number_served))
restaurant.number_served = 23
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(45)
print("Number served: " + str(restaurant.number_served))

# += adds to the sum total
restaurant.increment_number_served(8)
print("Number served: " + str(restaurant.number_served))
