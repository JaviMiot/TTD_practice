from functools import reduce

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *money):
        self.moneys.extend(money)

    def evaluate(self, currency: str) -> Money:

        filter_by_currency = filter(
            lambda money: money.currency == currency, self.moneys)

        total = reduce(lambda acc, money: acc +
                       money.amount, filter_by_currency, 0)

        return Money(total, currency)
