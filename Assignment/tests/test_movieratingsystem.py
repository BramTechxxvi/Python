import unittest
import movieratingsystem
from datetime import datetime


class TestMovieRatingSystem(unittest.TestCase):

	def test_that_function_can_return_header(self):
		actual = movieratingsystem.get_header()
		expected = "==========  MOVIE RATING SYSTEM  ==========\n"
		self.assertEqual(actual, expected)

	def test_that_function_can_return_features(self):
		actual = movieratingsystem.get_features()
		expected = " 1. Add a Movie\n 2. Rate a Movie\n 3. View ratings\n 4. View average ratings\n 5. Exit"
		self.assertEqual(actual, expected)

	def test_that_function_can_return_date(self):
		date = "2025-08-21"
		actual = movieratingsystem.get_date()
		expected = datetime.now().strptime(date,"%Y-%m-%d")
		self.assertTrue(actual, expected)

	def test_movie_name_function(self):
		name = "Intercept"
		actual = movieratingsystem.get_movie_name(name)
		expected = "Intercept"
		self.assertTrue(actual, expected)

	def test_that_movie_name_function_can_return_invalid(self):
		name = " "
		actual = movieratingsystem.get_movie_name(name)
		expected = "kjsusjwjqj"
		self.assertFalse(actual, expected)

	def test_rate_movie_function(self):
		actual = movieratingsystem.rate_movie(5)
		expected = 5
		self.assertEqual(actual, expected)

	def test_that_rate_movie_function_can_return_invalid(self):
		actual = movieratingsystem.rate_movie(0)
		expected = 0
		self.assertFalse(actual, expected)

	def test_view_ratings_function(self):
		pass

	def test_that_view_rating_function_can_return_invalid(self):
		pass

	def test_average_rating_function(self):
		pass

	def test_that_average_rating_function_can_return_invalid(self):
		pass

if __name__ == '__main__':
		unittest.main()