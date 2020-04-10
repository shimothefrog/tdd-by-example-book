class Money:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int):
        pass

    def currency(self) -> str:
        return self._currency

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if isinstance(other, Money):
            return self._amount == other._amount

        if isinstance(other, int):
            return self._amount == other

        raise TypeError()

    def __ne__(self, other):
        if type(self) != type(other):
            return True

        if isinstance(other, Money):
            return self._amount != other._amount

        if isinstance(other, int):
            return self._amount != other

        raise TypeError()

    @staticmethod
    def dollar(amount: int) -> 'Dollar':
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Franc(amount, "CHF")


class Dollar(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> 'Dollar':
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount: int, currency: str):
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> 'Franc':
        return Money.franc(self._amount * multiplier)

