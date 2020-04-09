class Dollar:
    def __init__(self, amount: int):
        self.amount: int = amount

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, Dollar):
            return self.amount == other.amount

        if isinstance(other, int):
            return self.amount == other

        raise TypeError()

    def __ne__(self, other):
        if isinstance(other, Dollar):
            return self.amount != other.amount

        if isinstance(other, int):
            return self.amount != other

        raise TypeError()
