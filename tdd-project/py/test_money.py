import unittest


class Money:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divider: int):
        return Money(self.amount / divider, self.currency)

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount and self.currency == other.currency


class TestMoney(unittest.TestCase):
    def testMultiplicationDollars(self):
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        self.assertEqual(fiveDollars.times(2), tenDollars)

    def testMultiplicationEuro(self):
        fiveEuros = Money(5, 'EUR')
        tenEuros = Money(10, 'EUR')
        self.assertEqual(fiveEuros.times(2), tenEuros)

    def testDivision(self):
        originalMoney = Money(4002, 'KRW')
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, 'KRW')

        self.assertEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision)


if __name__ == '__main__':
    unittest.main()
