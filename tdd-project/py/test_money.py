import unittest
from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):

    def test_Multiplication(self):
        fiveEuros = Money(5, 'EUR')
        tenEuros = Money(10, 'EUR')
        self.assertEqual(fiveEuros.times(2), tenEuros)

    def test_Division(self):
        originalMoney = Money(4002, 'KRW')
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, 'KRW')

        self.assertEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision)

    def test_Addition(self):
        fifteenDollars = Money(15, 'USD')
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(portfolio.evaluate('USD'), fifteenDollars)

    def test_addition_of_dollars_to_euros(self):
        five_dollars = Money(5, 'USD')
        ten_euros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expectValue = Money(17, 'USD')
        actualValue = portfolio.evaluate('USD')
        self.assertEqual(actualValue, expectValue)

    def test_addition_of_dollars_and_wons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_wons = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundred_wons)
        expected_value = Money(2200, "KRW")
        self.assertEqual(portfolio.evaluate('KRW'), expected_value)


if __name__ == '__main__':
    unittest.main()
