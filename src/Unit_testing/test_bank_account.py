import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == "__main__":
    unittest.main()
