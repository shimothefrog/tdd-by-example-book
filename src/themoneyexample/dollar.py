class Dollar:
    def __init__(self, amount: int):
        self.amount: int = amount

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            raise TypeError()

        return self.amount == other.amount

    def __ne__(self, other):
        if not isinstance(other, Dollar):
            raise TypeError()

        return self.amount != other.amount
