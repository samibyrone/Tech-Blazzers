from bank_account_sample import Accounting
from unittest import TestCase


class TestAccounting(TestCase):

    def test_that_acccount_can_deposit(self):
        a1 = Accounting("samibyrone", 1972)
        a1.deposit(200000)
        a1.deposit(250000)
        self.assertAlmostEqual(a1.balance, 4500000)

