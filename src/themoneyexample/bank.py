from src.themoneyexample.money import Money, Expression


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(10)
