import unittest
from ClassWork.bankAccount.account import Account
class AccountTest(unittest.TestCase):

    def setUp(self):
        self.my_app = Account("John")

    def test_if_account_has_balance(self):
        my_app = Account("John")
        self.assertEqual(0, my_app.get_balance())

    def test_if_account_can_deposit(self):
        my_app = Account("John")
        my_app.deposit(1_000)
        self.assertEqual(1_000, my_app.get_balance())

    def test_if_account_can_deposit_invalid_amount__raisesValurError(self):
        my_app = Account("John")
        with self.assertRaises(ValueError):
            my_app.deposit(-1_000)
        self.assertEqual(0, my_app.get_balance())

    def test_if_account_can_withdraw(self):
        my_app = Account("John")
        my_app.deposit(10_000)
        my_app.withdraw(5_000)
        self.assertEqual(5_000, my_app.get_balance())

    def test_if_account_can_withdraw_amount_greater_than_balance__raisesValueError(self):
        my_app = Account("John")
        my_app.deposit(10_000)
        with self.assertRaises(ValueError):
            my_app.withdraw(100_000)

    def test_if_account_can_withdraw_with_invalid_amount__raiseValueError(self):
        my_app = Account("John")
        my_app.deposit(10_000)
        with self.assertRaises(ValueError):
            my_app.withdraw(-10_000)
        self.assertEqual(10_000, my_app.get_balance())

    def test_if_account_can_view_transaction(self):
        my_app = Account("John")
        my_app.deposit(10_000)
        my_app.withdraw(5_000)
        self.assertEqual(2, my_app.view_history())



if __name__ == '__main__':
    unittest.main()
