class Dollar:
    def __init__(self, amount: int):
        self.amount: int = amount

    def times(self, multiplier: int):
        self.amount *= multiplier
