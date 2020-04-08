class Dollar:
    def __init__(self, amount: int):
        self.amount: int = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
