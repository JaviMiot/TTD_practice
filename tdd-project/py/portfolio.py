from functools import reduce

from money import Money
from bank import Bank


class Portfolio:
    def __init__(self):
        self.moneys = []
        self.exchange_rates = {'EUR->USD': 1.2, 'USD->KRW': 1100}

    def add(self, *money):
        self.moneys.extend(money)

    def evaluate(self, bank: Bank, currency: str) -> Money:
        total = 0.0
        failures = []

        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except KeyError as ke:
                failures.append(ke)

        if len(failures) == 0:
            return Money(total, currency)

        failureMessage = ','.join(f.args[0] for f in failures)
        raise Exception(f'Missing exchange rate(s):[{failureMessage}]')

    def _convert(self, money: Money, currency: str) -> Money:

        key = f'{money.currency}->{currency}'
        if money.currency == currency:
            return money
        money.amount *= self.exchange_rates[key]
        return money
