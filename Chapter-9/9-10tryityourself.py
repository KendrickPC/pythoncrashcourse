# 9-10. Imported Restaurant: Using your latest Restaurant class,
# store it in a module. Make a separate file that imports Restaurant.
# Make a Restaurant instance, and call one of Restaurants methods
# to show that the import statement is working properly.


from restaurantClass import Restaurant


woo_doo_lab = Restaurant('Woo Doo Lab', 'healthy food')
woo_doo_lab.describe_restaurant()
woo_doo_lab.open_restaurant()

# pep8 compliant
