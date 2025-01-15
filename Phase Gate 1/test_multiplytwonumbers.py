import unittest
import multiplytwonumbers

class TestFunctionMultiplyNumbers(unittest.TestCase):
	
	def test_that_two_numbers_can_multiply(self):
		actual = multiplytwonumbers.get_product(4)
		result = 40
		self.assertEqual(actual, result)