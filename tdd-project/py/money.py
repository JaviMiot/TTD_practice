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

    def __str__(self) -> str:
        return f'{self.amount:0.2f} {self.currency}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} Object: {str(self)}'
