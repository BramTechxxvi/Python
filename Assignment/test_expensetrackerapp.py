import unittest
import expensetrackerapp

class TestExpenseTrackerApp(unittest.TestCase):

    def test_that_date_function_exist(self):
        date = '2025-02-12'
        expensetrackerapp.get_date(date)
    
    def test_that_function_returns_date(self):
         pass
    
    #def test_kk_jj__(self):
         

    def test_that_total_function_exist(self):
        list1 = [9, 10, 15]
        expensetrackerapp.get_totalexpenses([9, 10, 15])

    def test_that_total_function_return_invalid_input(self):
        list1 = ['a', 'k', 'l']
        actual = expensetrackerapp.get_totalexpenses(list1)
        result = "Invalid... input"
        self.assertEqual(actual, result)

    def test_that_total_function_can_sum(self):
        list1 = [80, 10 , 15]
        actual = expensetrackerapp.get_totalexpenses(list1)
        result = 105
        self.assertEqual(actual, result)


if __name__ == "__main__":
	unittest.main()