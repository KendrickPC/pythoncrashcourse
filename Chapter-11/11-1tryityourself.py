# 11-1. City, Country: Write a function that accepts two parameters: a city
# name and a country name. The function should return a single string of
# the form City, Country, such as Santiago, Chile. Store the function in
# a module called city_functions.py. Create a file called test_cities.py
# that tests the function you just wrote (remember that you need to import
# unittest and the function you want to test). Write a method called
# test_city_country() to verify that calling your function with values
# such as 'santiago' and 'chile' results in the correct string. Run
# test_cities.py, and make sure test_city_country() passes.

# formatted_city_function stored in city_functions.py
def get_formatted_city(city, country):
    full_city_name = city + ', ' + country
    return full_city_name.title()

# test_cities.py unittest
import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """ Tests for 'city_functions.py """
    def test_city_country(self):
        """ Do names like 'Cupertino, United States' work? """
        full_city_name = get_formatted_city('cupertino', 'united states')
        self.assertEqual(full_city_name, 'Cupertino, United States')

unittest.main()
