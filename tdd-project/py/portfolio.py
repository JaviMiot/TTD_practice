from functools import reduce

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self.eur_to_usd = 1.2

    def add(self, *money):
        self.moneys.extend(money)

    def evaluate(self, currency: str) -> Money:

        map_by_currency = list(map(
            lambda money: self._convert(money, currency), self.moneys))

        total = reduce(lambda acc, money: acc +
                       money.amount, map_by_currency, 0)

        return Money(total, currency)

    def _convert(self, money: Money, currency: str) -> Money:
        if money.currency == currency:
            return money
        money.amount *= self.eur_to_usd
        return money
