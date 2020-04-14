from abc import ABC


class Expression(ABC):
    pass


class Money(Expression):
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return self._amount == other._amount \
                and self._currency == other._currency

        raise TypeError()

    def __ne__(self, other):
        if isinstance(other, Money):
            return not self == other

        raise TypeError()

    def __add__(self, other) -> Expression:
        if isinstance(other, Money):
            return Money(self._amount + other._amount, self._currency)

        raise TypeError()

    def __repr__(self):
        return f"{self._currency} {str(self._amount)}"

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Money(amount, "CHF")
