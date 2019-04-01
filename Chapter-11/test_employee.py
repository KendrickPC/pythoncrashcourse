import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	""" Tests for the module employee. """

	def setUp(self):
		""" Make an employee to use in tests. """
		self.kenderson = Employee('kenderson', 'chang', 65000)

	def test_give_default_raise(self):
		""" Testing default raise working properly. """
		self.kenderson.give_raise()
		self.assertEqual(self.kenderson.salary, 70000)

	def test_give_custom_raise(self):
		""" Test that a custom raise works correctly. """
		self.kenderson.give_raise(10000)
		self.assertEqual(self.kenderson.salary, 75000)

unittest.main()
