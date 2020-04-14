class Money:
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

    def __repr__(self):
        return f"{self._currency} {str(self._amount)}"

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Franc(amount, "CHF")


class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

