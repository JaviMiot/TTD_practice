import unittest
from money import Money
from portfolio import Portfolio
from bank import Bank


class TestMoney(unittest.TestCase):

    def setUp(self) -> None:
        self.bank = Bank()
        self.bank.add_exchange_rate("EUR", "USD", 1.2)
        self.bank.add_exchange_rate("USD", "KRW", 1100)

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
        self.assertEqual(portfolio.evaluate(self.bank, 'USD'), fifteenDollars)

    def test_addition_of_dollars_to_euros(self):
        five_dollars = Money(5, 'USD')
        ten_euros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expectValue = Money(17, 'USD')
        actualValue = portfolio.evaluate(self.bank, 'USD')
        self.assertEqual(actualValue, expectValue)

    def test_addition_of_dollars_and_wons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_wons = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundred_wons)
        expected_value = Money(2200, "KRW")
        self.assertEqual(portfolio.evaluate(self.bank, 'KRW'), expected_value)

    def test_addition_with_multiple_missing_exchange_rates(self):
        oneDollar = Money(1, 'USD')
        oneEuro = Money(1, 'EUR')
        oneWon = Money(1, 'KRW')
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
            Exception,
            "Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]",
        ):
            portfolio.evaluate(self.bank, "Kalganid")

    def test_conversion(self):
        bank = Bank()
        bank.add_exchange_rate('EUR', 'USD', 1.2)
        tenEuros = Money(10, 'EUR')
        self.assertEqual(bank.convert(tenEuros, 'USD'), Money(12, 'USD'))

    def test_conversion_with_missing_exchange_rate(self):
        bank = Bank()
        tenEuros = Money(10, "EUR")
        with self.assertRaisesRegex(Exception, "EUR->Kalganid"):
            bank.convert(tenEuros, "Kalganid")


if __name__ == '__main__':
    unittest.main()
