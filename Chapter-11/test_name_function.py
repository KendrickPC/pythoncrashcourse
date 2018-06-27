import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py'. """
    def test_first_last_name(self):
        """ Do names like 'Barack Obama' work? """
        formatted_name = get_formatted_name('barack', 'obama')
        self.assertEqual(formatted_name, 'Barack Obama')

    def test_first_last_middle_name(self):
        """ Do names like 'Barack Hussein Obama' work? """
        formatted_name = get_formatted_name('barack', 'obama', 'hussein')
        self.assertEqual(formatted_name, 'Barack Hussein Obama')

unittest.main()
