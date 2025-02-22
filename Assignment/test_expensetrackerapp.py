import unittest
import expensetrackerapp

class TestExpenseTrackerApp(unittest.TestCase):

    def test_expense_tracker_function_can_sum_total(self):
        list1 = [80, 10 , 15]
        actual = expensetrackerapp.get_totalexpenses(list1)
        result = 105
        self.assertEqual(actual, result)
	
    def test_expense_tracker_function_return_invalid(self):
        list2 = ["lion", "kiolp", "po"]
        actual = expensetrackerapp.get_totalexpenses(list2)
        result = "Invalid input"
        self.assertEqual(actual, result)


if __name__ == "__main__":
	unittest.main()