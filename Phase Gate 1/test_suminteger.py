import unittest
import suminteger

class TestFunctionAddInteger(unittest.TestCase):
	def test_that_function_exist(self):
		suminteger.get_sum(932)

	def test_that_function_return_invalid_input_with_decimal_number(self):
		actual = suminteger.get_sum(932)
		result = 14
		self.assertEqual(actual, result)

	def test_that_function_return_invalid_input_with_decimal_number(self):
		actual = suminteger.get_sum(78.9)
		result = 'invalid input'
		self.assertEqual(actual, result)

	def test_that_function_return_invalid_input_with_character(self):
		actual = suminteger.get_sum('a')
		result = 'invalid input'
		self.assertEqual(actual, result)

	def test_that_function_return_invalid_input_with_whitespace(self):
		actual = suminteger.get_sum(' ')
		result = 'invalid input'
		self.assertEqual(actual, result)

	def test_that_function_return_negative_input_with_negative_number(self):
		actual = suminteger.get_sum(-30)
		result = 'invalid input'
		self.assertEqual(actual, result)
		