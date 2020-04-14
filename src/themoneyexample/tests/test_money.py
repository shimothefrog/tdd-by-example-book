import pytest

from src.themoneyexample.money import Money


class TestMoney:
    def test_multiplication(self):
        five = Money.dollar(5)

        assert Money.dollar(10) == five.times(2)
        assert Money.dollar(15) == five.times(3)

    def test_equality(self):
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.franc(5) != Money.dollar(6)
        assert Money.franc(5) != Money.dollar(5)

    def test_currency(self):
        assert "USD" == Money.dollar(1).currency()
        assert "CHF" == Money.franc(1).currency()
