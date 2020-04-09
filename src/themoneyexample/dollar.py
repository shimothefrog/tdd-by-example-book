class Dollar:
    def __init__(self, amount: int):
        self._amount: int = amount

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, Dollar):
            return self._amount == other._amount

        if isinstance(other, int):
            return self._amount == other

        raise TypeError()

    def __ne__(self, other):
        if isinstance(other, Dollar):
            return self._amount != other._amount

        if isinstance(other, int):
            return self._amount != other

        raise TypeError()
