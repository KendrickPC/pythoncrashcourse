import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """ Tests for 'city_functions.py """
    def test_city_country(self):
        """ Do names like 'Cupertino, United States' work? """
        full_city_info = get_formatted_city('cupertino', 'united states')
        self.assertEqual(full_city_info, 'Cupertino, United States')

    def test_city_country_population(self):
        """ Do names like 'Cupertino, United States - 50000' work? """
        full_city_info = get_formatted_city('cupertino', 'united states', '50000')
        self.assertEqual(full_city_info, 'Cupertino, United States - 50000')

unittest.main()
