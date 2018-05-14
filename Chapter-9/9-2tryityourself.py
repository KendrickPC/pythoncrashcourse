# 9-2 Three Restaurants:

# Start with your class from Exercise 9-2 . Create three different instances
# from the class, and call describe_restaurant() for each instance.


class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.restaurant_name + " is a restaurant that serves " \
            + self.cuisine_type + " food."
        print(msg)

    def open_restaurant(self):
        msg = self.restaurant_name.title() + " is now open."
        print(msg)


woodoo = Restaurant('woo doo food lab', 'all natural fusion')
woodoo.describe_restaurant()

buddys = Restaurant('buddys', 'wine and cafe bar')
buddys.describe_restaurant()

twinkeyz = Restaurant('twinkeyz', 'Mexican')
twinkeyz.describe_restaurant()
