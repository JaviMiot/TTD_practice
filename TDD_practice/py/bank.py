from money import Money


class Bank:
    def __init__(self):
        self.exchange_rates = {}

    def add_exchange_rate(self, from_currency, to_currency, rate):
        self.exchange_rates[f'{from_currency}->{to_currency}'] = rate

    def convert(self, money, to_currency):
        key = f'{money.currency}->{to_currency}'
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        if key in self.exchange_rates:
            return Money(money.amount * self.exchange_rates[key], to_currency)

        raise KeyError(key)
