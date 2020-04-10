class Money:
    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int):
        pass

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
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> 'Franc':
        return Franc(amount)


class Dollar(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)
